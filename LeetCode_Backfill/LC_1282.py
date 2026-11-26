class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        temp_dict = defaultdict(list)
        result = []

        for i, size in enumerate(groupSizes):
            temp_dict[size].append(i)
            
            if len(temp_dict[size]) == size:
                result.append(temp_dict[size])
                temp_dict[size] = []
        return result
        