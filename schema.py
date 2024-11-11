from typing import List, Dict

def get_all_data(all_data) -> List[dict]:
    all_data_list = []
    for data in all_data:
        a_data = {
            'date': data['date'],
            'keyword': data['keyword'],
            'num': data['num']
        }
        all_data_list.append(a_data)
    return all_data_list

def update_db(new_keywords : list, date : str, all_data : list, collection):
    for keyword in new_keywords:
        found = False
        for data in all_data:
            if data['date'] == date and data['keyword'] == keyword:
                collection.update_one({'date': date, 'keyword': keyword}, {'$inc': {'num': 1}})
                data['num'] += 1
                found = True
                break
            
        if not found :
            new_data = {
                'date': date,
                'keyword': keyword,
                'num': 1
            }
            all_data.append(new_data)
            collection.insert_one(new_data)
    