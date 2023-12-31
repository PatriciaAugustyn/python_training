#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 17:53:28 2023

@author: patricia
"""
a = input("entrer : ")
b = list(a)
print(b)
print(len(b))

for i in b : 
    print(b, end= " ")

for i, c in enumerate(b):
    print(i,c)
b[2:2]: [5]