import requests
from bs4 import BeautifulSoup
import csv
data_list=[]
header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'authority': 's.weibo.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.9',
    'cookie': 'SINAGLOBAL=9921820861270.05.1682168751814; UOR=,,www.google.com; _s_tentry=-; Apache=2034823725165.6287.1682302376344; ULV=1682302376386:4:4:3:2034823725165.6287.1682302376344:1682257850817; PC_TOKEN=b0f6c3a615; WBtopGlobal_register_version=2023042410; SUB=_2A25JQZYZDeRhGeBJ6FEY9SzIwzqIHXVqNoDRrDV8PUNbmtAGLUnSkW9NRlvl3UNT5cwkeIBKMMARUPMjb4wOrxqo; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWLuBc1XL9BZUj4R8k9psxO5JpX5o275NHD95QcS0e01K-EShncWs4Dqcjei--ciK.Ni-zcUcvN; ALF=1682907334; SSOLoginState=1682302537; un=18436072711; WBStorage=4d96c54e|undefined'

}
url='https://s.weibo.com/top/summary?cate=realtimehot'

res=requests.get(url,headers=header)
print(res.status_code)
soup=BeautifulSoup(res.text,'lxml') 
hot_list=soup.find('tbody').find_all('tr')
for info in hot_list:
    hot_number=info.find('td',class_='td-01').text
    key_word=info.find('td',class_='td-02').find('a').text.strip()
    hot_url='https://s.weibo.com'+info.find('td',class_='td-02').find('a')['href']
    dict={
        '序号':hot_number,
        '关键词':key_word,
        '热搜链接':hot_url
    }
    print(dict)
    data_list.append(dict)
# with open('D:/software/Python练习/文件存储/微博热搜.csv','w',encoding='utf-8-sig',newline='') as f:
#     f_csv=csv.DictWriter(f,fieldnames=['序号','关键词','热搜链接'])
#     f_csv.writeheader()
#     f_csv.writerows(data_list)