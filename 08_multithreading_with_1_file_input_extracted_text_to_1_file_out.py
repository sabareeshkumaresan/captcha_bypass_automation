import base64
import cv2
import numpy as np
import os
import pytesseract
import threading

# The file containing the base64-encoded image data
file = "/path/to/image.txt"

# Read the base64-encoded image data from the file
with open(file, "r") as f:
    image_data = f.readlines()

# The file to write the extracted text to
output_file = "extracted_text.txt"

# A lock to ensure that multiple threads don't write to the output file simultaneously
file_lock = threading.Lock()

def extract_text(image_str):
    # Decode the base64-encoded image data
    image_bytes = base64.b64decode(image_str.split(",")[1])

    # Convert the binary image data to a NumPy array
    image = np.frombuffer(image_bytes, dtype=np.uint8)

    # Convert the NumPy array to a OpenCV image
    image = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)

    # Extract text from the image using pytesseract
    text = pytesseract.image_to_string(image)

    # Write the extracted text to the output file
    with file_lock:
        with open(output_file, "a") as f:
            f.write(text + "\n")

# Create a list of threads
threads = []

# Start a thread for each image
for image_str in image_data:
    t = threading.Thread(target=extract_text, args=(image_str,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()
