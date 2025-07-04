# 🎉 Birthday Wisher App

A Python automation project that sends personalized birthday emails to your friends and family on their special day. Built with pandas, datetime, and smtplib for seamless scheduling and delivery.

---

## ✨ Features
- 📅 Automatically checks today's date and matches it with birthdays in your CSV file
- 💌 Sends a personalized email using a random letter template
- 🔒 Secure login with your email credentials
- 📝 Easy to customize templates and recipient list
- 🐍 100% Python, no external dependencies beyond pandas

---

## 🛠️ Tech Stack
| Category      | Technology         |
|---------------|-------------------|
| Language      | Python 3.x        |
| Email         | smtplib           |
| Data Handling | pandas, CSV       |
| Date/Time     | datetime          |
| OS Support    | Windows, macOS, Linux |

---

## 🚀 Usage
1. **Update your details:**
   - Set `MY_EMAIL` and `MY_PASSWORD` in `main.py` to your email and password.
   - Update the SMTP server address for your email provider (e.g., Gmail, Outlook).
2. **Allow less secure apps:**
   - Enable access for less secure apps in your email account settings (or use an app password if required).
3. **Prepare your data:**
   - Edit `birthdays.csv` to include your friends' names, emails, and their birth dates (month and day).
   - Example CSV columns: `name,email,year,month,day`
4. **Customize your templates:**
   - Edit or add files in `letter_templates/letter_1.txt`, `letter_2.txt`, etc. Use `[NAME]` as a placeholder for the recipient's name.
5. **Run the script:**
   ```bash
   python main.py
   ```

---

## 📦 Example
```
name,email,year,month,day
John,john@example.com,1990,7,4
```

---

## 📋 Requirements
- Python 3.x
- pandas

Install pandas if needed:
```bash
pip install pandas
```

---

## 🙏 Credits
- Inspired by the 100 Days of Python Bootcamp
- Letter templates and starter data provided by the course

---

## 📄 License
This project is for educational purposes as part of #DaysOfCode.

---

**Automate your celebrations! 🥳**
