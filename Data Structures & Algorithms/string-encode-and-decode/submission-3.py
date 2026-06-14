class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res = ""
        for s in strs:
            res += str(len(s)) +"#"+ s
        return res

    def decode(self, s: str) -> List[str]:
        res, i =[], 0 #pointer

        while i < len(s):
            j = i #j pointer to find "#"
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            #move pointer i
            i = j + 1 + length 

        return res

