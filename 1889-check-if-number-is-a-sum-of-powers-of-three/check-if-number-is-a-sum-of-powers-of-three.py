class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power = -1
         
        while 3 ** power <= n:
            power += 1
        
        while n > 0:
            if n >= 3 ** power:
                n -= 3 ** power
                
            if n >= 3 ** power:
                return False
            
            power -= 1
        
        return True

        # remain = n
        # powers = []

        # while remain >= 3: 
        #     base_power = math.floor(sympy.log(remain, 3))
        #     if base_power not in powers:
        #         powers.append(base_power)
        #         remain -= 3 ** base_power
        #     else:
        #         return False
            
        # if remain == 0 or remain == 1:
        #     return True
        # else:
        #     return False