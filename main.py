def extract_text_from_image(image_path):
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Use pytesseract to do OCR on the image
            text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Replace 'path/to/your/image.jpg' with your image file path
    image_path = input("Enter the path to your image file: ")
    result = extract_text_from_image(image_path)
    print("Extracted Text:\n")
    print(result)