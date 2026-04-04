class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for p1 in s:
            if p1 in d.keys(): 
                stack.append(p1)
            elif stack:
                p2 = stack.pop()
                if p1 != d[p2]:
                    return False
            else:
                return False
                
        return not bool(len(stack))