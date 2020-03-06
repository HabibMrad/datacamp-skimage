# Obtain the segmentation with default 100 regions
segments = ____

# Obtain segmented image using label2rgb
segmented_image = ____(____, ____, kind='avg')

# Detect the faces with multi scale method
detected = detector.____(img=____, 
                                       scale_factor=1.2, 
                                       step_ratio=1, 
                                       min_size=(10, 10), max_size=(1000, 1000))

# Show the detected faces
show_detected_face(segmented_image, detected)
