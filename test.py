#This exercise is to find the lenght of largest substring
#example: string: dvdf, largest substring: vdf

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abcabcbb
        # aaabc
        stor = ""
        current=""
        # if len(s)==1:
        #     return 1
        s = s+" "
        for i in range(len(s)-1):
            stor = stor+s[i]
            if(s[i+1] in stor):
                if len(stor)>len(current):
                    current = stor
                stor =""
                continue
            
            if len(stor)>len(current):
                current = stor
            print(stor," ",current)
        print(current)
        return len(current)

a = Solution()
print(f'actual {a.lengthOfLongestSubstring("dvdf")}')
print(f"Expexted: {3}" )