#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 23:07:16 2023

@author: patricia
"""


def renverse(mot):
    mot_renverse=""
    for i in range(len(mot)-1,-1,-1):
        mot_renverse += mot[i]
    return mot_renverse 

print(renverse("Iris"))

#mot = "Iris"
#for i in range(len(mot)-1,-1,-1):
    #renverse = mot[i]
   # print(renverse, end=" ")