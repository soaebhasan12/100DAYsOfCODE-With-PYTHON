# 002: Parsing HTML and Making Soup.

from bs4 import BeautifulSoup
# import lxml


# Challenge: open the website.html. Store all of its text in a variable called contents.

# 1. Open & Read HTML File  
with open("D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/Day-45 - Web Scraping with Beautiful Soup/Day-45 - Web Scraping with Beautiful Soup/00 Stepwise Day Learning/002 Lecture-1/website.html", encoding="utf-8") as file:
    contents = file.read()
print(contents)
 

# 2. Parse HTML  
soup = BeautifulSoup(contents, "html.parser")  


# 3. Extract Data  
print(soup.title)           # <title>...</title>  
print(soup.title.name)      # "title"  
print(soup.title.string)    # Text inside title tag  
print(soup.prettify())      # Formatted HTML  
print(soup.a)               # First <a> tag  