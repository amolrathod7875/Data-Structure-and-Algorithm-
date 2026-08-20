class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()

        total_moves = 0
        for seat, student in zip(seats, students):
            total_moves += abs(seat - student)

        return total_moves
