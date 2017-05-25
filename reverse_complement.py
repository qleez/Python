# -*- coding: utf-8 -*-

# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.
# http://rosalind.info/problems/revc/

'''
"ATTCAG"[::-1]取"ATTCAG"的反向串"GACTTA"
在"TAGC"中寻找G、A、C、T、T、A出现的位置，2、1、3、0、0、1
找到"ATCG"[2]、"ATCG"[1]、"ATCG"[3]、"ATCG"[0]、"ATCG"[0]、"ATCG"[1]
并把找出的C、T、G、A、A、T几个字母join在一起，构成CTGAAT
'''

print(''.join(["ATCG"["TAGC".index(n)]
               for n in "ATTCAG"[::-1]
              ]
             )
     )
