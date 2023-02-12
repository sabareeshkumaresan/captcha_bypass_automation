import os
import cv2
import pytesseract

# The path to the directory containing the images
image_dir = "images"

# Loop through all the files in the directory
for filename in os.listdir(image_dir):
    # Skip files that are not images
    if not filename.endswith(".jpg") and not filename.endswith(".png"):
        continue
    
    # Load the image file
    image = cv2.imread(os.path.join(image_dir, filename))
    
    # Extract text from the image using pytesseract
    text = pytesseract.image_to_string(image)
    
    # Print the extracted text
    print(f"Text from {filename}:")
    print(text)
