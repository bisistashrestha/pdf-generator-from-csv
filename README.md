# PDF Generator from Topics

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)  
[![PDF](https://img.shields.io/badge/Output-PDF-red)](output.pdf)

---

## 📌 Project Overview
This project generates a **multi-page PDF** using topic names and page counts specified in a `topics.csv` file.  
Each topic's first page includes a **header with the topic title**, and all pages include a **footer with the topic name and page number**.

The final output is saved as **`output.pdf`**.

---

## 📂 Files in this Project
- `main.py` → Script to generate the PDF.  
- `topics.csv` → Input file with topics and their respective page counts.  
- `output.pdf` → Generated PDF output.  
- `LICENSE` → MIT License file.  
- `README.md` → Project documentation.  

---

## 🛠️ Requirements
- Python 3.x  
- [fpdf](https://pypi.org/project/fpdf/)  
- [pandas](https://pypi.org/project/pandas/)  

**Install dependencies**:
```bash
pip install -r Requirements.txt
```

---

## 📄 Usage
**Run the script:**
```bash
python main.py
```

**The generated pdf will be saved as:**
```
output.pdf
```

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).
