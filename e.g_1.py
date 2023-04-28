import requests
from bs4 import BeautifulSoup
login_url='https://passport.weibo.com/protection/mobile/sendcode?token=2YWFkRPjDAFBmo2A5LT75fIo1ajTSygbBCnByb3RlY3Rpb24'
data={
    'data': '[]',
'msg': 'succ',
'retcode': '20000000'
}
header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}
login_res=requests.post(login_url,data=data,headers=header)

url='https://s.weibo.com/top/summary/'
res=requests.get(url,headers=header,cookies=login_res.cookies)
print(res.status_code)
res.encoding='gbk'
soup=BeautifulSoup(res.text,'lxml')
hot_list=soup.find('tbody').find_all('tr')
for info in hot_list:
    hot_number=info.find('td',class_='td-01').text
    key_word=info.find('td',class_='td-02')
    dict={
        '序号':hot_number,
        '关键词':key_word
    }
    print(dict)


