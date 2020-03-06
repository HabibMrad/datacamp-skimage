# Import the slic function from segmentation module
from skimage.____ import ____

# Import the label2rgb function from color module
from skimage.____ import ____

# Obtain the segmentation with 400 regions
segments = ____(____, ____= ____)

# Put segments on top of original image to compare
segmented_image = ____(____, ____, kind='avg')

# Show the segmented image
show_image(segmented_image, "Segmented image, 400 superpixels")
