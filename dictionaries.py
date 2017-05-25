# -*- coding: utf-8 -*-

# Given: A string s of length at most 10000 letters.
# Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
# http://rosalind.info/problems/ini6/

import collections

str = ''
# 将字符串按照空格划分开
str1 = str.split(' ')

for key, value in collections.Counter(str1).items():
  print('%s %s' %(key, value))
