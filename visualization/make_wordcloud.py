from wordcloud import WordCloud, STOPWORDS
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import platform

#TF-IDF(Term Frequency-Inverse Document Frequency)를 이용한 워드클라우드 생성
def word_cloud(all_data : list):
    wc = {}
    for data in all_data:
        if data['keyword'] in wc:
            wc[data['keyword']] += data['num']
        else:
            wc[data['keyword']] = data['num']
            
    # num을 정규화
    max_num = max(wc.values())
    for word in wc:
        wc[word] = wc[word] / max_num
    
    stopwords = set(STOPWORDS)
    stopwords.add('한국철도공사')
    
    wordcloud = WordCloud(background_color= 'white',
                          font_path='NanumGothic.ttf',
                          max_words=200,
                          stopwords=stopwords,
                          )
    wordcloud.generate_from_frequencies(wc)
    
    plt.figure(figsize=(20, 20))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('../image/wordcloud.png')
    
    print("워드클라우드가 저장되었습니다.")