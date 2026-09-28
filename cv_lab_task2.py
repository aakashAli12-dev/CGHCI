import os
from PIL import Image, ImageFilter


def find_image():
    candidates = [
        "input.jpg",
        "input.png",
        "input.jpeg",
        "Akash1.jpeg",
        "Akash2.jpeg",
        "Akash1.jpg",
        "Akash2.jpg",
    ]

    for name in candidates:
        if os.path.exists(name):
            return name
    raise FileNotFoundError("No image file found in the folder. Please add input.jpg or one of the project images.")


image_path = find_image()

with Image.open(image_path) as img:
    gray = img.convert("L")
    binary_mask = gray.point(lambda p: 255 if p > 128 else 0, mode="1").convert("L")
    blurred = gray.filter(ImageFilter.BoxBlur(5))

    binary_mask.save("output_mask.jpg")
    blurred.save("output_blurred.jpg")

print("Processing completed successfully!")
print(f"Input image used: {image_path}")
print("Saved: output_mask.jpg")
print("Saved: output_blurred.jpg")