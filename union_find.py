import numpy as np

class UnionFind:
    def __init__(self, sz):
        self.sz = sz
        self.parent = np.arange(sz) # Parent node index in tree
    
    def same(self, a, b):
        return self.root(a) == self.root(b)
    
    def merge(self, a, b):
        '''
        @return boolean False, if two nodes have been already connected
        '''
        a = self.root(a) # parent[a] = a
        b = self.root(b) # parent[b] = b
        if a == b: return False
        self.parent[b] = a # Connect two trees
        return True
    
    def root(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]