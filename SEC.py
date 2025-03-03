#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 08:49:33 2025

@author: Alexander.Morano
"""

import os 
import pandas as pd
import matplotlib.pyplot as plt
import numpy


def SEC_Filtering(path_to_csv):
    
    splitpath = path_to_csv.split('/')
    directory = '/'.join(splitpath[:-1])
    
    #os.chdir("/Users/Alexander.Morano/Desktop/")
    FT_CSV = pd.read_csv(path_to_csv)

    def PF_binary(result):
        return result.split(' ')[0]
    
    FT_CSV['PF_Binary'] = FT_CSV["SEC_pass_fail"].apply(PF_binary)
    FT_CSV_Modified = FT_CSV.fillna("No Aggregation")

#you can add any condition you want here. In this situation, I've selected those that pass and those that fail. 
#but if you want to filter based on retention time, peak height, etc, you can add it here. 

    passers = FT_CSV_Modified["PF_Binary"] == "pass"
    fails = FT_CSV_Modified["PF_Binary"] == "fail"


    FT_Pass = FT_CSV_Modified[passers]
    print(f"Number of pass records: {len(FT_Pass)}")
    
    FT_Fail = FT_CSV_Modified[fails]
    print(f"Number of fail records: {len(FT_Fail)}")

    FT_Pass.to_csv(os.path.join(directory, r'FT_Pass.csv'))
    
    FT_Fail.to_csv(os.path.join(directory, r'FT_Fail.csv'))
    
    return "Pass And Fail Saved!"