# Import the necessary modules
from skimage import data, ____

# Load the image
original_image = ____.coffee()

# Apply the adaptive equalization on the original image
adapthist_eq_image = ____.____(original_image, ____=____)

# Compare the original image to the equalized
show_image(original_image)
show_image(adapthist_eq_image, '#ImageProcessingDatacamp')
