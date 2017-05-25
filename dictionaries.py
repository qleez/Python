#coding=utf-8

import collections
import os

with open('str.txt') as file1:#打开文本文件
    str1=file1.read().split(' ')#将文章按照空格划分开 

print "原文本:\n %s"% str1
print "\n各单词出现的次数：\n %s" % collections.Counter(str1)
