#!/usr/bin/env python3

import os
from PIL import Image

# This file will iterate over a series of images
# scaling them down, rotating them by 90 degrees
# and then converting them to a different format

src_dir = os.getcwd() + "/supplier-data/images" #The file path for the source directory
prt_dir = src_dir #The file path for the output directory

if not os.path.exists(prt_dir):
    os.makedirs(prt_dir)

for filename in os.listdir(src_dir):
    src_path = src_dir + "/" + filename
    if src_path[-5:] == ".tiff":
        prt_path = prt_dir + "/" + filename[0:-5] + ".jpeg"
        im = Image.open(src_path)
        im = im.convert("RGB")
        im = im.resize((600,400))
        im.save(prt_path,"JPEG")
        im.close()