# -*- coding: utf-8 -*-

# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.
# http://rosalind.info/problems/revc/

print(''.join(["ATCG"["TAGC".index(n)]
               for n in "ATTCAG"[::-1]
              ]
             )
     )
