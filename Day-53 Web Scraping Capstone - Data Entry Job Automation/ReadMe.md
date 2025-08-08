# 🏡 Real Estate Auto-Filler Bot

A Python automation project that scrapes property listings (addresses, prices, and links) from a Zillow-style website and auto-fills them into a Google Form using Selenium.

This project simulates a **lead generation pipeline** for real estate data — scraping useful data and submitting it automatically to a form for later analysis.

---


## 🚀 Features

* Scrapes address, price, and listing links from a Zillow-clone site
* Cleans and formats raw HTML data
* Automates form filling using Selenium
* Mimics real-world admin/data entry tasks
* Modular and easy to expand for other platforms

---

## 🧰 Tech Stack



* Python           | Core language                        |
* Selenium         | Browser automation                   |
* BeautifulSoup    | HTML parsing                         |
* Requests         | Fetch page content                   |
* WebDriverManager | Manage ChromeDriver automatically    |
* Google Forms     | Target for auto-filling scraped data |

---

## 📂 Project Structure

```
Day-53 Web Scraping Capstone - Data Entry Job Automation/
│
├── main.py                 # Core scraping + automation script
├── README.md               # Project documentation
```

---

## 🧪 How It Works

1. Visits the Zillow clone website
2. Extracts:

   * Address
   * Price (cleaned, monthly rent only)
   * Link to listing
3. Loops through the extracted data
4. Opens a Google Form
5. Auto-fills each field using Selenium
6. Submits the form
7. Repeats the process for all entries

---

## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/real-estate-bot.git
cd real-estate-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Bot

Make sure Chrome is installed on your system.

```bash
python main.py
```

---

## 🧾 Requirements

* Python 3.7+
* Google Chrome installed
* Internet connection

All other dependencies will be auto-installed using `webdriver-manager`.

---

## 📌 Use Case & Earning Ideas

This project can be turned into:

* A **freelance tool** for property agents
* A backend **lead generator** for real estate startups
* A **scraper-as-a-service** utility (with rate limits & logging)
* An internal tool for automating form-based data entry

This kind of automation is highly in-demand in admin-heavy industries.

---

## 🔮 Future Scope

* Save entries in Google Sheets or CSV instead of just forms
* Add login capability for protected sites
* Schedule periodic scraping (daily/weekly)
* Deploy as a desktop GUI app
* Add error logging/reporting

---

## 🙋‍♂️ Contributing

Contributions, suggestions, or bug reports are welcome!

```bash
1. Fork the repo
2. Create a branch: git checkout -b feature/your-feature-name
3. Commit your changes: git commit -m 'Added new feature'
4. Push and create a PR
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

This bot is inspired by a capstone project in [Angela Yu's Python Bootcamp](https://www.udemy.com/course/100-days-of-code/), with added real-world improvements and tweaks.

---

> **Note:** This bot is built for educational purposes only. Do not use it on real websites without permission.

```
