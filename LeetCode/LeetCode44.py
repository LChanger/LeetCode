class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i=j=0
        j_star=-1#记录在p中上一个*的位置
        i_star = -1#记录在s中上一个*匹配到的位置  注意 j_star和i_star 一定是同步更新的
        while i<len(s):
            #r若相等或者 ？ 则各向前走一步
            if s[i:i+1]==p[j:j+1] or "?"in p[j:j+1]:
                i+=1
                j+=1#s p 各走一步
                continue
            # * 首先匹配为空， 分别记录 *在s和p中的位置 j往前走一步 i不变
            if "*" in p[j:j+1]:
                j_star = j
                i_star=i-1
                j+=1 # * p匹配空字符
                continue
            # 到了这一步说明，不相等 p[j]也不为* 所以回退，回到上次*吞下的位置，再往前吞一个
            if i_star>-1:#回溯   * 吞一个字符
                i=i_star+2
                i_star+=1
                j=j_star+1
                continue
            # 到了这一步说明，只有一种情况，即P[0]是* 但 s[0]不是，且此时* 从未匹配过，所以 j回到上一个的位置，i前进两个位置，即吞下一个i
            if j_star>-1:# * 把上次吞的下一个位置给吞了
                j=j_star
                i = i_star + 2
                i_star += 1
                continue
            return False
        while j<len(p):
            if p[j]!="*":return False
            j+=1
        return True
c="hi"
x="*?"
t=Solution()
print (t.isMatch(c,x))

#参考 https://www.cnblogs.com/grandyang/p/4401196.html