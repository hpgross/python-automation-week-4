#! /usr/bin/env python3


import os
import requests

ip_address = ""
server_location = "http://" + ip_address + "/fruits/"
file_list = os.listdir(os.getcwd()+"/supplier-data/descriptions")
current_request = {}

for file in file_list:
    if file[-4:] == ".txt":
        #set up the dictionary for the request
        open_file = open(os.getcwd()+"/supplier-data/descriptions/"+file,"r")
        line_list = open_file.read().splitlines()
        current_request["name"] = line_list[0]
        current_request["weight"] = Int(line_list[1][0:-4])
        current_request["description"] = line_list[2]
        current_request["image_name"] = file[-4:0]+ ".jpeg"
        open_file.close()

        new_post = requests.post(server_location,json=current_request)
        new_post.raise_for_status()
        print(new_post.status_code)