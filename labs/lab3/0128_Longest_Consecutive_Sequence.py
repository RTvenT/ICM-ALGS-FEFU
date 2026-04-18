class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        d = {}
        max_len = 0
        
        for n in nums:
            if n not in d:
                left = d.get(n - 1, 0)
                right = d.get(n + 1, 0)
                
                current_sum = left + right + 1
                max_len = max(max_len, current_sum)
                
                d[n] = current_sum
                
                d[n - left] = current_sum
                d[n + right] = current_sum
                
        return max_len
            
            
def main():
    solve = Solution()
    nums = [0,3,7,2,5,8,4,6,0,1]

    print(solve.longestConsecutive(nums))
    
        
    
if __name__ == '__main__':
    main()
                