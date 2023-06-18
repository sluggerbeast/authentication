#This exercise is to find the lenght of largest substring
#example: string: dvdf, largest substring: vdf

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abcabcbb
        # aaabc
        #dvdf
        seen= {}
        l=0
        current = ""

        for r in range(len(s)):

            stor = s[r]

            if stor in seen and (r>seen[stor]):
                l = l +1

            else:
                current = r-l+1

            seen[stor] = r
        print(current)
        return current



        


a = Solution()
s ="dvdf"
len(s)
print(f'actual {a.lengthOfLongestSubstring(s)}')
print(f"Expexted: {3}" )