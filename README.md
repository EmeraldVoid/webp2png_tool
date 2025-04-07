![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)
![Pillow](https://img.shields.io/badge/Uses-Pillow-yellow)
![tqdm](https://img.shields.io/badge/Uses-tqdm-lightgrey)
![License](https://img.shields.io/badge/License-Unlicensed-green)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)

# 🖼️ webp2png_tool.py

**webp2png_tool.py** is a simple and beginner-friendly Python script that allows you to **batch convert `.webp` images to `.png` format**. It features an interactive terminal interface, progress tracking, and cross-platform support for a clean exit prompt.

---

## 🚀 Features

- 🔍 Scans a folder for `.webp` images  
- 💾 Saves converted `.png` files to a chosen directory  
- 📊 Displays how many files are being converted  
- ⏳ Shows a progress bar via `tqdm`  
- 🧹 Platform-compatible "Press any key to exit" at the end  

---

## 📦 Requirements

- Python 3.6 or higher  
- [Pillow](https://python-pillow.org) – for image processing  
- [tqdm](https://github.com/tqdm/tqdm) – for progress bar display

Install dependencies with:

```bash
pip install pillow tqdm
```

---

## 🛠️ Usage

1. Download or clone this repository.
2. Run the script:

```bash
python webp2png_tool.py
```

3. Follow the interactive prompts:
   - Enter the path to the folder containing `.webp` files
   - Enter the path to the folder to save `.png` files

---

## 📋 Example

```plaintext
=== WEBP to PNG Converter ===
Enter the path to the folder containing .webp files: C:\Users\You\Pictures\webp
Enter the path to the folder to save .png files: C:\Users\You\Pictures\png

3 file(s) are being converted...

Converting: 100%|█████████████████████████████| 3/3 [00:00<00:00, 20.56file/s]

3 file(s) have been converted successfully!

Press any key to exit...
```

---


## ❓ FAQ

### Q: What does this tool do?  
**A:** This script batch converts `.webp` image files into `.png` format. It’s useful if you have a folder full of `.webp` files and want to convert them all at once.

---

### Q: What programming language is it written in?  
**A:** This tool is written in Python and uses the following libraries:
```python
import os  
import sys  
from PIL import Image  
from tqdm import tqdm
```

---

### Q: Why does the code look so basic?  
**A:** I'm currently learning Python, and this project was a learning exercise for me. I also used AI assistance to help with parts I didn’t fully understand yet. I appreciate constructive feedback, and I hope you find something else in my GitHub that interests you!
