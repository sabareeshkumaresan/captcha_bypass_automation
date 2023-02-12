import cv2
import pytesseract

# Load the image file
image = cv2.imread("sample.jpg")

# Extract text from the image using pytesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
