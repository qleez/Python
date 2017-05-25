#coding=utf-8

import collections

str = ''
str1 = str.split(' ')  #将字符串按照空格划分开

for key, value in collections.Counter(str1).items():
    print(key + ' ' + value)
