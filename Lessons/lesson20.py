# Lesson 20: Web Scraping in Python
# In this lesson, we will explore web scraping, which involves extracting data from websites.

# What is Web Scraping?
# Web scraping is the process of extracting data from websites.
# It is commonly used for data collection, analysis, and automation.

# Using BeautifulSoup for Web Scraping
# BeautifulSoup is a Python library used for parsing HTML and XML documents.

from bs4 import BeautifulSoup
import requests

# Fetching a Web Page
# Use the requests module to fetch the content of a web page.

# Example:
url = "https://example.com"
response = requests.get(url)

# Parsing the HTML Content
# Use BeautifulSoup to parse the HTML content.

# Example:
soup = BeautifulSoup(response.content, "html.parser")

# Extracting Data
# Use BeautifulSoup methods to extract data from the parsed HTML.

# Example:
heading = soup.find('h1')
if heading:
    print("Heading:", heading.text)

# Extracting Links
# Use BeautifulSoup to extract all links from the page.

# Example:
links = soup.find_all('a')
for link in links:
    href = link.get('href')
    if href:
        print("Link:", href)

# Extracting Images
# Use BeautifulSoup to extract all image URLs from the page.

# Example:
images = soup.find_all('img')
for img in images:
    src = img.get('src')
    if src:
        print("Image URL:", src)

# Hands-On Exercises:
# 1. Scrape the titles of articles from a news website.
# 2. Extract and print all image URLs from a web page.
# 3. Experiment with scraping data from different types of elements (e.g., tables, lists).
# 4. Handle pagination to scrape data from multiple pages.

# Try it Yourself!
# Practice using BeautifulSoup to scrape data from websites.

# Solution Example:
# article_titles = soup.find_all('h2')
# for title in article_titles:
#     print("Article Title:", title.text)

# images = soup.find_all('img')
# for img in images:
#     src = img.get('src')
#     if src:
#         print("Image URL:", src)
