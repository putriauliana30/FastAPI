# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import os

from typing import Optional
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse


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
    
    
if __name__== "__main__":
    uvicorn.run(app,host="0.0.0.0",port=int(os.environ.get('PORT',5000)), log_level="info")
