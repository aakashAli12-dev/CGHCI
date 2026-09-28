import numpy as np

def adjust_brightness_contrast(image, alpha=1.0, beta=0):
    """
    Applies:
        O = alpha * I + beta

    Then clips pixel values to the valid range 0-255.
    """

    # Convert to float to avoid overflow
    adjusted = image.astype(np.float32) * alpha + beta

    # Keep pixel values between 0 and 255
    adjusted = np.clip(adjusted, 0, 255)

    # Convert back to uint8
    return adjusted.astype(np.uint8)


# Example input image represented as a NumPy array
gray = np.array([
    [100, 150],
    [200, 50]
], dtype=np.uint8)

# Increase contrast and slightly reduce brightness
result = adjust_brightness_contrast(
    gray,
    alpha=1.5,
    beta=-20
)

print("Original Image:")
print(gray)

print("\nAdjusted Image:")
print(result)