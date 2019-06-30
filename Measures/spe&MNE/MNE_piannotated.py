# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:42:15 2019

@author: cy
"""
import re
import linecache
import math
import string
from collections import defaultdict

def fo(file_name):
    fo_dict={}
    file=open(file_name,'r')
    for lines in file.readlines():
        line=lines.rstrip('\n').split('\t')
        if len(line)>1:
            fo_dict[line[0]]=line[1:]
    return fo_dict

A_fo=fo('./CG/A.fo')
B_fo=fo('./CG/B.fo')
C_fo=fo('./CG/C.fo')
D_fo=fo('./CG/D.fo')
E_fo=fo('./CG/E.fo')
F_fo=fo('./CG/F.fo')
G_fo=fo('./CG/G.fo')
H_fo=fo('./CG/H.fo')


f=open('smetana_8CG_28.1s.txt','r')#读取alignment文件
c_num=len(f.readlines())

ne=[]
mne=0
a_clu_num=0
for i in range(0,c_num):
    i_A=[]
    i_B=[]
    i_C=[]
    i_D=[]
    i_E=[]
    i_F=[]
    i_G=[]
    i_H=[]
    flag_annotated=0
    pi_sum=0
    d=0
#    p=[]
    p=defaultdict(list)
    pi2=0
    i_cluster_data=linecache.getline('smetana_8CG_28.1s.txt',i+1)
    i_cluster=i_cluster_data.strip('\n').split(' ')

    

    for i_ in i_cluster:
            
        
        if(i_.startswith('a')==1):
            if (i_ in A_fo.keys()):
                fo=''.join(A_fo.get(i_))
                pi2=pi2+1

                p[fo].append(i_)
        elif(i_.startswith('b')==1):
            if (i_ in B_fo.keys()):
                fo=''.join(B_fo.get(i_))
                pi2=pi2+1

                p[fo].append(i_)
        elif(i_.startswith('c')==1):
            if (i_ in C_fo.keys()):
                fo=''.join(C_fo.get(i_))
                p[fo].append(i_)
                pi2=pi2+1
                
        elif(i_.startswith('d')==1):
            if (i_ in D_fo.keys()):
                fo=''.join(D_fo.get(i_))
                p[fo].append(i_)
                pi2=pi2+1
                
        elif(i_.startswith('e')==1):
            if (i_ in E_fo.keys()):
                fo=''.join(E_fo.get(i_))
                p[fo].append(i_)
                pi2=pi2+1
                
        elif(i_.startswith('f')==1):
            if (i_ in F_fo.keys()):
                fo=''.join(F_fo.get(i_))
                p[fo].append(i_)
                pi2=pi2+1
                
        elif(i_.startswith('g')==1):
            if (i_ in G_fo.keys()):
                fo=''.join(G_fo.get(i_))
                p[fo].append(i_)
                pi2=pi2+1
                
        elif(i_.startswith('h')==1):
            if (i_ in H_fo.keys()):
                fo=''.join(H_fo.get(i_))
                p[fo].append(i_)
                pi2=pi2+1
            
#    print(pi2)
#            

    for p_ in p:
        pp=p.get(p_)
        if(len(pp)<2):
            if(flag_annotated!=1):
                flag_annotated=0
        else:
            flag_annotated=1
    if (flag_annotated==0):
        continue
    else:
        a_clu_num=a_clu_num+1

    for p_ in p:
        pp=p.get(p_)
#        print(pp)          
        if (pp!=''): 
            pi1=len(pp)
#            print(pi1)
            pi=pi1/pi2
            pi_=pi*math.log(pi)
            pi_sum=pi_sum+pi_
      
           
    
    d=len(p)
 
    if(d>0):
        if(d==1):
            ne_value=0
            ne.append(ne_value)
        else:
            ne_value=-pi_sum/math.log(d)
            ne.append(ne_value)


for ne_ in ne:
#    print(ne_)
    mne=mne+ne_
#    print (mne)
#print(mne)
#print(ne)
mne_value=mne/a_clu_num
print(mne_value)
f.close()
    
    

