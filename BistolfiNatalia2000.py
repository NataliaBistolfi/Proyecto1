# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 14:38:05 2024

@author: PC
"""

import re
file = open ("C:\\Users\\PC\\Documents\\data\\baby2000.html")

pattern='year'
pattern1= '\d{4,}'
pattern2= '<tr align="right"><td>'
pattern3= '\d{1,}'
pattern4= '[A-Z][a-z]*'
pattern5= '</td><td>'

mi_diccionario = {}
mi_lista= []

for line in file:
    result = re.findall(pattern, line)
    if result:
        result = re.findall(pattern1, line)
        if result:
            print(result)
            
    result= re.findall(pattern2, line)
    if result:
        resultRank= re.findall(pattern3, line)
        
        result= re.findall(pattern4, line)
        if result:
            mi_diccionario[str(resultRank)]=result
            print(result)
            
print(mi_diccionario)   
#Ranking         

for line in file:
    result= re.findall(pattern5, line)
    if result:
        result= re.search(pattern4, line)
        nuevos_datos= {resultRank: result}
        print(result)
        
        mi_lista.append(result.group(0))
mi_lista.sort()
        
mi_lista2= []
for line in file:
    result= re.findall(pattern, line)
    if result:
        print(result)
        result= re.search(pattern1, line)
        if result:
            print(result.group(0))
            mi_lista2.append(result.group(0))
        result= re.search(pattern2, line)
        if result:
            print(result.group(0))
            resultRank= re.search(pattern3, line)
            print(resultRank.group(0))
            mi_lista.append(result.group(0))
            result= re.search(pattern4, line)
            print(re.split('s', result))
            
#mi_lista2.append((anio, resultRank.group(0),result.group(0)))

print(mi_lista2.sort(key=lambda x: x[2], reverse= False))
print(mi_lista2)