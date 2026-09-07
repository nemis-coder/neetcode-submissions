class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack_polish = []
        for token in tokens:
            if token not in ['+','-','*','/']:
                stack_polish.append(token)
            else:
                operand_first = int(stack_polish.pop())
                operand_second = int(stack_polish.pop())
                new_val = None
                if token=='+':
                    new_val = operand_first + operand_second
                elif token=='-':
                    new_val = operand_second - operand_first
                elif token=='*':
                    new_val = operand_first * operand_second
                elif token=='/':
                    new_val = int((operand_second / operand_first))
                stack_polish.append(str(new_val))
        return int(stack_polish[-1])

