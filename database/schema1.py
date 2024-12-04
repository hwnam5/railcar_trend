from typing import List, Dict

def get_all_network(all_data) -> List[dict]:
    all_network_list = []
    for data in all_data:
        a_data = {
            'date' : data['date'],
            'keywords' : data['keywords'], # [word1, word2]
            'num' : data['num'],
            
        }
        all_network_list.append(a_data)
    return all_network_list
    

def update_network_db(new_keywords : list, date : str, all_data : list, collection, query):
    #for words in new_keywords:
    words_ = list(set(new_keywords))
    if query in words_:
        words_.remove(query)
    
    word_table = {}
    for i in range(len(words_) - 1):
        for j in range(i + 1, len(words_)):
            found = False
            word_i = words_[i]
            word_j = words_[j]
            if word_i < word_j:
                word_pair = [word_i, word_j]
            else:
                word_pair = [word_j, word_i]
            
            for data in all_data:
                if data['date'] == date and data['keywords'] == word_pair:
                    collection.update_one({'date': date, 'keywords': word_pair}, {'$inc': {'num': 1}})
                    data['num'] += 1
                    found = True
                    break
            if not found:
                new_data = {
                    'date' : date,
                    'keywords' : word_pair,
                    'num' : 1
                }
                all_data.append(new_data)
                collection.insert_one(new_data)
            
            