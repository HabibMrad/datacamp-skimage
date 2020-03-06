# Detect the faces
detected = ____.____(img=____, 
                                       scale_factor=1.2, step_ratio=1, 
                                       min_size=____, max_size=(100, 100))
# For each detected face
for d in ____:  
    # Obtain the face rectangle from detected coordinates
    face = getFaceRectangle(d)
    
    # Apply gaussian filter to extracted face
    blurred_face = ____(face, multichannel=____, sigma = ____)
    
    # Merge this blurry face to our final image and show it
    resulting_image = mergeBlurryFace(group_image, blurred_face) 
show_image(resulting_image, "Blurred faces")
