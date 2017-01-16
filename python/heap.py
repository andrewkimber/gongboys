class Heap:
    def __init__(self):
        self.queue = [0]
        self.currentSize = 0

    def __str__(self):
        return str(self.queue)

    def push_up(self, i):
        while i // 2 > 0:
            if self.queue[i] < self.queue[i / 2]:
                temp = self.queue[i / 2]
                self.queue[i // 2] = self.queue[i]
                self.queue[i] = temp
            i //= 2

    def insert(self, key):
        self.queue.append(key)
        self.currentSize += 1
        self.push_up(self.currentSize)

    def push_down(self, i):
        while i * 2 <= self.currentSize:
            mc = self.min_child(i)
            if self.queue[i] > self.queue[mc]:
                temp = self.queue[i]
                self.queue[i] = self.queue[mc]
                self.queue[mc] = temp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.queue[2 * i] < self.queue[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1

    def pop_min(self):
        retval = self.queue[1]
        self.queue[1] = self.queue[self.currentSize]
        self.currentSize -= 1
        self.queue.pop()
        self.push_down(1)
        return retval


heap = Heap()

heap.insert(1)
heap.insert(5)
heap.insert(7)
heap.insert(2)
heap.insert(4)
heap.insert(6)
heap.pop_min()
heap.pop_min()
heap.insert(10)
heap.insert(3)

print heap
