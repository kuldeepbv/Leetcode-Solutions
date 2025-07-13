class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        min_time1 = int(event1[0].split(':')[0]) * 60 + int(event1[0].split(':')[1])
        max_time1 = int(event1[1].split(':')[0]) * 60 + int(event1[1].split(':')[1])

        min_time2 = int(event2[0].split(':')[0]) * 60 + int(event2[0].split(':')[1])
        max_time2 = int(event2[1].split(':')[0]) * 60 + int(event2[1].split(':')[1])

        event1_time = []

        for time1 in range(min_time1, max_time1 + 1):
            if time1 in range(min_time2, max_time2 + 1):
                return True
        return False