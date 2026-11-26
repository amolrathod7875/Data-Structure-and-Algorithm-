class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        for fruit in fruits :
            placed = False
            for j in range(len(baskets)):
                if baskets[j] >= fruit:
                    baskets[j] = -1
                    placed = True
                    break

            if not placed:
                count += 1

        return count 