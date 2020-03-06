# Load the trained file from data
trained_file = ____.lbp_frontal_face_cascade_filename()

# Initialize the detector cascade
detector = ____(____)

# Detect faces with min and max size of searching window
detected = detector.detect_multi_scale(img = night_image,
                                       scale_factor=1.2,
                                       step_ratio=1,
                                       min_size=(____),
                                       max_size=(____))

# Show the detected faces
show_detected_face(night_image, detected)