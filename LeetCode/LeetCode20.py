class Solution2:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stackbraket=[]
        for st in s:
        	if st in {'(','{','['}:stackbraket.append(st)
        	elif st ==')':
        		index=len(stackbraket)-1
        		if index>=0 and stackbraket[index]=='(':stackbraket.pop(index)
        		else:return False
        	elif st =='}':
        		index=len(stackbraket)-1
        		if index>=0 and stackbraket[index]=='{':stackbraket.pop(index)
        		else:return False
        	elif st ==']':
        		index=len(stackbraket)-1
        		if index>=0 and stackbraket[index]=='[':stackbraket.pop(index)
        		else:return False
        	else:return False
        if len(stackbraket):return False
        return True
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stackbraket=[]
        data={'(':')','{':'}','[':']'}
        for st in s:
        	if st in data.keys():stackbraket.append(st)
        	elif st in data.values():   
        		index=len(stackbraket)-1
        		if index>=0 and data.get(stackbraket[index])==st:stackbraket.pop(index)
        		else:return False
        if len(stackbraket):return False
        return True