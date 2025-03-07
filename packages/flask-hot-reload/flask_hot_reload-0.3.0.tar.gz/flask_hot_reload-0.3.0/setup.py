from setuptools import setup, find_packages

# 读取README.md作为长描述
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='flask-hot-reload',
    version='0.3.0',
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
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='flask hot reload live reload development tools web hmr',
    url='https://github.com/ZhouYu2156/flask-hot-reload',
    project_urls={
        'Documentation': 'https://github.com/ZhouYu2156/flask-hot-reload#readme',
        'Bug Reports': 'https://github.com/ZhouYu2156/flask-hot-reload/issues',
        'Source Code': 'https://github.com/ZhouYu2156/flask-hot-reload',
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Build Tools',
    ],
    python_requires='>=3.7',
)