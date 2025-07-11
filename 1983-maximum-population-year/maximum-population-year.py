class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        total_people = {}
        for year in range(1950, 2051):
            for l in logs:
                if year in range(l[0], l[1]):
                    if year not in total_people:
                        total_people[year] = 1
                    else:
                        total_people[year] += 1
        
        dict_sort = sorted(total_people.items(), key = lambda item: item[1], reverse = True)

        return dict_sort[0][0]