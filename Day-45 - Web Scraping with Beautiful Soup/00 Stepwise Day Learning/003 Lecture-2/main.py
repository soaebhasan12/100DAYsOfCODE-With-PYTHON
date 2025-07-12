# 003: Finding and Selecting Particular Elements with BeautifulSoup.

from bs4 import BeautifulSoup
# import lxml


# Challenge: open the website.html. Store all of its text in a variable called contents.

with open("D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/Day-45 - Web Scraping with Beautiful Soup/Day-45 - Web Scraping with Beautiful Soup/00 Stepwise Day Learning/003 Lecture-2/website.html", encoding="utf-8") as file:
    contents = file.read()
print(contents)
 

soup = BeautifulSoup(contents, "html.parser")  


# 1. Find all anchor tags  
all_links = soup.find_all("a")  
for link in all_links:  
    print(link.get("href"))  # Extract links  

# 2. Find by ID  
heading = soup.find(name="h1", id="name")  

# 3. Find by class  
section_heading = soup.find(name="h3", class_="heading")  

# 4. CSS Selectors  
company_url = soup.select_one("p a")  # First <a> inside <p>  
all_headings = soup.select(".heading")  # All elements with class="heading"  