 # Definition for singly-linked list.
s ="aaa"
words = ["aa","aa"]

# 思路，纸面上画一下每步的步骤
class Solution:
    def findSubstring(self, s:str, words):
        if s == '' or len(words) == 0: return []
        cnt = len(words)
        wl = len(words[0])
        dic1 = {}  # 记录words中的word
        res = []  # 返回结果
        for word in words:
            if word not in dic1:
                dic1[word] = 1
            else:
                dic1[word] += 1

        # 向字典中添加元素
        def addic(dic, key):
            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1
            return dic

        for i in range(wl):
            left = i  # 记录左轴
            j = i
            dic2 = {}
            matchnum = 0  # 匹配成功的个数
            while j <= len(s) - wl:
                temp = s[j:j + wl]
                if temp in dic1:
                    addic(dic2,temp)
                    matchnum += 1  # 匹配个数加1
                    if dic2[temp] > dic1[temp]:
                        while dic2[temp] > dic1[temp]:
                            dic2[s[left:left + wl]] -= 1
                            left += wl
                            matchnum -= 1
                    if matchnum == cnt: res.append(left)
                else:
                    left = j + wl
                    dic2.clear()
                    matchnum = 0
                j += wl
        return res

#参考思路 https://www.cnblogs.com/grandyang/p/4521224.html
t = Solution()
t.findSubstring(s, words)
