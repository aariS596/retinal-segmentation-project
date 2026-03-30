import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

input_folder = "images"
output_folder = "results"

os.makedirs(output_folder, exist_ok=True)

x = 1
for filename in os.listdir(input_folder):
    x += 1

plt.figure(figsize=(x * 2, x * 2))

i = 1

plt.subplot(x, 2, i)
plt.title("Original Image")

plt.subplot(x, 2, i + 1)
plt.title("Vessel Segmentation")

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        # Convert to grayscale using green channel (better contrast for vessels)
        gray = image[:, :, 1]  # Green channel

        # Apply CLAHE to enhance contrast
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(gray)

        # Use morphological operations to enhance vessels
        # Vessels are dark structures, so use blackhat transform
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
        blackhat = cv2.morphologyEx(enhanced, cv2.MORPH_BLACKHAT, kernel)

        # Threshold to get binary mask
        _, vessel_mask = cv2.threshold(blackhat, 10, 255, cv2.THRESH_BINARY)

        # Clean up with morphological opening
        kernel_clean = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        vessel_mask = cv2.morphologyEx(vessel_mask, cv2.MORPH_OPEN, kernel_clean)

        output_path = os.path.join(output_folder, f"seg_{filename}")
        cv2.imwrite(output_path, vessel_mask)

        plt.subplot(x, 2, i)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.axis("off")

        plt.subplot(x, 2, i + 1)
        plt.imshow(vessel_mask, cmap="gray")
        plt.axis("off")

        i += 2

plt.tight_layout()
plt.subplots_adjust(wspace=0.05, hspace=0.3)
plt.show()