class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        seats.sort()
        count = 0

        for i, stud in enumerate(students):
            count += abs(stud - seats[i])
    
        return count