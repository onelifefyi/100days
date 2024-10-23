# https://leetcode.com/problems/implement-queue-using-stacks/
# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
class MyQueue:

    def __init__(self):
        self.left_stack = []
        self.right_stack = []

    def push(self, x: int) -> None:
        self.left_stack.append(x)

    def pop(self) -> int:
        while self.left_stack:
            self.right_stack.append(self.left_stack.pop())
        result = self.right_stack.pop()
        while self.right_stack:
            self.left_stack.append(self.right_stack.pop())
        return result


    def peek(self) -> int:
        return self.left_stack[0]

    def empty(self) -> bool:
        return len(self.left_stack) == 0


obj = MyQueue()
obj.push(5)
obj.push(10)
obj.push(12)
param_2 = obj.pop()
param_3 = obj.peek()
param_2 = obj.pop()
param_2 = obj.pop()
param_4 = obj.empty()
print(param_2, param_3, param_4)