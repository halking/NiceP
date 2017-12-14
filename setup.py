#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/13 16:29
# @Author  : Steven
# @Site    : 
# @File    : setup.py
# @Software: PyCharm Community Edition

from setuptools import setup,find_packages
import os

PACKAGE = {
            '': ['*.txt', '*.xlsx'],
            '': ['*.py'],
           }
setup(
    name="NiceP",
    version="0.1",
    author='halking Steven',
    author_email='halking@qq.com',
    description='An Advanced Django CMS',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/halking/NiceP',
    license='BSD License',
    platforms=['win10 gitHub'],
    include_package_data=True,
    packages=find_packages(exclude=['project', 'project.*']),
    zip_safe=False,
    package_data = PACKAGE,
    test_suite='runtests.main'

)