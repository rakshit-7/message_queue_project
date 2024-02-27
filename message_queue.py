from queue import PriorityQueue

class MessageQueue:
    def __init__(self):
        self.queue = PriorityQueue()

    def enqueue_message(self, message, priority):
        self.queue.put((priority, message))

    def dequeue_message(self):
        return self.queue.get()[1]

    def peek_message(self):
        if not self.queue.empty():
            return self.queue.queue[0][1]
        return None

    def is_empty(self):
        return self.queue.empty()
