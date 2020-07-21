# import requests
# from bs4 import BeautifulSoup
#
# URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
# page = requests.get(URL)
#
# soup = BeautifulSoup(page.content, 'html.parser')
# # print(soup)
# results = soup.find(id='ResultsContainer')
# # print(results.prettify())
# job_elems = results.find_all('section', class_='card-content')
# # Each job_elem is a new BeautifulSoup object.
# # You can use the same methods on it as you did before.
# for job_elem in job_elems:
#     # print(job_elem, end='\n'*2)
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='company')
#     location_elem = job_elem.find('div', class_='location')
#     print(title_elem)
#     print(company_elem)
#     print(location_elem)
#     print()
import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
# print(page.status_code)
# print(page.content)

#Now using BeautifulSoup, we can try parsing it
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

#lets try getting children of soup(the beautifulsuop object)
# print(list(soup.children))

#So three elements in list and lemme check what is its type
# print([type(item) for item in list(soup.children)])

#Trying to access the children
html = list(soup.children)[2]
# print(list(html.children))

#how abt getting the p tag text
body = list(html.children)[3]
p = list(body.children)[1]
# print(p.get_text())

#Finding all instances of a tag at once
# print(soup.find_all('p')[0].get_text())
# print(soup.find('p').get_text())

#Searching for tags by class and id
page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.find_all('p', class_='outer-text'))
# print(soup.find_all(class_="outer-text"))
# print(soup.find_all(id="first"))

#Using CSS Selectors
print(soup.select("div p"))

