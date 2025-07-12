# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 10:13:15 2025

@author: CB.EN.U4ECE24016
"""

char=input("Enter a string to check for pallindrome : ")
new=char[::-1]

if char==new:
    print("\n\nThe String",char,"is Pallindrome\n\n")
else:
    print("\n\nThe String",char,"is not a Pallindrome\n\n")