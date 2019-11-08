# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:07:19 2019

@author: jsain
"""
import numpy as np
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
fhout = open('pruebas.txt','w')
fhout.write("ID|TARGET|PRIMOEO")
for i in range(100):
    a=np.random.randint(1000000000)
    p=np.random.randint(25)
    p=prime[p]
    fhout.write(str(i+1)+"|"+str(a)+"|"+str(p)+'\n')
fhout.close()