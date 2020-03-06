# Import the otsu threshold function
from skimage.____ import ____

# Make the image grayscale using rgb2gray
chess_pieces_image_gray = ____(____)

# Obtain the optimal threshold value with otsu
thresh = ____(____)

# Apply thresholding to the image
binary = chess_pieces_image_gray ____ ____

# Show the image
show_image(binary, 'Binary image')
