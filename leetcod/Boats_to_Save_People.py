// problem link: https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3602/


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people)-1
        boats =0
        while i <= j:
            if (people[i]+people[j]) <= limit:
                i += 1
            j -= 1
            boats += 1
        return boats
