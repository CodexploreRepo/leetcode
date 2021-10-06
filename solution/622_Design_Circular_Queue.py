class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None]*k
        self.cur_size = 0
        self.max_size = k
        self.head = self.tail = -1
        
    def enQueue(self, value: int) -> bool:
        #Enqueue: To take care of the tail 
        if self.isFull():
            return False #return False as cannot enqueue
        else:
            if self.isEmpty(): #to check if the queue is empty
                self.head = self.tail = 0 #increse both Head & Tail to the 0 pos
            else:
                #if queue is not empty, just increase self.tail by 1
                #if self.tail == self.max_size, so (% self.max_size) to circular back to 0 pos
                self.tail = (self.tail + 1)%self.max_size
            #store the "value" in tail cell
            self.queue[self.tail] = value
            #update the cur_size by 1
            self.cur_size += 1
            return True #return True if can enqueue


    def deQueue(self) -> bool:
        #Dequeue: To take care of the head
        if self.isEmpty():
            return False
        else:
            if self.head == self.tail: #in case, only left with 1 element
                self.head = self.tail = -1 #init both head, tail to -1
            else:
                self.queue[self.head] = None #change the value @ head to None
                self.head = (self.head + 1)%self.max_size #increase head by 1
                #if self.head == self.max_size, so (% self.max_size) to circular head back to 0 pos
            self.cur_size -= 1
            return True
            
    def Front(self) -> int:
        return self.queue[self.head] if self.head >= 0 else -1

    def Rear(self) -> int:
        return self.queue[self.tail] if self.tail >= 0 else -1

    def isEmpty(self) -> bool:
        return self.cur_size == 0
        

    def isFull(self) -> bool:
        return self.cur_size == self.max_size
