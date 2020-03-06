# Load the trained file from data
trained_file = ____.___()

# Initialize the detector cascade
detector = ____

# Detect faces with scale factor to 1.2 and step ratio to 1
detected = detector.____(img=friends_image,
                                       scale_factor=____,
                                       step_ratio=____,
                                       min_size=(10, 10),
                                       max_size=(200, 200))
# Show the detected faces
show_detected_face(friends_image, detected)
