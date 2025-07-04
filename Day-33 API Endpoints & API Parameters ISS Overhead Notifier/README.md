# 🚀 API Projects: Kanye Quotes & ISS Overhead Notifier

A collection of two fun and practical Python projects using real-world APIs! Both apps are built with modern Python, requests, and Tkinter (for GUI), and are great for learning about API endpoints, parameters, and automation.

---

## 🎤 Project 1: Kanye Quotes App
A GUI app that fetches and displays random Kanye West quotes using the Kanye REST API.

### ✨ Features
- 🗣️ Get a new Kanye West quote with every click
- 🎨 Beautiful UI with custom background and button images
- 🔄 Real-time data from the Kanye REST API
- 🐍 100% Python, minimal dependencies

### 🛠️ Tech Stack
| Category      | Technology         |
|---------------|-------------------|
| Language      | Python 3.x        |
| GUI Framework | Tkinter           |
| HTTP Client   | requests          |
| OS Support    | Windows, macOS, Linux |

### 🚀 Usage
1. **Install requirements:**
   ```bash
   pip install requests
   ```
2. **Add images:**
   - Place `background.png` and `kanye.png` in the same directory as `main.py`.
3. **Run the app:**
   ```bash
   python main.py
   ```
4. **Click the Kanye button** to get a new quote!

### 📦 File Structure
- `main.py` — Main application code
- `background.png` — Background image
- `kanye.png` — Button image

---

## 🛰️ Project 2: ISS Overhead Notifier
A Python automation script that notifies you by email when the International Space Station (ISS) is overhead at your location during nighttime.

### ✨ Features
- 🛰️ Checks ISS position using the Open Notify API
- 🌙 Checks for nighttime using the Sunrise-Sunset API
- 📧 Sends an email notification when the ISS is overhead and it's dark
- 🐍 100% Python, minimal dependencies

### 🛠️ Tech Stack
| Category      | Technology         |
|---------------|-------------------|
| Language      | Python 3.x        |
| HTTP Client   | requests          |
| Email         | smtplib           |
| Date/Time     | datetime, time    |
| OS Support    | Windows, macOS, Linux |

### 🚀 Usage
1. **Install requirements:**
   ```bash
   pip install requests
   ```
2. **Configure your details:**
   - Set your email, password, latitude, longitude, and SMTP server in `main.py`.
3. **Run the script:**
   ```bash
   python main.py
   ```
4. The script will check every 60 seconds and send you an email if the ISS is overhead at night.

### 📦 File Structure
- `main.py` — Main application code

---

## 📋 Requirements (Both Projects)
- Python 3.x
- requests
- Tkinter (for Kanye Quotes, comes pre-installed with most Python distributions)

---

## 🙏 Credits
- Kanye Quotes: [Kanye REST API](https://api.kanye.rest)
- ISS Data: [Open Notify API](http://open-notify.org/)
- Sunrise/Sunset: [Sunrise-Sunset API](https://sunrise-sunset.org/api)
- Inspired by the 100 Days of Python Bootcamp

---

## 📄 License
These projects are for educational purposes as part of #DaysOfCode.

---

**Explore, learn, and have fun with APIs! 🌟**
