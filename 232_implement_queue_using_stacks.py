# https://leetcode.com/problems/implement-queue-using-stacks/description/
# easy

# leftmost is front of the queue


class MyQueue:

    def __init__(self):
        self.queue = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None

        Pushes element x to the back of the queue
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        :rtype: int

        Removes the element from the front of the queue and returns it
        """
        front_el = self.queue[0]
        self.queue.remove(front_el)
        return front_el
        

    def peek(self) -> int:
        """
        :rtype: int

        Returns the element at the front of the queue - the left one
        """
        return self.queue[0]
        

    def empty(self) -> bool:
        """
        :rtype: bool

        Returns true if the queue is empty, false otherwise
        """
        return self.queue == []


def test():
    test_queue = MyQueue()

    test_queue.push(1)
    test_queue.push(2)
    print(test_queue.queue)

    assert test_queue.peek() == 1
    assert test_queue.pop() == 1
    print(test_queue.queue)

    assert test_queue.empty() == False


    



if __name__ == "__main__":
    test()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()