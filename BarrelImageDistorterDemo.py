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

# BarrelImageDistorterDemo.py

# 2024/06/18 to-arai
# The distort method of this BarrenDistort has been take from the following
# code in stackoverflow.com
# https://stackoverflow.com/questions/59776772/python-opencv-how-to-apply-radial-barrel-distortion

import os
import sys
import glob
import shutil

import numpy as np
import cv2 
import math
import traceback

from BarrelImageDistorter import BarrelImageDistorter

class BarrelImageDistorterDemo(BarrelImageDistorter):

  def __init__(self, config_file):
     super().__init__(config_file)     

  def distort_one(self, image_filepath, output_dir):
          
    img = cv2.imread(image_filepath)
    basename = os.path.basename(image_filepath)

    (h, w, _) = img.shape

    # set up the x and y maps as float32
    map_x = np.zeros((h, w), np.float32)
    map_y = np.zeros((h, w), np.float32)

    scale_x = 1
    scale_y = 1
    index = 100
    for center in self.centers:
      index += 1
      print("=== filepath {}  center {}".format(image_filepath, center))
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
      img = cv2.remap(img, map_x, map_y, cv2.INTER_LINEAR)

      # For demonstration, draw a circle of center (cx, cy) with radius 20 with color yellow.
      cx = int(center_x)
      cy = int(center_y)
      cv2.circle(img, (cx, cy), 20, (0, 255, 255), thickness=2, 
                 lineType=cv2.LINE_8, shift=0)

      output_filepath = os.path.join(output_dir, 
                      str(index) + "_" + str(self.radius) + "_" + str(self.amount) + "_" + basename)    
      cv2.imwrite(output_filepath,img)
      print("=== Saved {}".format(output_filepath))
       
if __name__ == "__main__":
  try:
    config_file = "./demo_distortion.config"
    if len(sys.argv) == 2:
      config_file = sys.argv[1]
    distorter = BarrelImageDistorterDemo(config_file)
    distorter.distort()

  except:
    traceback.print_exc()
