class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height)-1
        area = 0
        
        while l != r:
            a = r - l
            b = min(height[l], height[r])
            area = max(area, a*b)
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
                
        return area
            
        

def main():
    solve = Solution()

    tests = [
        {'height': [1,8,6,2,5,4,8,3,7]},
        {'height': [1,1]}
    ]
                
    for test in tests:
        print(solve.maxArea(test['height']))
        

if __name__ == '__main__':
    main()
           