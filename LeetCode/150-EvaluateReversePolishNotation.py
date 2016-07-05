"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""


# TODO
# Works well on Mac, but can't run on the leetcode
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        token = ['+', '-', '*', '/']
        stack = []
        for str in tokens:
            if str in token:
                j = int(stack.pop())
                k = int(stack.pop())
                if str == '+':
                    stack.append(j + k)
                elif str == '-':
                    stack.append(k - j)
                elif str == '*':
                    stack.append(j * k)
                elif str == '/':
                    stack.append(k / j)
            else:
                stack.append(str)
        return int(stack.pop())

# s = Solution()
# print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
