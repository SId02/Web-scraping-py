import requests
from bs4 import BeautifulSoup   as bs
import csv
# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
 
# check status code for response received
# success code - 200
print(r)
 
# print content of request
print(r.content)

# print request object
print(r.url)
   
# print status code
print(r.status_code)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())


# Getting the title tag
print(soup.title)
 
# Getting the name of the tag
print(soup.title.name)
 
# Getting the name of parent tag
print(soup.title.parent.name)
 
# use the child attribute to get
# the name of the child tag


s = soup.find('div', class_='entry-content')
content = s.find_all('p')
 
print(content)


# Finding by id
s = soup.find('div', id= 'main')
 
# Getting the leftbar
leftbar = s.find('ul', class_='leftBarList')
 
# All the li under the above ul
content = leftbar.find_all('li')
 
print(content)

#Removing the tags from the content of the page 

s = soup.find('div', class_='entry-content')
 
lines = s.find_all('p')
 
for line in lines:
    print(line.text)


#Python BeautifulSoup Extracting Links

# find all the anchor tags with "href"
for link in soup.find_all('a'):
    print(link.get('href'))

#Python BeautifulSoup Extract Image 

images_list = []
 
images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"src": src, "alt": alt})
     
for image in images_list:
    print(image)


#Python BeautifulSoup saving to CSV


URL = 'https://www.geeksforgeeks.org/page/'
 
soup = bs(req.text, 'html.parser')
 
titles = soup.find_all('div', attrs={'class', 'head'})
titles_list = []
 
count = 1
for title in titles:
    d = {}
    d['Title Number'] = f'Title {count}'
    d['Title Name'] = title.text
    count += 1
    titles_list.append(d)
 
filename = 'titles.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['Title Number','Title Name'])
    w.writeheader()
     
    w.writerows(titles_list)



