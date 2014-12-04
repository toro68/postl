import requests
from bs4 import BeautifulSoup
url = 'https://www.strand.kommune.no/innsyn.aspx?response=journalpost_postliste&MId1=1031&scripturi=/innsyn.aspx&skin=infolink&fradato=2014-11-24T00:00:00'
r = requests.get(url)
r.content
soup = BeautifulSoup(r.content)
#print soup.prettify()
##links = soup.find_all("a")
##for link in links:
##    #if "http" in link.get("href")# print link.get("href")
##    print "<a href='%s'>%s</a>" %(link.get("href"), link.text)

g_data = soup.find_all("tbody")
##lines = (line.strip() for line in g_data.splitlines())
##g_data = soup.find(('div',{'class':['content-cell']})
##print g_data

##g_data = soup.findAll('div',{'class':['content-cell string']})
for item in g_data:
    try:	#print item.find_all('td', {'class': 'content-cell'})
##        print item.contents[0].find_all("td", {"class": "content-cell string"}).text
        print item.text
##        print item           
##        print(str(line.get_text()))
    except:
        pass
