class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        final = []
        temp = len(list1) + len(list2)
        for i, word in enumerate(list1):
            print(word)
            if word in list2:
                print('1st if')
                if i + list2.index(word) < temp:
                    print('2nd if')
                    final = [word]
                    temp =  i + list2.index(word)
                elif i + list2.index(word) == temp:
                    print('elif')
                    final.append(word)
        return final