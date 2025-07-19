# Day 49: Automating Job Applications on LinkedIn with Selenium

Automate LinkedIn job applications using Selenium WebDriver to streamline your job search process. This project focuses on leveraging Python to interact with LinkedIn's "Easy Apply" feature, reducing manual effort.

## 📌 Project Overview
- **Goal**: Build a bot to automatically apply to LinkedIn jobs matching your criteria.
- **Tech Stack**: Python, Selenium WebDriver.
- **Key Features**:
  - Automated login to LinkedIn.
  - Job search with custom filters (role, location, "Easy Apply").
  - One-click application submission (phone number/resume upload).
  - Error handling for CAPTCHAs/unavailable jobs.

---

## 🛠️ Setup Instructions

### 1. **Prerequisites**
- Python 3.x installed.
- LinkedIn account (**disable 2FA** temporarily).
- Chrome/Firefox browser and matching WebDriver.

### 2. **Install Dependencies**
```bash
pip install selenium python-dotenv
```

### 3. **Configure LinkedIn**
- Upload your resume in LinkedIn settings:  
  `Me → Settings & Privacy → Job Seeking Preferences → Job Application Settings`.
- Save credentials in `.env` file:
  ```ini
  LINKEDIN_EMAIL=your_email@example.com
  LINKEDIN_PASSWORD=your_password
  ```

---

## 🚀 How It Works

### **1. Automate Login**
- Uses Selenium to navigate to LinkedIn and log in.
- Waits for page loads to avoid detection.
```python
from selenium import webdriver
import os
from dotenv import load_dotenv

load_dotenv()
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")
driver.find_element("id", "username").send_keys(os.getenv("LINKEDIN_EMAIL"))
driver.find_element("id", "password").send_keys(os.getenv("LINKEDIN_PASSWORD"))
driver.find_element("css_selector", ".btn__primary--large").click()
```

### **2. Job Search**
- Customize the search URL with parameters:
  ```python
  search_url = "https://www.linkedin.com/jobs/search/?keywords=Python+Developer&location=London&f_LF=f_AL"
  driver.get(search_url)
  ```
  - `f_AL`: Filters "Easy Apply" jobs.

### **3. Apply for Jobs**
- Targets jobs requiring only a phone number:
  ```python
  apply_button = driver.find_element("css_selector", ".jobs-apply-button")
  apply_button.click()
  driver.find_element("class_name", "fb-single-line-text__input").send_keys("1234567890")
  driver.find_element("css_selector", "footer button").click()  # Submit
  ```

### **4. Error Handling**
- Skips unavailable jobs or multi-step applications.
- Manual CAPTCHA resolution (if triggered).

---

## ⚠️ Ethical Considerations
- **Do not spam**: Only apply to relevant jobs.
- **Use a test account** if practicing.
- Respect LinkedIn’s [User Agreement](https://www.linkedin.com/legal/user-agreement).

---

## 📝 Notes & Troubleshooting
- **CAPTCHAs**: Solve manually or reduce automation speed.
- **Dynamic Elements**: Use explicit waits (`WebDriverWait`).
- **Alternative**: Save jobs/follow companies instead of applying.

---