class Solution:
    def __G(self, k, piles, h) -> bool:
        if k == 0:
            return False
        
        for pile in piles:
            h -=  -(pile // -k)
            
            if h < 0:
                return False
            
        if h >= 0:
            return True
        
    
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 0
        r = max(piles)
        k = float("inf")
        
        while l <= r:
            mid = (l + r) // 2
            
            if self.__G(mid, piles, h):
                k = min(k, mid)
                r = mid-1
            else:
                l = mid+1
                
        return k
    
    
def main():
    solve = Solution()
    piles = [3,6,7,11]
    h = 8
    
    print(solve.minEatingSpeed(piles, h))
    
        
    
if __name__ == '__main__':
    main()
               