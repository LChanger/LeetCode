class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.index=defaultdict(set)
        self.nums=[]

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val not in self.index:
            self.nums.append(val)
            self.index[val].add(len(self.nums)-1)
            return True
        self.nums.append(val)
        self.index[val].add(len(self.nums)-1)
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.index:
            return False
        last_val=self.nums[-1]
        if last_val==val:
            self.index[val].remove(len(self.nums)-1)
        else:
            #更新最后一个位置的数的位置记录
            to_delete_index=self.index[val].pop()
            #交换位置
            self.nums[to_delete_index],self.nums[-1]=self.nums[-1],self.nums[to_delete_index]
            self.index[last_val].remove(len(self.nums)-1)
            self.index[last_val].add(to_delete_index)
        self.nums.pop()
        if not self.index[val]:
            self.index.pop(val)
        return True
    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        if not self.nums:return []
        import random
        index=random.randint(0,len(self.nums)-1)
        return self.nums[index]
obj = RandomizedCollection()
obj.insert(1)
param_1 = obj.insert(1)
param_2 = obj.remove(1)
param_3 = obj.getRandom()
