class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.hashtable = collections.defaultdict(set)
        self.array = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        valin = val not in self.hashtable
        self.hashtable[val].add(len(self.array))
        self.array.append(val)
        return valin 

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hashtable:
            return False
        else:
            if self.array[-1] == val:
                removeIdx = len(self.array) - 1
                self.hashtable[val].remove(removeIdx)
            else:
                # set pop remove arbitrary element
                removeIdx = self.hashtable[val].pop()
                self.array[removeIdx] = self.array[-1]
                self.hashtable[self.array[-1]].remove(len(self.array) - 1)
                self.hashtable[self.array[-1]].add(removeIdx)
            if len(self.hashtable[val]) == 0:
                del self.hashtable[val]
            del self.array[-1]
            return True
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        return random.choice(self.array)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
