class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        
        for s in strs:
            sorted_str = "".join(sorted(s))
            
            if not d.get(sorted_str):
                d[sorted_str] = [s]
            else:
                d[sorted_str].append(s)
                
        return list(d.values())
    
    
def main():
    solve = Solution()
    test = ["eat","tea","tan","ate","nat","bat"]
    
    print(solve.groupAnagrams(test))
    
        
    
if __name__ == '__main__':
    main()
                