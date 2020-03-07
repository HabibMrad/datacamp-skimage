# Import the module and function
from skimage.___ import ____

# Set proportional height so its half its size
height = int(____ / 2)
width = int(____ / 2)

# Resize using the calculated proportional height and width
image_resized = ____(dogs_banner, (____, ____),
                       anti_aliasing=True)

# Show the original and rotated image
show_image(dogs_banner, 'Original')
show_image(image_resized, 'Resized image')
