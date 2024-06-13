class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        seats.sort()
        count = 0

        for i, seat in enumerate(seats):
            count += abs(seat - students[i])
    
        return count