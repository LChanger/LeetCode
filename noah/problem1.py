class Solution:
    def __init__(self,word_set,window_size=None):
        #load dictionary and set window_size
        self.words_dict=word_set
        self.window_size=1
        if window_size:
            self.window_size=window_size
        else:
            for w in word_set:
                self.window_size=max(self.window_size,len(w))
    #正向最大匹配
    def fmmCut(self,sentence):
        len_sentence=len(sentence)
        index=0
        words=[] 
        while index<len_sentence:  
            match=False #标志是否匹配成功，未匹配成功则按字处理
            for i in range(self.window_size, 0, -1):
                sub_str=sentence[index: index+i]
                if sub_str in self.words_dict:
                    match=True
                    words.append(sub_str)
                    index+=i
                    break
            if not match:
                words.append(sentence[index])
                index+=1
        return words
    #反向最大匹配
    def rmmCut(self,sentence):
        len_sentence = len(sentence)
        index=len_sentence
        words=[] 
        while index>0:
            match=False
            for i in range(self.window_size, 0, -1):
                sub_str=sentence[index-i: index]
                if sub_str in self.words_dict:
                    match=True
                    words.append(sub_str)
                    index-=i
                    break
            if not match:
                words.append(sentence[index-1])
                index-=1
        return words[::-1] #倒序
    # 双向最大匹配
    def bmmCut(self, sentence):
        words_FMM = self.fmmCut(sentence)
        words_RMM = self.rmmCut(sentence)
        # 如果正向和反向结果一样，返回任意一个
        if words_FMM==words_RMM:
            return words_FMM
        # 单字词个数
        fmm_single_word=0
        rmm_single_word=0
        # 总词数
        fmm_total=len(words_FMM)
        rmm_total=len(words_RMM)
        # 非字典词数
        fmm_oov=0
        rmm_oov=0
        # 三者的总得分
        fmm_score=0
        rmm_score=0
        # 统计单字词数和非字典词数
        for word in words_FMM:
            if len(word)==1:
                fmm_single_word+=1
            if word not in self.dictionary:
                fmm_oov+=1
        for word in words_RMM:
            if len(word)==1:
                rmm_single_word+=1
            if word not in self.dictionary:
                rmm_oov+=1

        fmm_score=fmm_oov+fmm_total+fmm_single_word
        rmm_score=rmm_oov+rmm_total+rmm_single_word
        # 返回单字数、非字典词、总词数少的那一个
        if fmm_score<rmm_score:
            return words_FMM
        return words_RMM
    
word_set={"我","爱","北京","天安门","故宫","飞机","哈尔滨工业大学"}
text="我爱哈尔滨工业大学"
window_size=None
s=Solution(word_set,window_size)
print(s.bmmCut(text))