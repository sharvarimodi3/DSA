class PriorityQueue:    
    def __init__(self):
        self.queue = []

    def enqueue(self, pid, name, priority):
        self.queue.append([pid, name, priority])
        self.queue.sort(key=lambda x: x[2])
        print("Process added successfully")
    def dequeue(self):
        if not self.queue:
            print("Queue is empty")
        else:
            process = self.queue.pop(0)
            print("Executed Process:", process)
    def display_next(self):
        if not self.queue:
            print("Queue is empty")
        else:
            print("Next Process:", self.queue[0])
    def display_all(self):
        if not self.queue:
            print("Queue is empty")
        else:
            print("Processes in priority order:")
            for p in self.queue:
                print(p)
    def count(self):
        print("Total pending processes:", len(self.queue))
# Main program
pq = PriorityQueue()
pq.enqueue(101, "System Process", 1)
pq.enqueue(102, "Browser", 2)
pq.enqueue(103, "Background Task", 3)
pq.enqueue(104, "File Download", 4)
pq.display_all()
pq.display_next()
pq.dequeue()
pq.display_all()
pq.count()