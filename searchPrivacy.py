import requests
import re

Engine = {
            'Google' : 'http://google.com/search?',
            'Bing' : 'http://bing.com/search?',
            'DuckDuckGo' : 'http://duckduckgo.com/'
        }
Search = {
            'BackStage' : "intext:管理|後台|後臺|登陸|登入|使用者|管理員|用戶|驗證碼|密碼|系統|帳號|Manage|admin|Login|system|adminstor"
        }

def SearchItem(target,engine = Engine['Bing'], search = Search['BackStage']):
    pages = 3
    if(engine == Engine['Bing']):
        for page in range(pages):
            url = f'{engine}q={target} {search}&first={str(page)}1'
            regular(requests.get(url,headers={'user-agent': 'Mozilla/5.0 (compatible; Bingbot/2.0'}).text,engine)

def regular(text,engine):
    if(engine == Engine['Bing']):
        # 忽略掉strong標籤
        text = re.sub(r'<strong>|</strong>', '', text)
        pattern = r'<cite>(.*?)</cite>'
        result = re.findall(pattern,text)
        print(result)

target = 'taipower.com.tw'
data = SearchItem(target,engine = Engine['Bing'])

