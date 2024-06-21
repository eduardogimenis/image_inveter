from PIL import Image, ImageOps, ImageEnhance
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

# Function to process the image
def process_image(image_path):
    try:
        # Open the image file
        image = Image.open(image_path).convert("RGB")  # Ensure image is in RGB mode

        # Convert image to grayscale
        gray_image = ImageOps.grayscale(image)

        # Invert the grayscale image
        inverted_image = ImageOps.invert(gray_image)

        # Enhance contrast to make text and lines more visible
        contrast_enhancer = ImageEnhance.Contrast(inverted_image)
        enhanced_image = contrast_enhancer.enhance(1.5)  # Reduce contrast to avoid too much brightness

        # Enhance brightness to make text and lines stand out
        brightness_enhancer = ImageEnhance.Brightness(enhanced_image)
        final_image = brightness_enhancer.enhance(1.2)  # Reduce brightness to make it less harsh

        # Convert the enhanced inverted image back to RGB
        final_image = final_image.convert("RGB")

        # Get the directory and file name from the original path
        directory, original_file_name = os.path.split(image_path)
        
        # Create the new file name by prepending "inverted_"
        new_file_name = f"inverted_{original_file_name}"
        output_path = os.path.join(directory, new_file_name)

        # Save the processed image
        final_image.save(output_path)

        print(f"Processed image saved at: {output_path}")
    except Exception as e:
        print(f"Error processing image: {e}")

# Main function to open file dialog and process the image
def main():
    # Hide the main Tkinter window
    root = Tk()
    root.withdraw()

    # Open file dialog
    image_path = askopenfilename(
        title="Select an image file", 
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    
    if image_path:
        process_image(image_path)
    else:
        print("No file selected.")

if __name__ == "__main__":
    main()