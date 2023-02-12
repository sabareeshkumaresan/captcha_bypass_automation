import base64
import cv2
import numpy as np
import pytesseract

# The base64-encoded image data
image_data = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEASABIAAD/4QBmRXhpZgAATU0AKgAAAAgA...

# Decode the base64-encoded image data
image_bytes = base64.b64decode(image_data.split(",")[1])

# Convert the binary image data to a NumPy array
image = np.frombuffer(image_bytes, dtype=np.uint8)

# Convert the NumPy array to a OpenCV image
image = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)

# Extract text from the image using pytesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
