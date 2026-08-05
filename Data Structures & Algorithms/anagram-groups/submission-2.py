class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for s in strs:
            x=tuple(sorted(s))
            if x not in hashmap:
                hashmap[x]=[]
            hashmap[x].append(s)
        return list(hashmap.values())