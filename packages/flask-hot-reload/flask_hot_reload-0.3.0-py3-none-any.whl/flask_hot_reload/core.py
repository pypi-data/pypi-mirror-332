import os
from typing import Set, List, Optional
from flask import Blueprint, Flask, Response
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent
from flask_sock import Sock
from simple_websocket import Server as WebSocket
from colorama import Fore, Style


class HotReload:
    def __init__(self, 
                 app: Optional['Flask'] = None, 
                 includes: Optional[List[str]] = None, 
                 excludes: Optional[List[str]] = None) -> None:
        """
        初始化热重载实例
        :param app: Flask应用实例
        :param includes: 要监控的目录列表，如果为None则默认监控templates和static目录
        :param excludes: 要排除的目录名称列表
        """
        self.app: 'Flask' = app
        # 默认监控templates和static目录
        self.includes: List[str] = includes or ['templates', 'static']
        self.excludes: Set[str] = set(excludes or [])
        self.observer = Observer()
        self.clients: Set['WebSocket'] = set()
        
        if app is not None:
            self.init_app(app)

    def _should_ignore_path(self, file_path: str) -> bool:
        """
        检查是否应该忽略这个文件路径
        :param file_path: 要检查的文件路径
        :return: 如果应该忽略返回True，否则返回False
        """
        abs_path: str = os.path.abspath(file_path)
        # 检查是否在排除目录中
        for exclude in self.excludes:
            if exclude in abs_path.split(os.sep):
                return True
        return False

    def _handle_file_change(self, event_type: str, file_path: str) -> None:
        """
        处理文件变更
        :param event_type: 事件类型（created/modified/deleted/moved）
        :param file_path: 文件路径
        """
        if self._should_ignore_path(file_path):
            print(f"{Fore.YELLOW}Ignoring {event_type} in excluded path: {file_path}{Style.RESET_ALL}")
            return

        file_ext: str = os.path.splitext(file_path)[1].lower()
        
        # 如果是Python文件变更，执行完全重载
        if file_ext == '.py':
            print(f"{Fore.RED}Python file {file_path} was {event_type}, performing full reload{Style.RESET_ALL}")
            self._notify_clients('full-reload')
        # 如果是其他文件，执行普通重载
        else:
            print(f"{Fore.GREEN}File {file_path} was {event_type}{Style.RESET_ALL}")
            self._notify_clients('reload')

    def _start_file_monitor(self) -> None:
        hot_reload = self
        
        class FileChangeHandler(FileSystemEventHandler):
            def on_created(self, event: FileSystemEvent) -> None:
                if event.is_directory:
                    return
                hot_reload._handle_file_change('created', event.src_path)

            def on_modified(self, event: FileSystemEvent) -> None:
                if event.is_directory:
                    return
                hot_reload._handle_file_change('modified', event.src_path)

            def on_deleted(self, event: FileSystemEvent) -> None:
                if event.is_directory:
                    return
                hot_reload._handle_file_change('deleted', event.src_path)

            def on_moved(self, event: FileSystemEvent) -> None:
                if event.is_directory:
                    return
                # 处理移动的源文件和目标文件
                hot_reload._handle_file_change('moved', event.src_path)
                hot_reload._handle_file_change('moved', event.dest_path)

        # 监控所有包含的目录
        for include_path in self.includes:
            if isinstance(include_path, str):
                abs_path: str = os.path.abspath(include_path)
                if os.path.exists(abs_path):
                    print(f"{Fore.CYAN}Watching directory: {abs_path}{Style.RESET_ALL}")
                    self.observer.schedule(FileChangeHandler(), abs_path, recursive=True)
                else:
                    print(f"{Fore.RED}Warning: Directory not found: {abs_path}{Style.RESET_ALL}")
        
        self.observer.start()

    def init_app(self, app: 'Flask') -> None:
        self.app = app
        self.sock = Sock(app)
        
        # 创建一个Blueprint来处理WebSocket连接
        hot_reload_bp: 'Blueprint' = Blueprint('hot_reload', __name__)
        
        @hot_reload_bp.route('/hot-reload-ws')
        def hot_reload_ws() -> str:
            return """
                <script>
                    (function() {
                        var ws = new WebSocket('ws://' + location.host + '/ws');
                        ws.onmessage = function(event) {
                            if (event.data === 'reload') {
                                location.reload();
                            } else if (event.data === 'full-reload') {
                                // 对于Python文件的变更, 等待一段时间后再刷新
                                // 这样给服务器一些时间来重启
                                setTimeout(function() {
                                    location.reload();
                                }, 1000);
                            }
                        };
                        ws.onclose = function() {
                            // 如果连接断开，尝试重新连接
                            setTimeout(function() {
                                location.reload();
                            }, 2000);
                        };
                    })();
                </script>
            """
        
        @self.sock.route('/ws')
        def ws(sock: WebSocket) -> None:
            self.clients.add(sock)
            try:
                while True:
                    # 保持连接
                    sock.receive()
            finally:
                self.clients.remove(sock)
        
        # 注册Blueprint
        app.register_blueprint(hot_reload_bp)
        
        # 注入热更新脚本
        @app.after_request
        def after_request(response: Response) -> Response:
            if response.content_type and response.content_type.startswith('text/html'):
                response.data = response.get_data(as_text=True).replace('</body>', hot_reload_ws() + '</body>')
            return response
        
        # 启动文件监控
        self._start_file_monitor()

    def _notify_clients(self, action: str = 'reload') -> None:
        """
        通知所有连接的客户端
        :param action: 要执行的动作（'reload' 或 'full-reload'）
        """
        for client in list(self.clients):
            try:
                client.send(action)
            except:
                self.clients.remove(client) 