import requests
from bs4 import BeautifulSoup
url='https://www.flipkart.com/search?q=nokia7.1'
url2='https://www.amazon.com/search?q=nokia7.1'

r=requests.get(url)
r2=requests.get(url2)
print(r.status_code)
t=r.text
soup=BeautifulSoup(t,'html.parser')

print(r2.status_code)
t2=r2.text
soup=BeautifulSoup(t2,'html.parser')
