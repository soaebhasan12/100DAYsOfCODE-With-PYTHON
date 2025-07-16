# Day-48: Selenium WebDriver Browser Automation & Game Bot

![Cookie Clicker Bot Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDhyZ2NtY3B6dW0ya3JtY2VlZGN5Z2VjeHp4eG5qY2VjZzZzbmZ6biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ohzdQFPJt7L3GRQSY/giphy.gif)

## 📚 Today's Lessons
1. **Introduction to Selenium WebDriver**
   - Browser automation vs. static scraping
   - Core use cases: Testing, scraping dynamic content, automating workflows

2. **Setup & Configuration**
   ```python
   from selenium import webdriver
   from webdriver_manager.chrome import ChromeDriverManager
   
   driver = webdriver.Chrome(ChromeDriverManager().install())
   ```

3. **Element Location Strategies**
   ```python
   # Modern Selenium 4+ syntax
   driver.find_element(By.CSS_SELECTOR, "#price")
   driver.find_elements(By.XPATH, "//div[@class='item']")
   ```

4. **Interaction Methods**
   ```python
   element.click()
   element.send_keys("text")
   element.send_keys(Keys.ENTER)
   ```

5. **Cookie Clicker Automation Project**
   - Continuous clicking algorithm
   - Smart upgrade purchasing system
   - Performance metrics tracking

## 🛠️ Projects
### Wikipedia Article Counter
```python
count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(f"Wikipedia has {count.text} articles")
```

### Form Autofill Bot
```python
driver.find_element(By.NAME, "email").send_keys("test@example.com")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
```

### Cookie Clicker Automation
Features:
- 600+ clicks/minute
- Dynamic upgrade purchasing
- 5-minute performance report

## 🧠 Key Concepts

- **By Class**: Location strategies (`By.ID`, `By.CSS_SELECTOR`)
- **Explicit Wait**: `WebDriverWait(driver, 10).until()`
- **Special Keys**: `Keys.RETURN`, `Keys.TAB` 
- **WebElement Methods**: `.click()`, `.send_keys()`
- **Locator Strategies**: XPath (`//div[@class]`) vs CSS (`.class`)

## 🚀 How to Run
1. Install requirements:
   ```bash
   pip install selenium webdriver-manager
   ```
2. Run any project:
   ```bash
   python cookie_clicker.py
   ```

## 🔗 Resources
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [ChromeDriver Manager](https://pypi.org/project/webdriver-manager/)
- [CSS Selector Reference](https://www.w3schools.com/cssref/css_selectors.asp)

