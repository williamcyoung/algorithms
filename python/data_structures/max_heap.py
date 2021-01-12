class Heap():
    def __init__(self, array):
        self.length = len(array)
        self.heap_size = 0

    def parent(self, i):
        return i//2

    def left(self, i):
        return 2*i

    def right(self, i):
        return (2*i)+1

    def maxHeapify(self, array, i):
        l = self.left(i)
        r = self.right(i)