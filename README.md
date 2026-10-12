## Overview
A Python-based image-processing pipeline designed to enhance and extract retinal blood-vessel structures from retinal images.

The project explores traditional computer vision techniques for medical image analysis, using contrast enhancement and morphological operations to make vascular structures more distinguishable.

## Features
- Loads and processes retinal images in batches.
- Extracts the green channel from colour images for grayscale analysis.
- Applies Contrast Limited Adaptive Histogram Equalization (CLAHE) to improve local contrast.
- Uses morphological image-processing operations to help isolate vessel-like structures.
- Saves processed images to an output directory.
- Uses Matplotlib to visualize image-processing results.

## Technologies
- **Language:** Python
- **Libraries:** OpenCV, NumPy, Matplotlib
- **Concepts:** Image enhancement, grayscale processing, morphological operations, medical computer vision

## Pipeline
1. Load retinal images from an input directory.
2. Extract the green channel for analysis.
3. Enhance local contrast using CLAHE.
4. Apply morphological operations to emphasize vessel structures.
5. Visualize and save the processed results.

## Applications
Retinal vessel analysis is relevant to ophthalmic imaging and research into automated analysis of retinal structures. This project is an exploration of image-processing methods, not a diagnostic system.

## Future Improvements
- Evaluate the output against manually annotated vessel masks.
- Calculate segmentation metrics such as precision, recall, and Dice score.
- Compare traditional image processing with a machine-learning segmentation model.
- Add support for standardized retinal image datasets.
- Improve visualization and automated result reporting.
- 
Developed as a personal project exploring medical image processing and computer vision.
