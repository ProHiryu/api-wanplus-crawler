#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages
import sys
import os
"""
打包的用的setup必须引入
"""

VERSION = '2.1.3'

setup(
    name='wanplusapi',  # 文件名
    version=VERSION,  # 版本(每次更新上传Pypi需要修改)
    description="a small programm of wanplus crawler",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='python wanplus crawler',  # 关键字
    author='songheqi',  # 用户名
    author_email='songheqi1996@gmail.com',  # 邮箱
    url='https://github.com/ProHiryu/api-wanplus-crawler',  # github上的地址,别的地址也可以
    license='MIT',  # 遵循的协议
    packages=['wanplusapi'],  # 发布的包名
    install_requires = ['requests>=2.13.0'],
    platforms = 'any',
)
