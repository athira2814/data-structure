class Queue:
    def __init__(self,n):
        self.maxsize = n
        self.front = 0
        self.rear = 0
        self.queue = []
    
    def enqueue(self,data):
        if (self.rear >= self.maxsize):
            print("Queue is full")
        else :
            self.front+=1
            self.rear+=1
            self.queue.append(data)
            print(self.queue)

    def dequeue(self):
        if (self.queue == []):
            print("Queue is empty")
        else:
            self.queue.pop(0)
            self.front+=1
            print(self.queue)

    def display(self):
        return self.queue

if __name__ == "__main__" :
    q= Queue(5)
    while (True):

        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Quit")
        c = input("Enter your choice")

        if(c == "1"):
            data = int(input("Enter an element :"))
            q.enqueue(data)
        elif (c == "2"):
            q.dequeue()
        elif (c == "3"):
            print(q.display())
        elif (c == "4"):
            print("Thank You!!")
            break
        else:
            print("wrong choice")
