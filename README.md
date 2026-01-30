# 🎨 ASCII Art Generator

Transform images into beautiful ASCII art using Python.  
This project converts an input image into text-based art by analyzing pixel brightness and mapping it to ASCII characters using **image processing and graph traversal algorithms**.

---

## 📌 Project Purpose

The main purpose of this project is to:

- Understand **image processing fundamentals**
- Learn **grayscale conversion**
- Apply **logic-based pixel-to-character mapping**
- Use **BFS (Breadth-First Search)** for region-based analysis
- Demonstrate how visual data can be represented using **plain text**

This project is useful for:
- Learning Python image handling
- Exploring algorithmic creativity
- Understanding pixel-level data transformation
- Applying graph algorithms to real-world data

---

## ⚙️ How the Code Works

The ASCII art generation follows these structured steps:

---

### 1️⃣ Load the Image
- The input image is loaded using the `PIL (Pillow)` library.
- Image data is accessed at the pixel level for processing.

---

### 2️⃣ Resize the Image
- The image is resized to a fixed width while maintaining its **aspect ratio**.
- A correction ratio is applied to match terminal character dimensions.
- This ensures the ASCII output fits well in the terminal.

---

### 3️⃣ Convert to Grayscale
- The image is converted into grayscale.
- Each pixel is represented by a brightness value between **0 and 255**.
- Grayscale simplifies intensity comparison and mapping.

---

### 4️⃣ Region Detection Using BFS (Core Algorithm)
- **Breadth-First Search (BFS)** is applied to group neighboring pixels.
- Adjacent pixels with similar intensity values are treated as a **single region**.
- This helps in:
  - Preserving edges
  - Improving detail clarity
  - Reducing random noise

---

### 5️⃣ Map Pixels to ASCII Characters
- Pixel intensity is mapped to a predefined ASCII character set.
- Darker pixels are represented by **denser characters** (`@`, `#`).
- Lighter pixels are represented by **lighter characters** (`.`, `:`).
- Region size is used to refine character selection for better accuracy.

---

### 6️⃣ Generate ASCII Art
- ASCII characters are placed in a 2D grid.
- Characters are arranged row by row to form the final image structure.

---

### 7️⃣ Display or Save Output
- The generated ASCII art is printed directly in the terminal.
- Output can also be redirected to a text file if required.

---

## ▶️ How to Run the Program

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Minhaj078/Ascii_Art_Algorithm.git
cd REPOSITORY_NAME
```
### 2️⃣ Install Dependencies
Make sure Python is installed, then install Pillow:

```bash
pip install pillow
```

### 3️⃣ Run the Program
```
python ascii_art.py
```

## 🧠 Algorithm Highlights
```
BFS-based region grouping

Threshold-based intensity comparison

Adaptive ASCII character mapping

Better edge and detail preservation compared to simple pixel mapping
```

## 🎓 Learning Outcomes
```
Practical understanding of image processing

Real-world application of BFS algorithm

Improved logical and algorithmic thinking

Creative visualization using Python
```
