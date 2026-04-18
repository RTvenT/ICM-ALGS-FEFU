class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        
        return -1
        
    
def main():
    solve = Solution()
    nums = [8, 5, 6, 7]
    target = 5
    
    print(solve.search(nums, target))
    
        
    
if __name__ == '__main__':
    main()
            