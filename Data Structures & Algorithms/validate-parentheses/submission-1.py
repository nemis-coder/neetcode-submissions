class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_chars = {'(':1, '[':1,'{':1}
        for curr_c in s:
            if curr_c in open_chars:
                stack.append(curr_c)
            else:
                if curr_c == ')' and len(stack)>0:
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        return False
                elif curr_c == ']' and len(stack)>0:
                    if stack[-1]=='[':
                        stack.pop()
                    else:
                        return False
                else:
                    if len(stack)>0 and stack[-1]=='{':
                        stack.pop()
                    else:
                        return False
        if len(stack)>0:
            return False
        return True
