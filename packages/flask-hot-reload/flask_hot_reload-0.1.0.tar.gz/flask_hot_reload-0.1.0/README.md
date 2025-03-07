# Flask Hot Reload

[English](#english) | [中文](#chinese)

<h2 id="english">English</h2>

A Flask extension that automatically refreshes your browser when you make changes to your templates, static files, or Python code.

## Installation

```bash
pip install flask-hot-reload
```

## Quick Start

```python
from flask import Flask, render_template
from flask_hot_reload import HotReload

app = Flask(__name__)

# Initialize hot reload with custom watch directories
hot_reload = HotReload(app, 
    includes=[
        'templates',  # template directory
        'static',     # static files directory
        '.'          # current directory
    ],
    excludes=[
        '__pycache__',
        'node_modules',
        '.git'
    ]
)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

## Features

- 🔄 Real-time browser refresh on file changes
- 📁 Monitor multiple directories
- 🚫 Exclude unwanted directories
- 🐍 Support for Python file hot reload
- 📝 Template file hot reload
- 🎨 Static file hot reload
- 🔌 WebSocket-based, low latency
- 🎯 Zero configuration needed

## Configuration

### Watch Directories

By default, Flask Hot Reload watches the `templates` and `static` directories. You can customize the watched directories:

```python
hot_reload = HotReload(app, 
    includes=[
        'templates',
        'static',
        'src',
        'routes'
    ]
)
```

### Exclude Directories

Exclude directories that don't need monitoring:

```python
hot_reload = HotReload(app,
    excludes=[
        '__pycache__',
        'node_modules',
        '.git',
        'venv'
    ]
)
```

## Requirements

- Python 3.7+
- Flask 2.0.0+
- Watchdog 2.1.0+
- Flask-Sock 0.4.0+
- Colorama 0.4.6+

---

<h2 id="chinese">中文文档</h2>

一个Flask扩展插件，当你修改模板、静态文件或Python代码时，浏览器会自动刷新。

## 安装

```bash
pip install flask-hot-reload
```

## 快速开始

```python
from flask import Flask, render_template
from flask_hot_reload import HotReload

app = Flask(__name__)

# 使用自定义监控目录初始化热重载
hot_reload = HotReload(app, 
    includes=[
        'templates',  # 模板目录
        'static',     # 静态文件目录
        '.'          # 当前目录
    ],
    excludes=[
        '__pycache__',  # 排除Python缓存目录
        'node_modules', # 排除npm模块目录
        '.git'         # 排除git目录
    ]
)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

## 特性

- 🔄 文件变更时实时刷新浏览器
- 📁 支持监控多个目录
- 🚫 可排除不需要监控的目录
- 🐍 支持Python文件热重载
- 📝 支持模板文件热重载
- 🎨 支持静态文件热重载
- 🔌 基于WebSocket，低延迟
- 🎯 零配置即可使用

## 配置

### 监控目录

默认情况下，Flask Hot Reload 会监控 `templates` 和 `static` 目录。你可以自定义监控目录：

```python
hot_reload = HotReload(app, 
    includes=[
        'templates',
        'static',
        'src',
        'routes'
    ]
)
```

### 排除目录

排除不需要监控的目录：

```python
hot_reload = HotReload(app,
    excludes=[
        '__pycache__',
        'node_modules',
        '.git',
        'venv'
    ]
)
```

## 环境要求

- Python 3.7+
- Flask 2.0.0+
- Watchdog 2.1.0+
- Flask-Sock 0.4.0+
- Colorama 0.4.6+

## 许可证

MIT License

## 作者

Blake Zhou (1043744584@qq.com)

## 链接

- [GitHub 仓库](https://github.com/ZhouYu2156/flask-hot-reload)
- [问题反馈](https://github.com/ZhouYu2156/flask-hot-reload/issues)