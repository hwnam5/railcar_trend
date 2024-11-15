import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import font_manager, rc
import matplotlib.font_manager as fm

mpl.use('Agg')
# 한글 폰트 설정
plt.rc('font', family='NanumGothic')
plt.rc('axes', unicode_minus=False)
#font_path = "NanumGothic.ttf"
#font_prop = fm.FontProperties(fname=font_path)
#plt.rcParams["font.family"] = font_prop.get_name()
#plt.rcParams['axes.unicode_minus'] = False

def top10(all_data : list):
    df = pd.DataFrame(all_data)
    sns.set()
    plt.figure(figsize=(15,5))
    ax = sns.barplot(x='num', y='keyword',
                     data=df.sort_values(by='num', ascending=False).head(10))
    ax.set_title('Top 10 Keywords')
    ax.set(xlabel='Overall', ylabel='Keyword')
    
    #plt.show()
    plt.savefig('../image/top10.png')
    print("Top 10 키워드가 저장되었습니다.")