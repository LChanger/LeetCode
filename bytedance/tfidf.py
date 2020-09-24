texts=["我喜欢动物园","我更喜欢植物园","海豚","鲸鱼"]
def tf_idf(texts):
    import jieba
    import math
    words=set()
    for text in texts:
        word=jieba.lcut(text)
        words=words|set(word)
    #tf 总次数/总词数，idf是 log(文本总数/包含该词的文档数+1)
    res=[]
    tf_dict={}
    idf={}
    total=0
    for text in texts:
        text=jieba.lcut(text)
        visited=set()
        for word in text:
            tf_dict[word]=tf_dict.get(word,0)+1
            total+=1
            if word not in visited:
                idf[word]=idf.get(word,0)+1
                visited.add(word)
    tf_idf={}
    print(tf_dict)
    print(idf)
    for k in tf_dict:
        tf_idf[k]=tf_dict[k]/total*math.log(len(texts)/(idf.get(k,0)+1))
        print(k)
        print(tf_idf[k])
tf_idf(texts)
