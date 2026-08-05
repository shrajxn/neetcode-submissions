class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        L,R=0,len(people)-1
        count=0
        while L<=R:
            remain=limit-people[R]
            count+=1
            R-=1
            if remain>=people[L]:
                L+=1
        return count