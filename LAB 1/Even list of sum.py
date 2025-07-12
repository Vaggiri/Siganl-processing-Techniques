# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 09:54:13 2025

@author: CB.EN.U4ECE24016
"""
import numpy as np
n=int(input("Enter the no of list items : "))

def check(n):
    sum=0
    val=np.zeros(n,int)
    for i in range(n):
        
        print("Enter the value of index ",i)
        val[i]=int(input())
        
    for i in range(n):
        if (val[i]%2==0):
            sum=sum+val[i]
    print("\nThe sum of even number in list is :",sum)
    
check(n)