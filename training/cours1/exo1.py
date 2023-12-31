#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 21:57:45 2023

@author: patricia
"""

b = ["world", "word", "hello", "", "h"]

for i in b :
    print("Le mot",i, "est renversé",i[::-1])
    
#liste renversé

c = ["patou", "hey", "note"]
for i in c :
    ren = i[::-1]
    print(ren)
