# Resolution Changer

A simple Python utility for resizing images into multiple resolutions.  
This tool optionally crops an image to a square and generates resized versions using high-quality scaling.

I created this tool to generate icons in multiple sizes for browser extensions.

---

## ✨ Features

- Optional **centered square cropping**
- Generates multiple resolutions from a single input image
- Uses **LANCZOS resampling** for high-quality resizing
- Automatically creates the output directory if it does not exist
- Supports common image formats (JPG, PNG, etc.)
- Simple and lightweight (built with Pillow)

---

## 📦 Requirements

- Python 3.9+
- Pillow

Install Pillow:
```bash
pip install pillow
```

---

## 🚀 Usage

```python
from resolution_changer import ResolutionChanger

changer = ResolutionChanger()

changer.change_resolution(
    image_path="input.png",
    output_path="output",
    resolutions=[(16, 16), (32, 32), (48, 48), (128, 128)],
    square_cropping=True  # Default is False. Set to True to crop image to square
)
```

---

## ⚙️ Parameters

- `image_path` (str): Path to the input image  
- `output_path` (str): Directory where resized images will be saved (created automatically if it does not exist)  
- `resolutions` (list[tuple[int, int]]): List of target resolutions  
- `square_cropping` (bool, default=False):  
  - `True` → crop image to square before resizing  
  - `False` → keep original aspect ratio  

---

## 📁 Output

Images will be saved in the specified output directory:

```
output/
├── 16x16_resolution.png
├── 32x32_resolution.png
├── 48x48_resolution.png
├── 128x128_resolution.png
```

---

## ⚙️ How It Works

1. Loads the image from the given path  
2. Optionally crops the image to a **square (centered)**  
3. Resizes the image to each specified resolution  
4. Saves each result as a `.png` file  

---

## ⚠️ Notes

- Larger resolutions than the original image will be upscaled (may reduce quality)  
- If `square_cropping` is disabled, the image will be resized directly  
- Output images are always saved in **PNG format**, regardless of the input format  

---

## 📄 License

MIT License

---

## 👤 Author

Daiki Hagiwara