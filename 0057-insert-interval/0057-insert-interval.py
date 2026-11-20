class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
       
        new= newInterval    
        res = []
        i, n = 0, len(intervals)

        # 1. intervals entirely before the new one
        while i < n and intervals[i][1] < new[0]:
            res.append(intervals[i])
            i += 1

        new = new[:]  
        while i < n and intervals[i][0] <= new[1]:
            new[0] = min(new[0], intervals[i][0])
            new[1] = max(new[1], intervals[i][1])
            i += 1
        res.append(new)

        # 3. intervals entirely after
        res.extend(intervals[i:])
        return res
