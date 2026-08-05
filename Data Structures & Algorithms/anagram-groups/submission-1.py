class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for s in strs:
            x=str(sorted(s))
            if x not in hashmap:
                hashmap[x]=[]
                hashmap[x].append(s)
            else:
                hashmap[x].append(s)
        return list(hashmap.values())