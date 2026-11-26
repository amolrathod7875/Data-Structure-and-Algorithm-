class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        res_list = set(friends)
        res = []
        for id in order:
            if id in res_list:
                res.append(id)
        return res
        