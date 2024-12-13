import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import font_manager, rc
import matplotlib.font_manager as fm
from matplotlib.ticker import MaxNLocator
import os

font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
if os.path.exists(font_path):
    font_name = fm.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_name)
else:
    print(f"Font file not found: {font_path}")

plt.rcParams['axes.unicode_minus'] = False

def word_transition_check(words : list, num : int, all_data : list):
    df = pd.DataFrame(all_data)
    selected_df = df[df['keyword'].isin(words)]
    
    sns.set()
    plt.rcParams['font.size'] = 10
    plt.rcParams['font.family'] = 'NanumGothic'
    cnt = 0
    fig, ax = plt.subplots()
    for word in words:
        if cnt == num:
            break
        one_df = selected_df[selected_df['keyword'] == word]
        one_df = one_df.sort_values(by='date')
        ax.plot(one_df['date'], one_df['num'], label=f'Transition of {word}', marker='o')
        cnt += 1
        
    ax.set_title("Compare Transition of words")
    ax.set_xlabel("Date")
    ax.set_ylabel("num")
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    ax.grid(True)
    
    plt.tight_layout()
    plt.savefig("image/word_transition.png")