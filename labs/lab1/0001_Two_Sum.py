class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = dict()
        
        for i, n in enumerate(nums):
            second = d.get(target - n)
            if second is not None:
                return [i, second]
            d[n] = i
            
            
            
def main():
    solve = Solution()

    tests = [
        {'nums': [2,7,11,15], 'target': 9},
        {'nums': [3,2,4], 'target': 6},
        {'nums': [3, 3], 'target': 6}
    ]
                
    for test in tests:
        print(solve.twoSum(test['nums'], test['target']))
        

if __name__ == '__main__':
    main()