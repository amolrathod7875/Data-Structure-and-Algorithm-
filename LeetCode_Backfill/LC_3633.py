class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        minLand1 = float('inf')
        for i in range(len(landStartTime)):
            minLand1 = min(minLand1, landStartTime[i] + landDuration[i])
            
        result1 = float('inf')
        for i in range(len(waterStartTime)):
            waterStart = max(minLand1, waterStartTime[i])
            result1 = min(result1, waterStart + waterDuration[i])
            
        minWater2 = float('inf')
        for i in range(len(waterStartTime)):
            minWater2 = min(minWater2, waterStartTime[i] + waterDuration[i])
            
        result2 = float('inf')
        for i in range(len(landStartTime)):
            landStart = max(minWater2, landStartTime[i])
            result2 = min(result2, landStart + landDuration[i])
            
        return min(result1, result2)