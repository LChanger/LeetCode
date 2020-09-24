#思路：归并排序
#T:o(nlogN)
#S:O(1)
class Solution0:
    def countSmaller(self, nums):
        res=[0 for i in range(len(nums))]
        index=[i for i in range(len(nums))]
        tempStorage=[0]*len(nums)#临时安置索引数组
        def sort(start1,end1,start2,end2):
            p1=start1
            p2=start2
            pt=start1
            while p1<=end1 and p2<=end2:
                if nums[index[p1]]<=nums[index[p2]]:
                    tempStorage[pt]=index[p1]
                    res[index[p1]]+=p2-start2
                    p1+=1
                    pt+=1
                else:
                    tempStorage[pt]=index[p2]
                    p2+=1
                    pt+=1
            if p2<=end2:tempStorage[pt:end2+1]=index[p2:end2+1]
            else:
                while p1<=end1:
                    tempStorage[pt]=index[p1]
                    res[index[p1]]+=end2-start2+1
                    pt+=1
                    p1+=1
            index[start1:end1+1]=tempStorage[start1:end1+1]
            index[start2:end2+1]=tempStorage[start2:end2+1]
        def merge(start,end):
            if start==end:return
            mid=(start+end)//2
            merge(start,mid)
            merge(mid+1,end)
            sort(start,mid,mid+1,end)
        merge(0,len(nums)-1)
        return res

#对位置进行归并
#思路：归并排序
#T:o(nlogN)
#S:O(1)
class Solution:
    def countSmaller(self, nums):
        if not nums:return []
        res=[0 for i in range(len(nums))]
        index=[i for i in range(len(nums))]#存储num[i]元素的位置
        tempStorage=[0]*len(nums)#临时安置索引数组
        def merge_sort(start1,end1,start2,end2):
            p1=start1
            p2=start2
            p=start1
            while p1<=end1 and p2<=end2:
                if nums[index[p1]]<=nums[index[p2]]:
                    tempStorage[p]=index[p1]
                    res[index[p1]]+=p2-start2
                    p1+=1
                else:
                    tempStorage[p]=index[p2]
                    p2+=1
                p+=1
            if p1<=end1:
                tempStorage[p:end2+1]=index[p1:end1+1]
                for i in range(p1,end1+1):
                    res[index[i]]+=p2-start2
            else:
                tempStorage[p:end2+1]=index[p2:end2+1]
            index[start1:end2+1]=tempStorage[start1:end2+1]
        def merge(start,end):
            if start==end:return
            mid=(start+end)//2
            merge(start,mid)
            merge(mid+1,end)
            merge_sort(start,mid,mid+1,end)
        merge(0,len(nums)-1)
        return res
nums=[5,2,6,1]
s = Solution()
print(s.countSmaller(nums))