class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        final = []
        temp = len(list1) + len(list2)
        for i, word in enumerate(list1):
            if word in list2:
                if i + list2.index(word) < temp:
                    final = [word]
                    temp =  i + list2.index(word)
                elif i + list2.index(word) == temp:
                    final.append(word)
        return final