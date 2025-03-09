# ear-calculator

A Python module to compute Eye Aspect Ratio (EAR) from images.

## Installation

```bash
pip install ear-calculator
```

## Usage

```python
from ear_calculator import EARCalculator

model_path = "shape_predictor_68_face_landmarks.dat"
ear_calculator = EARCalculator(model_path)

with open("face_image.jpg", "rb") as img_file:
    image_data = base64.b64encode(img_file.read()).decode('utf-8')

ear = ear_calculator.get_ear_from_image(image_data)
print(f"Eye Aspect Ratio (EAR): {ear}")
```
