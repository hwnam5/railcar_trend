import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import font_manager, rc
import matplotlib.font_manager as fm
import os

font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
if os.path.exists(font_path):
    font_name = fm.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_name)
else:
    print(f"Font file not found: {font_path}")

plt.rcParams['axes.unicode_minus'] = False

def top10(all_data : list):
    df = pd.DataFrame(all_data)
    sns.set()
    plt.figure(figsize=(15,5))
    plt.rcParams['font.size'] = 10
    plt.rcParams['font.family'] = 'NanumGothic'
    ax = sns.barplot(x='num', y='keyword',
                     data=df.sort_values(by='num', ascending=False).head(10),
                     )
    ax.set_title('Top 10 Keywords')
    ax.set(xlabel='Overall', ylabel='Keyword')
    
    #plt.show()
    plt.savefig('./image/top10.png')
    print("Top 10 키워드가 저장되었습니다.")