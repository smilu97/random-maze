import numpy as np

class UnionFind:
    def __init__(self, sz):
        self.sz = sz
        self.parent = np.arange(sz)
    
    def same(self, a, b):
        return self.root(a) == self.root(b)
    
    def merge(self, a, b):
        a = self.root(a)
        b = self.root(b)
        if a == b: return False
        self.parent[b] = a
        return True
    
    def root(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]