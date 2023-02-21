#!/usr/bin/env python3

from PIL import Image
import os

directory = "images/"
new_dir_path = '/opt/icons/'

for filename in os.listdir(directory):
  f=os.path.join(directory, filename)
  if filename != ".DS_Store":
    im = Image.open(f)
    im = im.rotate(-90).resize((128,128)).convert("RGB")
    im.save(new_dir_path+filename+".jpeg")
