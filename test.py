import requests
from BeautifulSoup import BeautifulSoup as b4

response = requests.get('http://estu.fju.edu.tw/fjucourse/firstpage.aspx')

data = b4(response.text)
print data.find('input', {'id':'__VIEWSTATE'}).get('value')
print 
print data.find('input', {'id':'__EVENTVALIDATION'}).get('value')
