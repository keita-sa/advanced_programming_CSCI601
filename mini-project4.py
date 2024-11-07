import numpy as np
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt
from skimage import io

# Step 1: Load an image into a NumPy array
image = io.imread('input_image.jpg')  # Replace with your image path
print(type(image))                    # Check the type of the image, it should be a NumPy array

# Step 2: Apply a Gaussian blur filter using SciPy
# The standard deviation of the filter determines how blurred the image is (larger values = more blur).
blurred_image = ndimage.gaussian_filter(image, sigma=1)

# Step 3: Save the processed image back to a file
io.imsave('output_image.jpg', blurred_image)

# Step 4: Visualize the original and processed images
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(image)
ax[0].set_title('Original Image')
ax[0].axis('off')

ax[1].imshow(blurred_image)
ax[1].set_title('Blurred Image (Gaussian)')
ax[1].axis('off')

plt.show()
