class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # a string, return length of longest substring 
        # substring (no duplicates)
        # all alphabets, empty string 

        # "abcdabca" -> 4 ("abcd")

        # sliding window and hashset
        # l and r 
        # charSet = set() # O(1) lookup find duplicates
        # if s[r] in charSet, remove it from charset 
        # add r to hashset 
        # longest = max(longest, r-l+1)

        l = 0
        longest = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            longest = max(longest, r-l+1)
        return longest


        