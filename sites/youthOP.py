from bs4 import BeautifulSoup
import requests

# post extractor
url = 'https://www.youthop.com/bd/internships/page/2'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
postGroup = []
for post in soup.find_all('div', {'class': 'post-header'}):
    postname =""
    postLink = ""
    for heading in post.find_all('h3'):
        postname = heading.text
        # print(heading.text)
    for a in post.find_all('a'):
        postLink = a['href']
        # print(a['href'])
    Group = (postname,postLink)
    postGroup.append(Group)
    # print('```````````````````````````````````````````````````````````````````````````````````````````````````````````````')

print(postGroup)
# url = 'https://www.youthop.com/bd/internships/janata-wifi-is-looking-for-iot-research-engineer-intern-2023-in-dhaka?ref=browse_page'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
#
#
# post-title entry-title

# div = soup.find('div', {'class': 'div-class'})
#
# # Find all the 'a' tags within that div
# for a in div.find_all('a'):
#     print(a.get('href'))