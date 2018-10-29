
import requests
from bs4 import BeautifulSoup as bs
import json
token = '637784833:AAEfmbDKEl1W-_fulbqHBMpcTKscfatbhSk'
method_name = 'getUpdates'
url = 'https://api.telegram.org/bot{}/{}'.format(token, method_name)

update = requests.get(url).json()
#print(update)
#print(update['result'][0]['message']['from']['id'])

user_id = update['result'][0]['message']['from']['id'] #'762656647'

method_name = 'sendmessage'
msg = '안녕하세요'


url_cos = 'https://finance.naver.com/sise/'
req = requests.get(url_cos).text
soup = bs(req,'html.parser')    #html.parser
#print(soup)

select = soup.select_one('#KOSPI_now').text
msg_url = 'https://api.telegram.org/bot{}/{}?chat_id={}&text={}'.format(token, method_name, user_id, select)








# import requests
# url = 'https://finance.naver.com/sise/'
# req = requests.get(url).text
# soup = bs(req,'lxml')    #html.parser
# #print(soup)

# select = soup.select_one('#KOSPI_now')

#print(type(select))
# print(select.text)



# print(msg_url)
print(requests.get(msg_url))






#print(url)
#result = requests.get(url).text

#print(result)


#print(json.load(result, encoding = 'utf-8'))