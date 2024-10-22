#Q1. Using a sobel filter, filter the image and show the original image and then the filter image 

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
import imageio  # Library to read and write image files

# Load an example image
image = imageio.imread('dog.jpg')  # Replace with your image file path

# Apply the Sobel filter on the image
sobel_filtered_image = ndimage.sobel(image)

# Plot the original image
plt.figure(figsize=(6, 6))
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.show()

# Plot the Sobel filtered image
plt.figure(figsize=(6, 6))
plt.imshow(sobel_filtered_image, cmap='gray')
plt.title('Sobel Filtered Image')
plt.axis('off')
plt.show()

