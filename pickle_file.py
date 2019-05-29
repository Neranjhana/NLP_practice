#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:27:11 2019

@author: developer
"""
    
    
import pickle 
import pandas as pd
contents=open(str('Processed_Input_Data.pkl'),"rb")
dicto =pd.read_pickle(contents)

