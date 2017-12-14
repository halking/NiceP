#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/14 15:46
# @Author  : Steven
# @Site    : 
# @File    : MapReduce.py
# @Software: PyCharm Community Edition
from functools import reduce
def nomalFuc(x):
    return  x * x

def redFuc(x, y):
    return  x * y

exp = [x for x in range(1,11)]
temp = map(nomalFuc,exp)

red = reduce(redFuc,exp)

result = list(temp)

print("map : " , result)
print("reduce :", red)