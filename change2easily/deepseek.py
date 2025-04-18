import requests
import json
import pandas as pd
import time

# OpenRouter API 키로 교체하세요
API_KEY = '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'
API_URL = 'https://openrouter.ai/api/v1/chat/completions'
MAX_RETRY = 5
# API 요청을 위한 헤더 정의
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}
df = pd.read_excel('data1.xlsx')
new_df = []
for i in range(len(df)):
    content = df['content'][i]
    page = df['page'][i]
    data = {
        "model": "deepseek/deepseek-chat:free",
        "messages": [{"role": "user", "content": f"이 글을 어린아이가 이해하기 아주 쉽게 풀어서 적어주세요? (문장구조와 형식은 유지해주세요. 결과물만 출력해주세요. 격식있는 존댓말을 사용해주세요.) {content}"}]
    }
    retry_count = 0
    while retry_count < MAX_RETRY:
        
            response = requests.post(API_URL, json=data, headers=headers)
            result = response.json()
            print(result)
            new_content = result['choices'][0]['message']['content'].strip()

            if new_content:
                new_df.append({'page': page, 'content': new_content})
                print(f"[{i}] 처리 완료")
                
                break
            else:
                retry_count += 1
                print(f"[{i}] 빈 응답, 재시도 {retry_count}/{MAX_RETRY}")
                time.sleep(1.5)

    print(new_df[i])

new_df = pd.DataFrame(new_df)
new_df.to_excel('change_data1.xlsx', index=False)