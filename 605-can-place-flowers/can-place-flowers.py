class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n > 0:
            flowerbed[0] = 1
            n -= 1
        elif flowerbed[0] == 0 and n > 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        temp = 1
        while temp < len(flowerbed) - 1 and n > 0:
            if flowerbed[temp] == 1:
                temp += 1
                continue
            elif flowerbed[temp] == 0 and flowerbed[temp-1] == 0 and flowerbed[temp+1] == 0:
                flowerbed[temp] = 1
                n -= 1
            temp += 1

        if flowerbed[-1] == 0 and n > 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1
        if n == 0:
            return True
        else:
            return False 