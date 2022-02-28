import requests
from bs4 import BeautifulSoup


URL = 'https://pythonjobs.github.io/'

page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")

result = soup.find(class_ ="job_list")
# print (result.prettify())

jobs= result.find_all("div", class_="job")
for job in jobs:
    h1 = job.find("h1")
    a= h1.contents
    print(f"{h1.text} \n  {a} \n\n")
