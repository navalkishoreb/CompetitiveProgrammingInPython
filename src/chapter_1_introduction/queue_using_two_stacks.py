# coding: utf-8
class Queue:
    def __init__(self):
        self.in_stack = list()
        self.out_stack = list()
        
    def __len__(self):
        return len(self.in_stack)+len(self.out_stack)
        
    def push(self,item):
        self.in_stack.append(item)
        
    def pop(self):
        if self.in_stack:
            self.out_stack.extend(self.in_stack[::-1])
            self.in_stack = list()
        if self.out_stack:
            return self.out_stack.pop()
        raise Exception("Nothing to pop")
        
