class Solution:
    def getSecondLargest(self, arr: list[int]) -> int:
        """Return the second largest distinct element in the array.

        Scans the array once, tracking the largest and second largest
        values. If no second largest exists (fewer than 2 distinct
        values), returns -1.
        """
        largest = None
        second_largest = None

        for num in arr:
            if largest is None or num > largest:
                second_largest = largest
                largest = num
            elif num != largest and (second_largest is None or num > second_largest):
                second_largest = num

        return second_largest if second_largest is not None else -1