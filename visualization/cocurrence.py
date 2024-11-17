import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib import rc
import seaborn as sns
import matplotlib.lines as mlines
import matplotlib.ticker as mtick
import matplotlib.gridspec as grid_spec
from matplotlib.patches import Rectangle

import pandas as pd
#import statsmodels.api as sm

# import pyarrow.parquet as pq
# import pyarrow as pa


import os

import itertools
import collections

#---NLP packages--------------------
#import nltk
#from nltk import bigrams
#from nltk.corpus import stopwords
#from nltk.util import ngrams

#----process string-------
import string
import re

#---network visualization-----------
import re
import networkx as nx

# NanumGothic 폰트 설정
font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
if os.path.exists(font_path):
    font_name = fm.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_name)
else:
    print(f"Font file not found: {font_path}")

plt.rcParams['axes.unicode_minus'] = False

def cocurrence_network(start_date, end_date, all_data):
    data_for_date = []
    for data in all_data:
        if data['date'] >= start_date and data['date'] <= end_date:
            data_for_date.append(data)
    df = pd.DataFrame(data_for_date)
    df[['word1', 'word2']] = pd.DataFrame(df['keywords'].tolist(), index=df.index)
    df = df[['word1', 'word2', 'num']]
    df['num'] = df['num'].astype(int)
    
    G = nx.Graph()
    
    for _, row in df.iterrows():
        G.add_edge(row['word1'], row['word2'], weight=row[2])
        
    pos_kkl = nx.kamada_kawai_layout(G, scale=2)
    f, ax = plt.subplots(figsize=(16, 16))


    d = dict(nx.degree(G))
    edges = G.edges()
    weights = [G[u][v]['weight']/10 for u,v in edges]
    
    # 노드 가중치 합 계산
    node_weights = {
        node: sum(data['weight'] for _, _, data in G.edges(node, data=True))
        for node in G.nodes()
    }

    # 노드 크기 설정 (가중치 합에 비례)
    node_size = [weight * 100 for weight in node_weights.values()]

    nx.draw(G, pos_kkl, 
            with_labels=True, 
            #node_size=[v * 50 for v in d.values()],
            node_size=node_size,
            nodelist=d.keys(),  
            width=weights, 
            edge_color='grey', #node_color=list(df_skills_stats['core_number']), cmap="coolwarm_r", 
            alpha=0.9,
            font_family='NanumGothic',
            font_size=9,
        )

    # Set title
    ax.set_title('Word Co-occurrence Network', 
                fontdict={'fontsize': 26,
                'fontweight': 'bold',
                'color': 'salmon', 
                'verticalalignment': 'baseline',
                'horizontalalignment': 'center'}, 
                loc='center')
    # Set edge color
    plt.gca().collections[0].set_edgecolor("#000000")
    plt.savefig('./image/cocurrence.png')
    
    print("cocurrence network가 저장되었습니다.")