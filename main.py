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
from visualization.word_transition import word_transition_check
from llama_FineTuning.data_2_csv import append_discription_csv, append_topk_csv, append_cocurrence_csv


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
    
    #append_cocurrence_csv(all_pairs_list)
    
    select = 0
    while select != '5':
        print("원하시는 기능을 선택하세요")
        print("1. 뉴스 가져와서 키워드 추가하기")
        print("2. 많이 언급된 키워드 top10 보기")
        print("3. 키워드 관계도 분석하기")
        print("4. 워드클라우드로 시각화하기")
        print("5. 시간 흐름에 따른 keyword 분석")
        print("6. 종료")
        select = input("선택: ")
        
        if select == '1':  
            display_num = input("가져올 뉴스의 수를 입력하세요: ")
            start_num = input("가져올 뉴스의 시작 위치를 입력하세요: ")
            sort = input("정렬 기준을 입력하세요(sim, date): ")
    
            news_list, query = get_news(int(display_num), int(start_num), sort)
            for news in news_list:
                discription = news['description']
                pub_date = news['pubDate']
                date_obj = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z")
                date = date_obj.strftime("%Y-%m-%d")
                date_korean = date_obj.strftime("%Y년 %m월 %d일")
                keywords = get_keywords(discription)
                print(keywords)
                #print(type(keywords))
                keyword2list = make_list(keywords)
        
                update_db(keyword2list, date, all_data_list, collection, query)
                update_network_db(keyword2list, date, all_pairs_list, collection1, query)
            ask_data = input("데이터 수집을 원하십니까?")
            if ask_data == "Yes":
                append_discription_csv(discription, date_korean, keyword2list)
                append_topk_csv(all_data_list)
                append_cocurrence_csv(all_pairs_list)
                
        elif select == '2':
            top10(all_data_list)
            #append_topk_csv(all_data_list)
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
            num = input("비교하고 싶은 단어의 개수 (1~3) : ")
            words = input("추이를 확인하고 싶은 단어를 입력하세요 : ").split()
            word_transition_check(words, num, all_data_list)
            
        elif select == '6':
            print("종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")
        
if __name__ == "__main__":
    main()