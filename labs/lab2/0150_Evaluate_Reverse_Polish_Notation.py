class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operands = ['+', '-', '*', '/']
        stack = []

        for t in tokens:
            if t not in operands:
                stack.append(t)
            elif stack:
                right = str(stack.pop())
                left = str(stack.pop())
    
                stack.append(int(eval(left + t + right)))
                
        return int(stack[0])
        
        
def main():
    solve = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    
    print(solve.evalRPN(tokens))
    
        
    
if __name__ == '__main__':
    main()
                
                
