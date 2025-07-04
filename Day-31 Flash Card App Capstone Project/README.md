# 🚀 Flashy Flash Card App

A modern, interactive flashcard app to help you master French vocabulary! This capstone project for Day 31 of #DaysOfCode uses a beautiful Tkinter GUI and smart progress tracking to make language learning fun and effective.

---

## ✨ Features
- 🇫🇷 Learn French vocabulary with English translations
- 🃏 Flashcard interface: front (French), back (English)
- ⏱️ Cards flip automatically after 3 seconds
- ✅ Mark words as known to remove them from the deck
- 💾 Progress is saved between sessions (words you know are not shown again)
- 🎨 Beautiful UI with custom images and buttons
- 🔄 Unknown words remain in the deck for more practice
- 📊 Data-driven: tracks your learning journey

---

## 🛠️ Tech Stack
| Category      | Technology         |
|---------------|-------------------|
| Language      | Python 3.x        |
| GUI Framework | Tkinter           |
| Data Handling | pandas, CSV       |
| OS Support    | Windows, macOS, Linux |

---

## 🧑‍💻 How It Works
- Loads a list of French words and their English translations from `data/french_words.csv`.
- When you mark a word as known, it is removed from your learning list and saved to `data/words_to_learn.csv`.
- If you make a mistake or want to review, unknown words remain in the deck.
- Your progress is automatically saved, so you can pick up where you left off!

---

## 🚀 Getting Started
1. **Install requirements:**
   ```sh
   pip install pandas
   ```
2. **Run the app:**
   ```sh
   python main.py
   ```
3. **Use the UI:**
   - Click the checkmark if you know the word (removes it from the deck)
   - Click the cross if you don't know the word (keeps it in the deck)

---

## 📁 File Structure
- `main.py` — Main application code
- `data/french_words.csv` — List of French words and English translations
- `data/words_to_learn.csv` — Progress file (auto-generated)
- `images/` — Card and button images

---

## 🙏 Credits
- Frequency word lists: [HermitDave on GitHub](https://github.com/hermitdave/FrequencyWords)
- Images and starter data provided by the course

---

## 📄 License
This project is for educational purposes as part of #DaysOfCode.

---

**Happy Learning! 🌟**
