# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:33:03 2015
http://slendermeans.org/ml4h-ch1-p2.html
@author: joe
"""
import pandas
from fc_python import *
import matplotlib.pyplot as plt
import datetime as dt

inpath='ufo_awesome.tsv'
outpath='ufo6'
#dic=pd.DataFrame({'Patient':[],'Devis total':[],'Nombre d éléments à poser':[],'Séance':pd.DataFrame({'Numeros':[],'Durée':[],'Nombre d éléments':[],'Nombre d éléments mobiles':[],'Soins':[],'Somme':[],'Date':[]},columns=['Numeros','Durée','Nombre d éléments','Nombre d éléments mobiles','Soins','Somme','Date']),columns=['Patient','Nombre d éléments à poser','Devis total','Séance'])

#Crate the data frame
tablufo= pandas.read_table('ufo6', sep = '\\t',
                  na_values = '',  header = None,
                  names = ['date_occurred', 'date_reported',
                           'location', 'short_desc', 'duration',
                           'long_desc'])
print tablufo[0:1]



#Convert dates
tablufo['date_occurred'] = tablufo['date_occurred'].map(ymd_convert)
tablufo['date_reported'] = tablufo['date_reported'].map(ymd_convert)



#Convert locations, if US state add ',US', addy NOPE if not match with and country
tablufo['location']=tablufo['location'].map(location)



#find all unfined countries/location (those preceded by NOPE)
pp=tablufo['location'].map(lambda x:x if len(re.findall('NOPE',x))!=0 else '')
#add the indice of the serie to be able to retrive all the informtions
pp=pp.map(lambda x:[x,pandas.Index(tablufo['location']).get_loc(x)] if x!='' else '' )
for x in pp:
    if len(x)>1:
        print x[0]
#write the description of the "pirate-ufo-event" in a file
uv=open('pirate','w')
uv.write(str(tablufo[40742:40743]['long_desc']))
uv.close()
