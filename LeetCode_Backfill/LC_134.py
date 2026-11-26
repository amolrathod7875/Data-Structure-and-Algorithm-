class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_fuel = 0      
        current_fuel = 0    # Fuel at current starting point
        start = 0           # starting station
        
        for i in range(len(gas)):
            total_fuel += gas[i] - cost[i]
            current_fuel += gas[i] - cost[i]
            
            # If current candidate fails, next station is new candidate
            if current_fuel < 0:
                start = i + 1
                current_fuel = 0
        
        # Only valid if total fuel isn't negative
        return start if total_fuel >= 0 else -1
        