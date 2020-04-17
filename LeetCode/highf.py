# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
from gensim import corpora
from gensim import models
import json
import jieba


# %%
inp_path = 'E:\\Learning\\securityAI\\adversarial_wordCut50.txt'


# %%
with open(inp_path, 'r',encoding='UTF-8') as f:
    inp_lines = json.load(f)


# %%
origin_text = [item[0] for item in inp_lines['text']]
adversarial_text = [item[1] for item in inp_lines['text']]


# %%
# adversarial_text


# %%
# 结巴获取高频词


# %%
def gaoping(text):
    # txt = open('gaopin.txt','r').read()
    words = jieba.lcut(' '.join(text))
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word,0) + 1
    items = list(counts.items())
    items.sort(key=lambda x : x[1],reverse=True)
    #items.sort(reverse = True)
    for i in range(30):
        word ,count =items[i]
        print(word,count)


# %%
gaoping(adversarial_text)


# %%



# %%
inp_lines = origin_text
word_list = [jieba.lcut(line) for line in inp_lines]
dictionary = corpora.Dictionary(word_list)
new_corpus = [dictionary.doc2bow(text) for text in word_list]


# %%
new_corpus

