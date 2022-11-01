#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: Binux<roy@binux.me>
#         http://binux.me
# Created on 2014-11-24 22:27:45


import sys
from setuptools import setup, find_packages
from codecs import open
from os import path
from site import getsitepackages

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

import pyspider

install_requires = [
    'Flask==2.2.2',
    'Jinja2==3.1.2',
    'chardet==5.0.0',
    'cssselect==1.2.0',
    # "lxml==4.9.0", # 手动安装
    # 'pycurl==7.45.1', # 手动安装
    'requests==2.28.1',
    'Flask-Login==0.6.2',
    'u-msgpack-python==2.7.1',
    'click==8.1.3',
    'six==1.16.0',
    'tblib==1.7.0',
    'wsgidav==4.0.2',
    'tornado>=3.2,<=4.5.3',
    'pyquery',
]

extras_require_all = [
    'mysql-connector-python==8.0.16',
    'pymongo==3.9.0',
    'redis==2.10.6',
    'redis-py-cluster==1.3.6',
    'psycopg2==2.8.2',
    'elasticsearch==2.3.0',
    'kombu==4.4.0',
    'amqp==2.4.0',
    'SQLAlchemy==1.3.10',
    'pika==1.1.0'
]

setup(
    name='pyspider',
    version=pyspider.__version__,

    description='A Powerful Spider System in Python',
    long_description=long_description,

    url='https://github.com/binux/pyspider',

    author='Roy Binux',
    author_email='roy@binux.me',

    license='Apache License, Version 2.0',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

        'License :: OSI Approved :: Apache Software License',

        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',

        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    keywords='scrapy crawler spider webui',

    packages=find_packages(exclude=['data', 'tests*']),

    install_requires=install_requires,

    extras_require={
        'all': extras_require_all,
        'test': [
            'coverage',
            'Werkzeug==2.2.2',
            'httpbin==0.7.0',
            'pyproxy==0.1.6',
            'easywebdav==1.2.0',
        ]
    },

    package_data={
        'pyspider': [
            'logging.conf',
            'fetcher/phantomjs_fetcher.js',
            'fetcher/splash_fetcher.lua',
            'webui/static/*.js',
            'webui/static/*.css',
            'webui/templates/*'
        ],
    },

    entry_points={
        'console_scripts': [
            'pyspider=pyspider.run:main'
        ]
    },

    test_suite='tests.all_suite',
)

packages = getsitepackages()
site_path =[item for item in packages if item.find('site-packages')> 0][0]
print(site_path)
tornado_path = path.join(site_path, 'tornado', 'httputil.py')
if path.exists(tornado_path):
    content = None
    with open(tornado_path, 'r', encoding='utf-8-sig') as source_file:
        content = source_file.read()
        print("执行替换")
        content = content.replace('collections.MutableMapping', 'collections.abc.MutableMapping')

    if content:
        print("开始执行")
        with open(tornado_path, 'w', encoding='utf-8-sig') as source_file:
            source_file.write(content)
            print("执行成功")