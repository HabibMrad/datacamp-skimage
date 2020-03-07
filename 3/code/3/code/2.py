# Initialize the mask
mask = ____(____[:-1])

# Set the pixels where the logo is to 1
mask[210:272, 360:425] = ____

# Apply inpainting to remove the logo
image_logo_removed = inpaint.____(____,
                                  ____,
                                  multichannel=True)

# Show the original and logo removed images
show_image(image_with_logo, 'Image with logo')
show_image(image_logo_removed, 'Image with logo removed')
