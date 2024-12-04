from typing import List, Dict
import re

def is_korean(text):
    return bool(re.fullmatch(r'[가-힣]+', text))

def make_list(keywords : str) -> List[str]:
    keywords_list = keywords.split(" ")
    keywords_list = [keyword for keyword in keywords_list if is_korean(keyword)]
            
    return keywords_list