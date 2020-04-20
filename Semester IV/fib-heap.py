class Heap:
    def __init__(self):
        self.min = None
        self.n = 0
        self.rootList = []
    
    def insert(self, x):
        x.degree = 0
        x.parent = None
        x.child = None
        x.mark = False
        if self.min is None:
            self.min = x
        else:
            if x.key < self.min.key:
                self.min = x
        self.n += 1
        self.rootList.append(x)


class Node:
    def __init__(self, key):
        self.parent = None
        self.child = None
        self.right = None
        self.left = None
        self.mark = False
        self.degree = None
        self.key = key
    
    def setLeft(self, x):
        if self.__left is not None:
            self.__left = x
            
    
    def setRight(self, x):
        if self.__right is not None: 
            self.__right = x

def heapUnion(h1, h2):
    H = Heap()
    H.min = h1.min
    H.rootList.append(h1.rootList)
    H.rootList.append(h2.rootList)
    if h1.min is None or \
            (h2.min is not None and h2.min.key < h1.min.key):
        H.min = h2.min
    H.n = h1.n + h2.n
    return H

