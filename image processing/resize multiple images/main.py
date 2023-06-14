# Author: Zarbio Romulo

import cv2
import os

def calculate_size(scale_percentage, width, height):
  new_width = int(width * scale_percentage / 100)
  new_height = int(height * scale_percentage / 100)
  print("New Dim:", new_width, new_height)
  return (new_width, new_height)

def resize(image_path, scale_percentage, resized_path):
  image = cv2.imread(image_path)
  new_dim = calculate_size(scale_percentage, image.shape[1], image.shape[0])
  resized_image = cv2.resize(image, new_dim)
  cv2.imwrite(resized_path, resized_image)

images = os.listdir('images')
for image in images:
  resize(f'images/{image}', 10, f'resized/resized-{image}')