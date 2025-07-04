# 📝 Article Summarizer using BART (NLP)

This project is a simple Python tool that summarizes lengthy articles using **Natural Language Processing (NLP)**. It leverages a **pre-trained BART model** (`facebook/bart-large-cnn`) from Hugging Face Transformers to generate concise summaries from long texts.

---

## ✅ Task Description

**Task:** Create a tool that summarizes lengthy articles using NLP techniques.  
**Deliverable:** A Python script showcasing input text and concise summaries.

---

## 🧠 Model Used

- **Model:** `facebook/bart-large-cnn`
- **Library:** Hugging Face `transformers`
- **Approach:** Abstractive summarization using `pipeline("summarization")`

---

## 🧩 Features

- 📜 Accepts long input text (e.g., news, blogs, articles)
- 🧠 Uses pre-trained summarization model
- ✂️ Returns a clean, concise summary
- ✅ Script-based and easy to extend

---

## 📁 Project Structure

article_summarizer/<br/>
│<br/>
├── summarizer.py # Main Python script<br/>
├── requirements.txt # Python dependencies<br/>
└── README.md # Documentation<br/>

---

## ⚙️ Setup Instructions

### 1. Create and activate a virtual environment

```bash
python -m venv summarizer_env
```
# Activate (Windows)
```
summarizer_env\Scripts\activate
```
# Activate (Linux/macOS)
```
source summarizer_env/bin/activate
```
### 2. Install dependencies
```
pip install -r requirements.txt
```
## ▶️ How to Run
Simply run the Python script:
```
python summarizer.py
```
It will:

Print the original article

Print the summarized version




---
