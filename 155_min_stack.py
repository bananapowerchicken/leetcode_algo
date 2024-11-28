# https://leetcode.com/problems/min-stack/description/
# medium
# train stack and class methods and attributes


# do I need checking for type? i can process only integers
class MinStack:

    def __init__(self):
        self.stack = [] # just a list as an instance attribute
        

    def push(self, val):
        """
        :type val: int
        :rtype: None

        pushes the elem val onto the stack
        """
        self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None

        removes the elem on the top of the stack(last of list)
        """
        self.stack.pop(-1)
        

    def top(self) -> int:
        """
        :rtype: int

        gets the top elem of the stack(last of list)
        """
        return self.stack[-1] # returns the last element of the list
        

    def getMin(self) -> int:
        """
        :rtype: int

        retrieves the min elem in the stack
        """
        return min(self.stack)

def test():
    test_stack = MinStack()
    test_stack.push(-2)
    test_stack.push(0)
    test_stack.push(-3)
    assert test_stack.getMin() == -3
    print(test_stack.stack)

    test_stack.pop()
    print(test_stack.stack)
    assert test_stack.top() == 0
    assert test_stack.getMin() == -2

    



if __name__ == "__main__":
    test()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()