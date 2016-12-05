# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 21:44:31 2015

@author: joe
"""
import numpy as np
import datetime as dt
import re
def ufo(inpat,outpat):
    inf = open(inpat, 'r')
    outf = open(outpat, 'w')
    
    for  line in inf.readlines():
        splitline= line.split('\t')
        if len(splitline)<6:
            continue
        
        newline='\t'.join(splitline[ :6])
        if newline[-1: ] != '\n':
            newline+='\n'
        outf.write(newline)
    inf.close()
    outf.close()
            
            

#Extraire le dictionnaire etat:code
def extractt():
    pa=open('etat.txt','r').read()
    liste_pays = pa.split('\n')
    dic={}
    for ligne in liste_pays:
        try:
            dic[ligne.split('\t')[0]]= ligne.split('\t')[1]
        except:
            pass
    return dic



#Création du dictionnaire pays:code
def extract():
    pa=open('pays3.txt').read()
    pa=re.split(r'\n',pa)
    liste_pays={}
    liste_pays['UK']='UK'
    for ligne in pa:
        try:
            liste_pays[ligne.split('\t')[0].strip(' ')]=ligne.split('\t')[1].strip(' ')
        except:
            pass
    return liste_pays            
            
            
            
         
         #convertir les dates au bon format
def ymd_convert(x):
    try:
        cnv_dt = dt.datetime.strptime(str(x),'%Y%m%d').date()
    except ValueError:
        cnv_dt=np.nan
        
    return cnv_dt
    
def ymd_convert2(x):
    try:
        cnv_dt = dt.datetime.strptime(str(x),'%Y-%m-%d')
    except ValueError:
        cnv_dt=np.nan
        
    return cnv_dt  
    
    
def location(x):
    liste_pays=extract()
    liste_state=extractt()
    
    y='NOPE '+x
    if len(x.split(','))==2:
        y=x+' US'
        return y
    else:
        for etat,code in liste_state.items():
            t=re.findall(etat,x)
            if len(t)!=0:
                x=re.sub(etat,'',x)
                y=x+' '+code+' '+'US'
                return y
                break
            t=re.findall(code,x)
            if len(t)!=0:
                x=re.sub(code,'',x)
                y=x+' '+code+' '+'US'
                return y
                break
            
        for pays,code in liste_pays.items():
            t=re.findall(pays,x)
            if len(t)!=0:
                x=re.sub(pays,'',x)
                y=x+' '+pays
                return y
                break
            t=re.findall(code,x)
            if len(t)!=0:
                x=re.sub(code,'',x)
                y=x+' '+code
                return y
                break
    return y