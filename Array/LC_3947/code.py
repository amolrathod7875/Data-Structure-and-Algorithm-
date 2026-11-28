from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        limit = max(factor for factor, _ in items)
        frequency = [0] * (limit + 1)
        for factor, _ in items:
            frequency[factor] += 1

        bonus_slots = [0] * (limit + 1)
        for factor in range(1, limit + 1):
            if frequency[factor]:
                bonus_slots[factor] = sum(
                    frequency[multiple]
                    for multiple in range(factor, limit + 1, factor)
                ) - 1

        ordered = sorted(items, key=lambda item: item[1])
        cheapest_price = ordered[0][1]
        boosted_copies = 0
        for factor, price in ordered:
            # Two copies at the minimum price cost no more than this bonus pair.
            if price >= 2 * cheapest_price or price > budget:
                break
            count = min(bonus_slots[factor], budget // price)
            boosted_copies += count
            budget -= count * price

        return 2 * boosted_copies + budget // cheapest_price
