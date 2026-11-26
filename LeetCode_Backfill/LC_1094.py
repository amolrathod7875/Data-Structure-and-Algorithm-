class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = [0] * 1002
        for passanger, start, end in trips:
            timeline[start] += passanger
            timeline[end] -= passanger
        seats = 0
        for passanger_change in timeline:
            seats += passanger_change 
            if seats > capacity:
                return False
        return True 
        