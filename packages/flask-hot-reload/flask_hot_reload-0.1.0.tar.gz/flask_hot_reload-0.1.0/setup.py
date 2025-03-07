from setuptools import setup, find_packages

setup(
    name='flask-hot-reload',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Flask>=2.0.0',
        'flask-sock>=0.4.0',
        'watchdog>=2.1.0',
        'colorama>=0.4.6'
    ],
    author='Blake Zhou',
    author_email='1043744584@qq.com',
    description='A Flask extension that provides real-time hot reload for templates, static files and Python code changes',
    keywords='flask hot reload live reload',
    url='https://github.com/ZhouYu2156/flask-hot-reload',
)