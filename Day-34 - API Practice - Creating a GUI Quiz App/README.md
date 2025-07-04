# 🧠 Quizzler App - GUI Quiz Game

A modern Python GUI quiz app that fetches trivia questions from the Open Trivia Database API and challenges you with a fun, interactive quiz! Built with Tkinter and requests, this project is a great way to learn about APIs, GUI programming, and OOP in Python.

---

## ✨ Features
- 🔄 Fetches 10 random True/False questions from the Open Trivia Database API
- 🖼️ Beautiful Tkinter interface with score tracking
- ✅ Instant feedback with color changes for correct/incorrect answers
- 🏁 End-of-quiz summary and button disabling
- 🐍 100% Python, minimal dependencies

---

## 🛠️ Tech Stack
| Category      | Technology         |
|---------------|-------------------|
| Language      | Python 3.x        |
| GUI Framework | Tkinter           |
| HTTP Client   | requests          |
| Data Handling | OOP, API, JSON    |
| OS Support    | Windows, macOS, Linux |

---

## 🚀 Usage
1. **Install requirements:**
   ```bash
   pip install requests
   ```
2. **Add images:**
   - Place `true.png` and `false.png` in an `images/` folder in the same directory as `main.py`.
3. **Run the app:**
   ```bash
   python main.py
   ```
4. **Play the quiz:**
   - Click True or False to answer each question
   - Watch your score update and get instant feedback

---

## 📦 File Structure
- `main.py` — App entry point
- `data.py` — Fetches questions from the API
- `question_model.py` — Question class
- `quiz_brain.py` — Quiz logic and score tracking
- `ui.py` — Tkinter GUI
- `images/true.png` & `images/false.png` — Button images

---

## 📋 Requirements
- Python 3.x
- requests
- Tkinter (comes pre-installed with most Python distributions)

---

## 🙏 Credits
- Questions provided by the [Open Trivia Database API](https://opentdb.com/)
- Inspired by the 100 Days of Python Bootcamp

---

## 📄 License
This project is for educational purposes as part of #DaysOfCode.

---

**Test your knowledge and have fun! 🏆**
