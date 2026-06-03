class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode it to single string 
        if not strs:
            return ""

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        #decode it to a list
        #return a list 
        #assign a pointer to keep track
        res, i = [], 0

        while i < len(s):
            # assign a pointer to find #
            j = i # starts at 0
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res

