from typing_extensions import Self


class PasswordHacker:
    def __init__(self, minValue, maxValue):
        self.minValue = minValue
        self.maxValue = maxValue
        self.validPasswords = []

# 8090 was too high
# 2400 was too high

    def DetermineNumPasswords(self):
        
        for i in range(self.minValue,self.maxValue):
            if(self.MeetsRequirements(i) == True):
                print(i)
                self.validPasswords.append(i)

        return len(self.validPasswords)
   
    def MeetsRequirements(self, potentialPassword):
        if (potentialPassword >= self.minValue 
            and potentialPassword <= self.maxValue
            and len(str(potentialPassword)) == 6
            and self.MeetsAdjacentRules(potentialPassword) == True
            ):
            return True
        else:
            return False

    def MeetsAdjacentRules(self,num):
        strNum = str(num)
        numLength = len(strNum)
        adjacentSame = False
        adjacentNotDecrease = False
        # Check for duplicates - need at least one
        for i in range(0,numLength - 1):
            if strNum[i] == strNum[i+1]:
                adjacentSame = True
                break

        # Check for adjacent same or increasing
        for i in range(0,numLength - 1):
            if (strNum[i] <= strNum[i+1]):
                adjacentNotDecrease = True
            else:
                adjacentNotDecrease = False
                break

        if adjacentSame == True and adjacentNotDecrease == True:
            return True
        else:
            return False

passHacker = PasswordHacker(402328,864247)
print(f"Number of passwords witin the range provided: {passHacker.DetermineNumPasswords()}")


                


        



        
        
