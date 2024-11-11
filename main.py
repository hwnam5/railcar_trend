from news import get_news
from keywords import get_keywords
from MongoDB import get_db
from make_list import make_list
from schema import get_all_data, update_db
from datetime import datetime
from Top10 import top10
from make_wordcloud import word_cloud


def main():
    db = get_db()
    collection = db['date2keyword']
    all_data = collection.find()
    all_data = list(all_data)
    all_data_list = get_all_data(all_data)
    
    select = 0
    while select != '5':
        print("원하시는 기능을 선택하세요")
        print("1. 뉴스 가져와서 키워드 추가하기")
        print("2. 많이 언급된 키워드 top10 보기")
        print("3. 키워드 관계도 분석하기")
        print("4. 워드클라우드로 시각화하기")
        print("5. 종료")
        select = input("선택: ")
        
        if select == '1':  
            display_num = input("가져올 뉴스의 수를 입력하세요: ")
            start_num = input("가져올 뉴스의 시작 위치를 입력하세요: ")
            sort = input("정렬 기준을 입력하세요(sim, date): ")
    
            news_list = get_news(int(display_num), int(start_num), sort)
            for news in news_list:
                discription = news['description']
        
                pub_date = news['pubDate']
                date_obj = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z")
                date = date_obj.strftime("%Y-%m-%d")
                keywords = get_keywords(discription)
                print(keywords)
                #print(type(keywords))
                keyword2list = make_list(keywords)
        
                update_db(keyword2list, date, all_data_list, collection)
                
        elif select == '2':
            top10(all_data_list)    
        #elif select == '3':
            #word_cloud(all_data_list)
        elif select == '4':
            word_cloud(all_data_list)
        elif select == '5':
            print("종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")
        
if __name__ == "__main__":
    main()