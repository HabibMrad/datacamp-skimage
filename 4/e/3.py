# Import the corner detector related functions and module
from skimage.____ import ____, corner_peaks

# Convert image from RGB-3 to grayscale
building_image_gray = ____

# Apply the detector  to measure the possible corners
measure_image = ____

# Find the peaks of the corners using the Harris detector
coords = ____(____, min_distance=2)

# Show original and resulting image with corners detected
show_image(building_image, "Original")
show_image_with_corners(building_image, coords)
