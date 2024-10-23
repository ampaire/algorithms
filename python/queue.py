class Queue:
    def _init_(self):
        self.queue = []

    def enqueue(self,element):
        self.queue.append(element)

    def dequeue(self):
        if self.is_empty():
            print("Cannot dequeue element from an empty Queue")
        else:
            self.queue.pop[0]
    