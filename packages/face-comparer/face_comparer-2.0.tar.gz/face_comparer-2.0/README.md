# Face Comparer

## Overview

This Python module provides functionality to encode images to Base64 format and compare faces. It supports both file-based and Base64-based image comparisons.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Importing the Module](#importing-the-module)
  - [Convert Image to Base64](#convert-image-to-base64)
  - [Convert Base64 to Image](#convert-base64-to-image)
  - [Compare Faces from Image Paths](#compare-faces-from-image-paths)
  - [Compare Faces from Base64 Strings](#compare-faces-from-base64-strings)
- [Features](#features)
- [Limitations](#limitations)
- [License](#license)

## Installation

Ensure you have the required dependencies installed before using this module:

```bash
pip install face_recognition numpy pillow
```

## Usage

### Importing the Module

```python
from face_comparer import ImageConverter, FaceComparer
```

### Convert Image to Base64

```python
converter = ImageConverter()
base64_string = converter.image_to_base64("path_to_image.jpg")
```

### Convert Base64 to Image

```python
image_array = converter.base64_to_image(base64_string)
```

### Compare Faces from Image Paths

```python
comparer = FaceComparer()
result = comparer.compare_faces("image1.jpg", "image2.jpg")
print(result)
```

### Compare Faces from Base64 Strings

```python
result = comparer.compare_faces_from_base64(base64_string1, base64_string2)
print(result)
```

## Features

- Convert images to Base64 format and vice versa.
- Compare faces using `face_recognition`.
- Handle both file paths and Base64 encoded images.

## Limitations

- Requires images to have at least one recognizable face.
- Works best with clear, front-facing images.

## License

This project is licensed under the MIT License.
