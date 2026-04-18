class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}
        
        for num in nums:
            if d.get(num) is None:
                d[num] = 0
            else:
                d[num] += 1
                
        print(d)
                
        return sorted(d, key=d.get, reverse=True)[:k]
    
    
def main():
    solve = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    
    print(solve.topKFrequent(nums, k))
    
        
    
if __name__ == '__main__':
    main()
                