class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            key = tuple(sorted(s))

            if key not in groups:
                groups[key]=[]

            groups[key].append(s)

            
        return list(groups.values())

    # m is number of strings and n is length of the longest string
