import os
import csv
import pandas as pd
from itertools import groupby
from collections import defaultdict

def append_discription_csv(discription, date, keyword2list, headers=["input", "response"]):
    file_path = "llama_FineTuning/data.csv"
    file_exists = os.path.exists(file_path)
    
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        if not file_exists and headers:
            writer.writerow(headers)
        
        query = date + "에 "
        count = 0
        for keyword in keyword2list:
            count += 1
            if keyword != "한국철도공사":
                query = query + keyword 
                if count < len(keyword2list):
                    query += ", "
                if count == 7:
                    query_parts = query.rsplit(", ", 1)
                    query = query_parts[0] + " " + query_parts[1]
                    break
        query += " 와 관련된 뉴스의 내용은?"
                
        response = discription
        data = [query, response]
        
        writer.writerow(data)
        
def append_topk_csv(all_data_list, headers=["input", "response"]):
    file_path = "llama_FineTuning/data.csv"
    
    sorted_data = sorted(all_data_list, key=lambda x : x["date"])
    results = {
        date: sorted(list(group), key=lambda x: x['num'], reverse=True)
        for date, group in groupby(sorted_data, key=lambda x : x['date'])
    }
    
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        dates = results.keys()
        #print(len(results))
        for date in dates:
            query = "제일 많이 언급된 키워드 순으로 알려줘"
            date_korean = date.replace("-", "년 ", 1).replace("-", "월 ", 1) + "일"
            date_query = date_korean + "에 " + query
            
            response =""
            count = 0
            for result in results[date]:
                count +=1
                response += result['keyword'] + ", "
                if count > 10:
                    break
            
            response_parts = response.rsplit(", ", 1)
            response = response_parts[0] + " " + response_parts[1]
            
            data = [date_query, response]
        
            writer.writerow(data)
            
def append_cocurrence_csv(all_pairs_list, headers=["input", "response"]):
    file_path = "llama_FineTuning/data.csv"
        
    sorted_data = sorted(all_pairs_list, key=lambda x : x["date"])
    results = {
        date : list(group)
        for date, group in groupby(sorted_data, key=lambda x : x['date'])
    }
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        #print(results)
        #dates = results.keys()
        for date, items in results.items():
            table = defaultdict(dict)
            for item in items:
                #print(item)
                keyword1, keyword2 = item['keywords']
                #print(keyword1)
                
                table[keyword1][keyword2] = item['num']
                table[keyword2][keyword1] = item['num']
            
            date_korean = date.replace("-", "년 ", 1).replace("-", "월 ", 1) + "일" 
            keys = table.keys()
            #print(keys)
            for keyword1 in keys:
                query = date_korean + "에 " + keyword1 + "와 같이 많이 언급된 키워드 순으로 알려줘"
                response = ""
                sorted_keywords = sorted(table[keyword1].items(), key=lambda x: x[1], reverse=True)
                for keyword2, num in sorted_keywords:
                    response += keyword2 + ", "
                    
                response_parts = response.rsplit(", ", 1)
                response = response_parts[0] + " " + response_parts[1]
                
                data = [query, response]
                
                writer.writerow(data)