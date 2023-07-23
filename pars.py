# import requests
# from bs4 import BeautifulSoup as BS
# respons=requests.get('https://stopgame.ru/news')
# html=BS(respons.content,'html.parser')
# for i in html.select('.list-view > div '):
#     title=i.select('._title_1tbpr_49')
#     try:
#         print(title[0].text)
#     except IndexError:
#         print(title)
# print('sdfs')

import requests
from bs4 import BeautifulSoup as BS
search=input('')
search.replace(' ','_')
respons=requests.get(f'https://ru.wikipedia.org/wiki/{search}')
html=BS(respons.text,'html.parser')
x=html.select('.mw-parser-output')[0]  
# for i in x:


print(x.select('p')[0].text)
print(x.select('p')[1].text)
print(x.select('p')[2].text)

# print('------------------------------------------')
# print(x.select('p')[0][1])
# print(x.select('p')[0][1])
    # result=[]
    # for g in x:
    #     print(g)
    #   # result.append(g[0].text)
    # print(html.select('.mw-parser-output')[1])




print('-----------------------------------------------------------------------------')
#     title=i.select('p')
#     try:
#         print(title[0][1][2].text)
#     except IndexError:
#         print(title)
# print('sdfs')
