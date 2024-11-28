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

        removes the elem on the top of the stack
        """
        

    def top(self) -> int:
        """
        :rtype: int

        gets the top elem of the stack
        """
        

    def getMin(self) -> int:
        """
        :rtype: int

        retrieves the min elem in the stack
        """

def test():
    test_stack = MinStack()
    test_stack.push(3)
    print(test_stack.stack)



if __name__ == "__main__":
    test()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()