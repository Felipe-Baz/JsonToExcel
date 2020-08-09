#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:10:30 2020

@author: felipe
"""

import json
import pandas as pd
import numpy as np


def excel():
    dict1 = {'1':[], # 1 linha 
             '2':[], # 2 linha
             '3':[], # 3 linha
             '4':[], # 4 linha
             '5':[], # 5 linha
             '6':[], # 6 linha
             '7':[], # 7 linha
             '8':[], # 8 linha
             '9':[], # 9 linha
             '10':[], # 10 linha
             '11':[], # 1 linha 
             '12':[], # 2 linha
             '13':[], # 3 linha
             '14':[], # 4 linha
             '15':[], # 5 linha
             '16':[], # 6 linha
             '17':[], # 7 linha
             '18':[], # 8 linha
             '19':[], # 9 linha
             '20':[], # 10 linha
             '21':[], # 1 linha 
             '22':[], # 2 linha
             '23':[], # 3 linha
             '24':[], # 4 linha
             '25':[], # 5 linha
             '26':[], # 6 linha
             '27':[], # 7 linha
             '28':[], # 8 linha
             '29':[], # 9 linha
             '30':[]} # 10 linha
    
    for i in range(1, 31):
        with open(f'result/result{i-1}.json') as fp:
            data = json.load(fp)
        for j in range(0,7):
            dict1[f'{i}'].append(data['acc'][j])
        for j in range(0,7):
            dict1[f'{i}'].append(data['f1'][j])
        for j in range(0,7):
            dict1[f'{i}'].append(data['recall'][j])
        for j in range(0,7):
            dict1[f'{i}'].append(data['prec'][j])     
    df = pd.DataFrame.from_dict(dict1, orient='index')
    df.to_excel("output.xlsx")
    
if __name__ == "__main__":
    data = excel()
    
    