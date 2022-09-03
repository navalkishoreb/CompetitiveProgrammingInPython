# coding: utf-8
class Heap:
    def __init__(self, items):
        self.heap = [None]
        self.rank = dict()
        for item in items:
            self.push(item)

    def __len__(self):
        return len(self.heap) - 1

    def push(self, item):
        assert item not in self.rank
        i = len(self.heap)
        self.heap.append(item)
        self.rank[item]=i
        self.up(i)
        
    def up(self,index):
        item = self.heap[index]
        while index >1 and item < self.heap[index // 2]:
            self.heap[index] = self.heap[index // 2]
            self.rank[self.heap[index //2 ]] = index
            index = index // 2
        self.heap[index] = item
        self.rank[item] = index
        
    def pop(self):
        root = self.heap[1]
        del self.rank[root]
        last = self.heap.pop()
        if self:
            self.heap[1]= last
            self.rank[last] = 1
            self.down(1)
        return root

    def down(self, index):
        item = self.heap[index]
        count = len(self.heap)
        while True:
            left = 2* index
            right = left + 1
            
            if right < count and self.heap[right] < item and self.heap[right] < self.heap[left]:
                self.heap[index] = self.heap[right]
                self.rank[self.heap[right]]= index
                index = right
                
            elif left < count and self.heap[left] < item:
                self.heap[index] = self.heap[left]
                self.rank[self.heap[left]] = index
                index = left
                
            else:
                self.heap[index] = item
                self.rank[item] = index
                return
                
