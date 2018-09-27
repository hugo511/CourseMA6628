# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:47:02 2018

@author: Hugo Xian
"""
import math
import numpy as np
        
"""

"""

def judge_pri(N):
    st=math.floor(math.sqrt(N))
    i=1
    while i<=st:
        if N%i == 0 and i!=1:
            #print('%d不是素数'%N)
            return False
            break
        else:
            i+=1
    return True
def find_twpri(data):
    j=0
    twlist=[]
    while j in range(len(data)):
        if data[j] == True and data[j+2] == True:
            twlist.append((j+1,j+3))
            j+=1
        else: 
            j+=1
    return (twlist)    
print(judge_pri(3))   
result=np.zeros(1000000,dtype=np.bool,order='c')
for i in range(len(result)):
    if judge_pri(i+1):
        result[i]=True
li=find_twpri(result)
