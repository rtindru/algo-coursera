import math
import sys

class MinHeap(object):
    def __str__(self):
        return 'Min Heap'
    
    def __init__(self, array):
        if not isinstance(array, list):
            raise ValueError('Initialize the heap with an list')
        self.count = len(array)
        self.heap = [None]
        self.heap.extend(array)
        self.heapify(1)

    def _swap(self, a, b):
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp

    def _bubble_down(self, index):
        lindex, rindex = index << 1, (index << 1) + 1
        lchild = self.heap[lindex] if lindex <= self.count else sys.maxint
        rchild = self.heap[rindex] if rindex <= self.count else sys.maxint
        min_child, min_index = (lchild, lindex,) if lchild < rchild else (rchild, rindex,)
        while self.heap[index] > min_child:
            self._swap(index, min_index)
            self._bubble_down( min_index)

    def _bubble_up(self, index):
        parent_index = index/2
        parent = self.heap[parent_index]
        while index != 0 and self.heap[index] < parent:
            self._swap(index, parent_index)
            self._bubble_up(parent_index)
        return

    def heapify(self, index):
        lindex, rindex = index << 1, (index << 1) + 1
        print self.count, index, lindex, rindex, self.heap
        lchild = self.heap[lindex] if lindex <= self.count else None
        rchild = self.heap[rindex] if rindex <= self.count else None
        if lchild and lchild < self.heap[index]:
            largest = lindex
        else:
            largest = index
        if rchild and rchild < self.heap[largest]:
            largest = rindex
        if self.heap[largest] != self.heap[index]:
            self._swap(index, largest)
            self.heapify(largest)
       
    def insert(self, item):
        self.heap.append(item)
        self.count += 1 
        self._bubble_up(self.count)

    def pop_min(self):
        res = self.heap[1]
        self.heap[1] = self.heap[self.count]
        del(self.heap[self.count])
        self.count -= 1
        self._bubble_down(1) 
        return res

    def show_min(self):
        return self.heap[1]
