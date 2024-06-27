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

# ImageMaskAugmentor.py
# 2024/06/21 Updated 
# The distort method of this class has been taken from the stackoverfflow.com web-site:
# https://stackoverflow.com/questions/59776772/python-opencv-how-to-apply-radial-barrel-distortion

import os
import sys
import glob
import shutil
import math
import cmath
import numpy as np

import cv2
import traceback

from ConfigParser import ConfigParser

class ImageMaskAugmentor:

  def __init__(self, config_file):
     self.config     = ConfigParser(config_file)
     self.config.dump_all()

     self.images_dir = self.config.get("augmentor",  "images_dir")
     self.masks_dir  = self.config.get("augmentor",  "masks_dir")
     self.output_dir = self.config.get("augmentor",  "output_dir") 
      
     self.centers    = self.config.get("augmentor",  "centers")
     # self.amounts take a list of amount something like [0.3, -0.3]
     # the positive value will generate a barrel distortion, and negative a pincushion. 
     self.amounts    = self.config.get("augmentor",  "amounts", dvalue=[0.3, -0.3])                                                                      
     self.radii      = self.config.get("augmentor",  "radii",   dvalue=[0.3, 0.5])

     if os.path.exists(self.output_dir):
       shutil.rmtree(self.output_dir)
     if not os.path.exists(self.output_dir):
       os.makedirs(self.output_dir)
     self.output_images_dir = os.path.join(self.output_dir, "images")
     self.output_masks_dir  = os.path.join(self.output_dir,  "masks")

     os.makedirs(self.output_images_dir)
     os.makedirs(self.output_masks_dir)
     
  def augment(self):
     image_files  = glob.glob(self.images_dir + "/*.jpg")
     image_files += glob.glob(self.images_dir + "/*.png")
     image_files += glob.glob(self.images_dir + "/*.bmp")
     image_files += glob.glob(self.images_dir + "/*.tif")
     image_files  = sorted(image_files)

     mask_files   = glob.glob(self.masks_dir + "/*.jpg")
     mask_files  += glob.glob(self.masks_dir + "/*.png")
     mask_files  += glob.glob(self.masks_dir + "/*.bmp")
     mask_files  += glob.glob(self.masks_dir + "/*.tif")
     mask_files   = sorted(mask_files)
     num_image_files = len(image_files)
     num_mask_files  = len(mask_files)

     if num_image_files != num_mask_files:
       raise Exception("Unmatched number of image and mask files")
     for i in range(num_image_files):
        image_file = image_files[i]
        mask_file  = mask_files[i]
        self.distort(image_file, mask_file)

  def distort(self, image_file, mask_file):
    print("=== distort {} {}".format(image_file, mask_file))
    image = cv2.imread(image_file)
    mask  = cv2.imread(mask_file)
    
    image_basename = os.path.basename(image_file)
    mask_basename  = os.path.basename(mask_file)
    for radius in self.radii:
      for amount in self.amounts:
        cimage = image.copy()
        cmask  = mask.copy()

        self.distort_one(cimage, cmask, radius, amount, image_basename, mask_basename)

  def distort_one(self, cimage, cmask, radius, amount, image_basename, mask_basename):

    (h,  w,  _) = cimage.shape
    (hm, wm, _) = cmask.shape
    if h != hm or w != wm:
      raise Exception("Unmatched shape of image, mask")
 
    # set up the x and y maps as float32
    #map_x = np.zeros((h, w), np.float32)
    #map_y = np.zeros((h, w), np.float32)

    scale_x = 1
    scale_y = 1
    index   = 100
    
    for center in self.centers:
      image = cimage.copy()
      mask  = cmask.copy()
      # set up the x and y maps as float32
      map_x = np.zeros((h, w), np.float32)
      map_y = np.zeros((h, w), np.float32)

      index += 1
      (ox, oy) = center
      center_x = w * ox
      center_y = h * oy
      radius = w * radius  
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
                v = math.sqrt(distance)
                factor = math.pow(math.sin(math.pi * math.sqrt(distance) / radius / 2), amount)
            map_x[y, x] = factor * delta_x / scale_x + center_x
            map_y[y, x] = factor * delta_y / scale_y + center_y
            

      # do the remap
      image = cv2.remap(image, map_x, map_y, cv2.INTER_LINEAR)
      mask  = cv2.remap(mask, map_x, map_y,  cv2.INTER_LINEAR)
      
      output_image_filepath = os.path.join(self.output_images_dir, 
                      "barrdistorted_"+str(index) + "_" + str(radius) 
                      + "_" + str(amount) + "_" + image_basename)    
      cv2.imwrite(output_image_filepath, image)
      print("=== Saved {}".format(output_image_filepath))

      output_mask_filepath = os.path.join(self.output_masks_dir, 
                      "barrdistorted_"+str(index) + "_" + str(radius) 
                      + "_" + str(amount) + "_" + mask_basename)    
      cv2.imwrite(output_mask_filepath, mask)
      print("=== Saved {}".format(output_mask_filepath))
       

if __name__ == "__main__":
  try:
    config_file = "augmentor.config"
    if len(sys.argv) == 2:
      config_file = sys.argv[1]

    augmentor = ImageMaskAugmentor(config_file)
    augmentor.augment()

  except:
    traceback.print_exc()


  