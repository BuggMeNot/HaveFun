# -*- coding: utf-8 -*-
import pandas as pd

path = 'C:\Users\adminuser\Desktop\Learning'

def groups(col,score):
    path = 'C:\Users/adminuser\Desktop\Learning'
    inputfile = path + '/' + '711.xls'
    
    df = pd.read_excel(inputfile)
    print(df.head(2))
    
    df_r = [df[col]>score]
    print(len(df_r))
    
