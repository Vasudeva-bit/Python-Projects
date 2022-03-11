import requests
import pprint
from bs4 import BeautifulSoup
res=requests.get('https://news.ycombinator.com')
soup=BeautifulSoup(res.text,'html.parser')
links=soup.select('.storylink')
points=soup.select('.subtext')
def appender(links,points) :
lis=[]
for idx,link in enumerate(links) :
score=points[idx].select('.score')
if len(score) :
linc=link.get('href')
title=link.getText()
point=score[0].getText()
if int(point.replace(' points',''))>99:
lis.append({'title':title,'link':linc,'points':point})
return fun(lis)
def fun(thing) :
return sorted(thing,key=lambda i : i['points'],reverse=True)
pprint.pprint(appender(links,points))
