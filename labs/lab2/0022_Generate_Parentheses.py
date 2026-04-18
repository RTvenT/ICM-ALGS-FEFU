class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        stack = [("", 0, 0)]

        while stack:
            current, open_count, close_count = stack.pop()

            if len(current) == 2 * n:
                result.append(current)
                continue
            
            if open_count < n:
                stack.append((current + "(", open_count + 1, close_count))
            
            if close_count < open_count:
                stack.append((current + ")", open_count, close_count + 1))
                
            print(stack)
                

        return result
    
    
def main():
    solve = Solution()

    n = 3
                
    print(solve.generateParenthesis(n))
        
    
if __name__ == '__main__':
    main()