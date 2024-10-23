# https://leetcode.com/problems/valid-parentheses/description/

# Approach:
# if it's opening bracket, push to stack
# if it's closing bracket, pop from stack and check if it's matching with the respective popped bracket.
# if stack is empty, return True at the end else return False.

# Time O(N) | Space O(N)
def isvalidparenthesis(s):
    stack = []
    corrosponding_bracket = {")":"(", "}":"{", "]":"["}
    for bracket in s:
        if bracket in "({[":
            stack.append(bracket)
        else:
            if len(stack) == 0: return False
            popped_bracket = stack.pop()
            if corrosponding_bracket[bracket] != popped_bracket:
                return False
    return len(stack) == 0

# s = "()[]{}"
# s = "(]"
# s = "([])"
# s = "[{}"
# s = ""
s = "]"
print(isvalidparenthesis(s))