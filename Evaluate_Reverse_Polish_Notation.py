import typing
import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda x, y: int(x / y)  # Ensure truncation toward zero
        }
        
        stack = []  # Stack for storing intermediate results
        
        for token in tokens:
            if token in ops:  
                b = stack.pop()  
                a = stack.pop()  
                stack.append(ops[token](a, b))  # Apply operation and push result
            else:  
                stack.append(int(token))  # Push the integer value onto the stack
        
        return stack.pop()  