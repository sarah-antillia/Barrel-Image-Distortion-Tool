# Copyright 2024 antillia.com Toshiyuki Arai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# BarrelImageDistorter.py

# https://stackoverflow.com/questions/59776772/python-opencv-how-to-apply-radial-barrel-distortion

import os
import sys
import glob
import shutil

import numpy as np
import cv2 as cv
import math
import traceback
from ConfigParser import ConfigParser

class BarrelImageDistorter:

  def __init__(self, config_file):
     self.config = ConfigParser(config_file)

     self.radius     = self.config.get(ConfigParser.BARRDISTORTION, "radius", dvalue=0.3)
     self.amount     = self.config.get(ConfigParser.BARRDISTORTION, "amount", dvalue=0.3)
     self.centers    = self.config.get(ConfigParser.BARRDISTORTION, "centers", dvalue= [(0.5, 0.5),])
     self.images_dir = self.config.get(ConfigParser.BARRDISTORTION, "images_dir", dvalue="./images")
     self.output_dir = self.config.get(ConfigParser.BARRDISTORTION, "output_dir", dvalue="./distorted_images")


  def distort(self):
     image_files  = glob.glob(self.images_dir + "/*.jpg")
     image_files += glob.glob(self.images_dir + "/*.png")
     image_files += glob.glob(self.images_dir + "/*.bmp")
     image_files += glob.glob(self.images_dir + "/*.tif")
     image_files  = sorted(image_files)

     if os.path.exists(self.output_dir):
        shutil.rmtree(self.output_dir)
     if not os.path.exists(self.output_dir):
        os.makedirs(self.output_dir)
     print("=== image_file {}".format(image_files))
     
     for image_file in image_files:
       self.distort_one(image_file, self.output_dir)


  def distort_one(self, image_filepath, output_dir):
          
    img = cv.imread(image_filepath)
    basename = os.path.basename(image_filepath)

    (h, w, _) = img.shape

    # set up the x and y maps as float32
    map_x = np.zeros((h, w), np.float32)
    map_y = np.zeros((h, w), np.float32)

    scale_x = 1
    scale_y = 1
    index   = 100
    for center in self.centers:
      print("=== filepath {}  center {}".format(image_filepath, center))
      index += 1
      (ox, oy) = center
      center_x = w * ox
      center_y = h * oy
      radius = w * self.radius
      amount = self.amount   
      # negative values produce pincushion
 
      # create map with the barrel pincushion distortion formula
      for y in range(h):
        delta_y = scale_y * (y - center_y)
        for x in range(w):
          # determine if pixel is within an ellipse
          delta_x = scale_x * (x - center_x)
          distance = delta_x * delta_x + delta_y * delta_y
          if distance >= (radius * radius):
            map_x[y, x] = x
            map_y[y, x] = y
          else:
            factor = 1.0
            if distance > 0.0:
                factor = math.pow(math.sin(math.pi * math.sqrt(distance) / radius / 2), amount)
            map_x[y, x] = factor * delta_x / scale_x + center_x
            map_y[y, x] = factor * delta_y / scale_y + center_y
            

       # do the remap
      img = cv.remap(img, map_x, map_y, cv.INTER_LINEAR)

      output_filepath = os.path.join(output_dir, 
                      "barrdistorted_"+str(index) + "_" + str(self.radius) + "_" + str(self.amount) + "_" + basename)    
      cv.imwrite(output_filepath,img)
      print("=== Saved {}".format(output_filepath))
       


if __name__ == "__main__":
  try:
    config_file = "./distortion.config"
    if len(sys.argv) == 2:
      config_file = sys.argv[1]
    distorter = BarrelImageDistorter(config_file)

    distorter.distort()

  except:
    traceback.print_exc()
