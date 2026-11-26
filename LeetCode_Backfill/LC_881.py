class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        boat_count = 0
        left = 0
        right = len(people) - 1

        while left<=right:
            boat_count += 1 
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
        return boat_count
        