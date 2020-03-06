# Create list with the shape of each contour
shape_contours = [cnt.shape[0] for cnt in ____]

# Set 50 as the maximum size of the dots shape
max_dots_shape = ____

# Count dots in contours excluding bigger than dots size
dots_contours = [cnt for cnt in contours if np.shape(cnt)[0] < ____]

# Shows all contours found 
show_image_contour(binary, contours)

# Print the dice's number
print("Dice's dots number: {}. ".format(len(____)))
