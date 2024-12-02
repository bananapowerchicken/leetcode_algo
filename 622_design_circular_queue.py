# https://leetcode.com/problems/design-circular-queue/description/
# medium

class MyCircularQueue():

    def __init__(self, k):
        """
        :type k: int

        Initializes the object with the size of the queue to be k
        """
        self.k = k
        self.queue = [] * k
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool

        Inserts an element into the circular queue. Return true if the operation is successful.
        Inserts to the right
        """
        if self.queue:
            self.queue.append(value)
            return True
        else:
            return False
        

    def deQueue(self):
        """
        :rtype: bool

        Deletes an element from the circular queue. Return true if the operation is successful.
        Suppose that the left element
        """
        if len(self.queue) > 0:
            self.queue.pop(0)
            return True
        else:
            return False

    def Front(self):
        """
        :rtype: int

         Gets the front item from the queue. If the queue is empty, return -1.
         left
        """
        return self.queue[0] if self.queue else -1

    def Rear(self):
        """
        :rtype: int

        Gets the last item from the queue. If the queue is empty, return -1
        right
        """
        return self.queue[-1] if self.queue else -1
        

    def isEmpty(self):
        """
        :rtype: bool

        Checks whether the circular queue is empty or not.
        """
        return len(self.queue) == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.queue) == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(3)
# param_1 = obj.enQueue(1)
# param_2 = obj.enQueue(2)
# param_3 = obj.enQueue(3)
# param_4 = obj.enQueue(4)
# param_5 = obj.Rear()
# param_6 = obj.isFull()
# param_7 = obj.deQueue()
# param_8 = obj.enQueue(4)
# param_9 = obj.Rear()

obj = MyCircularQueue(6)
param_01 = obj.enQueue(6)
param_02 = obj.Rear()
param_03 = obj.Rear()
param_04 = obj.deQueue()
param_05 = obj.enQueue(5)
param_06 = obj.Rear()
param_07 = obj.deQueue()
param_08 = obj.Front()
param_09 = obj.deQueue()
param_10 = obj.deQueue()
param_11 = obj.deQueue()
print('finish')