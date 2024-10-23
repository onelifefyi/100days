# https://leetcode.com/problems/backspace-string-compare/
# Appraoch:
# Create a stack and keep pushing one character at a time.
# If it's hash, pop() from the stack.
# Create another stack and do the same for t.
# Compare the two stacks.
# Time O(n) | Space O(n)
def backspaceCompare(s, t):
    s_stack = []
    for ch in s:
        if ch == "#":
            s_stack.pop() if s_stack else None
        else:
            s_stack.append(ch)

    t_stack = []
    for ch in t:
        if ch == "#":
            t_stack.pop() if t_stack else None
        else:
            t_stack.append(ch)
    return s_stack == t_stack

# Test Cases
print(backspaceCompare("ab#c", "ad#c"))
print(backspaceCompare("ab##", "c#d#"))
print(backspaceCompare("a#c", "b"))
