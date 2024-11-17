from news.news import get_news
from news.keywords import get_keywords
from database.MongoDB import get_db
from database.make_list import make_list
from database.schema import get_all_data, update_db
from database.schema1 import get_all_network, update_network_db
from datetime import datetime
from visualization.Top10 import top10
from visualization.make_wordcloud import word_cloud
from visualization.cocurrence import cocurrence_network


def main():
    db = get_db()
    collection = db['date2keyword']
    all_data = collection.find()
    all_data = list(all_data)
    all_data_list = get_all_data(all_data)
    
    collection1 = db['keyword2network']
    all_data1 = collection1.find()
    all_data1 = list(all_data1)
    all_pairs_list = get_all_network(all_data1)
    
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
                update_network_db(keyword2list, date, all_pairs_list, collection1)
                
        elif select == '2':
            top10(all_data_list)
            #print("top10이 저장되었습니다.")   
             
        elif select == '3':
            print("날짜 범위를 입력하세요 (시작 날짜, 끝 날짜)" )
            start_date = input("시작 날짜: ")
            end_date = input("끝 날짜: ")
            cocurrence_network(start_date, end_date, all_pairs_list)
            #print("cocurrence network가 저장되었습니다.")
            
        elif select == '4':
            word_cloud(all_data_list)
            #print("word cloud가 저장되었습니다.")
            
        elif select == '5':
            print("종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")
        
if __name__ == "__main__":
    main()