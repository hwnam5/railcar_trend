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

#plt.rcParams['font.family'] = 'NanumGothic'
#plt.rcParams['axes.unicode_minus'] = False

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

    nx.draw(G, pos_kkl, 
            with_labels=True, 
            node_size=[v * 100 for v in d.values()],
            nodelist=d.keys(),  
            width=weights, 
            edge_color='grey', #node_color=list(df_skills_stats['core_number']), cmap="coolwarm_r", 
            alpha=0.9,
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