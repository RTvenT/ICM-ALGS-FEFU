class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
       
        digit = lambda x: 48 <= ord(x) <= 57
        uppercase = lambda x: 65 <= ord(x) <= 90
        lowercase = lambda x: 97 <= ord(x) <= 122

       
        while l <= r:
            lc = s[l]
            rc = s[r]
                
            if not (digit(lc) or uppercase(lc) or lowercase(lc)):      
                l += 1
                continue
            if not (digit(rc) or uppercase(rc) or lowercase(rc)):   
                r -= 1
                continue
            
            if digit(lc) ^ digit(rc): return False
      
            if (lc != rc) and abs(ord(lc) - ord(rc)) != 32: return False
            l += 1
            r -= 1
            
        return True
            

def main():
    solve = Solution()

    tests = [
        {'s': "A man, a plan, a canal: Panama"},
        {'s': "race a car"},
        {'s': " "}
    ]
                
    for test in tests:
        print(solve.isPalindrome(test['s']))
        

if __name__ == '__main__':
    main()
           