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


        # min_time = min(event1[0], event2[0])
        # min_time = int(min_time.split(':')[0]) * 60 + int(min_time.split(':')[1])
        
        # max_time = max(event1[1], event2[1])
        # max_time = int(max_time.split(':')[0]) * 60 + int(max_time.split(':')[1])

        # for i in range(min_time, max_time):
        #     hr = i // 60
        #     mi = i % 60
            
            #print(i)