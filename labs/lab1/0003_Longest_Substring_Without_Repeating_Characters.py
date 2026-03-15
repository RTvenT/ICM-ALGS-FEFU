class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = 0
        u = set(s[0])
        max_len = 1
        cur_len = 1
        
        for r in range(1, len(s)):
            cur_len += 1
            if s[r] in u:
                while s[l] != s[r]:
                    u.remove(s[l])
                    l += 1
                    cur_len -= 1
                l += 1
                cur_len -= 1

            u.add(s[r])
            max_len = max(max_len, cur_len)
                
        return max_len
            
            
        

def main():
    solve = Solution()

    tests = [
        {'s': "abcabcbb"},
        {'s': "bbbbb"},
        {'s': "pwwkew"},
        {'s': ""}
    ]
                
    for test in tests:
        print(solve.lengthOfLongestSubstring(test['s']))
        

if __name__ == '__main__':
    main()
           