import base64
import cv2
import numpy as np
import os
import pytesseract

# The file containing the base64-encoded image data
file = "/path/to/image.txt"

# Read the base64-encoded image data from the file
with open(file, "r") as f:
    image_data = f.readlines()

# The file to write the extracted text to
output_file = "extracted_text.txt"

with open(output_file, "w") as f:
    for image_str in image_data:
        # Decode the base64-encoded image data
        image_bytes = base64.b64decode(image_str.split(",")[1])

        # Convert the binary image data to a NumPy array
        image = np.frombuffer(image_bytes, dtype=np.uint8)

        # Convert the NumPy array to a OpenCV image
        image = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)

        # Extract text from the image using pytesseract
        text = pytesseract.image_to_string(image)

        # Write the extracted text to the output file
        f.write(text + "\n")
