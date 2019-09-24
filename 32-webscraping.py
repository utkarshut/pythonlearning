#beautifulsoup4 lxml html5lib requests

import  csv

from bs4 import  BeautifulSoup
import  requests

with open('32-webscraping.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

print(soup.prettify())

print(soup.p)

print(soup.p.text)

match = soup.find('div', class_='footer')
print(match.p.text)
csv_file = open('32-webscraping.csv', 'w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['headline', 'summary'])


for article in soup.find_all('div'):
    print("-->", article.p.text)
    print("-->", article.h2.text)
    print(article.find('p'))
    csv_writer.writerow([article.p.text, article.h2.text])

csv_file.close()
