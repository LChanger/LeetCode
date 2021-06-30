class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        #贪心
        cur = 0
        start = 0
        res = []
        for i in range(len(words)):
            cur+=len(words[i])+1#记录当前的宽度
            if cur-1>maxWidth:
                space_cnt=i-1-start
                if space_cnt==0:
                    res.append(words[i-1].ljust(maxWidth,' '))
                else:
                    total_space=maxWidth-(cur-1-len(words[i])-1)+space_cnt
                    small_long=total_space//space_cnt
                    big_cnt=total_space%space_cnt
                    small_cnt=space_cnt-big_cnt
                    small_space=' '*small_long
                    big_space=small_space+' '
                    if big_cnt>0:
                        res.append(big_space.join(words[start:start+big_cnt+1])+small_space+small_space.join(words[start+big_cnt+1:i]))
                    else:
                        res.append(small_space.join(words[start:start+small_cnt+1]))
                cur=len(words[i])+1
                start=i
        res.append(' '.join(words[start:]).ljust(maxWidth,' '))
        return res
words=["What","must","be","acknowledgment","shall","be"]
maxWidth=16
print(Solution().fullJustify(words,maxWidth))