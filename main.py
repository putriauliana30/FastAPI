# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# import nessecary library
import pandas as pd
import numpy as np
import os
import json

from typing import Optional
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

# The data used in this assignment is the death data for the population of DKI Jakarta province based on gender in 2017
app = FastAPI()

@app.get('/tugasputri')

def assignment_putri():
    data = pd.read_csv('data-kematian-penduduk-berdasarkan-jenis-kelamin-per-kecamatan-tahun-2017.csv', sep=';')
    mydata = data.groupby(['nama_kabupaten','nama_kecamatan','jenis_kelamin'])[['jumlah']].sum().reset_index()
    mydata['Rank'] = mydata['jumlah'].rank(method='dense', ascending=False)
    mydata = mydata.sort_values('Rank').head(10).reset_index(drop=True)
    mydata_dict = mydata.to_dict(orient="index")
    result = mydata_dict
    return result
    
    
# In this case, it can be seen that the order of the number of deaths in the province of Jakarta is based on the name of the district, the name of the province and the gender in 2017
# Displayed in 10 order from highest to lowest number of deaths
