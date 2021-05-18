#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
data_loc = os.getcwd()+"/supplier-data/images"
file_list = os.listdir(data_loc)

for file in file_list:
    if file[-5:] == ".jpeg":
        with open(data_loc+'/'+file, 'rb') as opened:
            r = requests.post(url, files={'file': opened})