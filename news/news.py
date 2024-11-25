from typing import List, Dict
import requests
import urllib.request

CLIENT_ID = '1aAbJBSWAobrTJjechcF'
CLIENT_SECRET = 'OA0TgaKfJZ'

#query : 검색어, display : 출력할 뉴스의 수, start : 출력할 뉴스의 시작 위치, sort : 정렬 기준(sim, date)
def get_news(display_num : int, statrt_num : int, sort : str) -> List[dict]:
    url = "https://openapi.naver.com/v1/search/news.json?"
    Keyword = "한국철도공사"
    query ="query=" + Keyword
    #display = "&display=10"
    display = "&display=" + str(display_num)
    #start = "&start=1"
    start = "&start=" + str(statrt_num)
    #sort = "&sort=date"
    sort = "&sort=" + sort
    
    headers = {
        'X-Naver-Client-Id': CLIENT_ID,
        'X-Naver-Client-Secret': CLIENT_SECRET
    }
    
    response = requests.get(url+query+display+start+sort, headers=headers)
    
    # print(response.status_code)
    news = response.json()
    news_list = []
    
    print(news)
    for item in news['items']:
        a_news = {
            'title': item['title'],
            'originallink': item['originallink'],
            'link': item['link'],
            'description': item['description'],
            'pubDate': item['pubDate']
        }
        news_list.append(a_news)
    
    # print(item.keys())
    return news_list, Keyword


# print(get_news())
