
class ChecksumPuzzel:
    def __init__(self, inputLocation):
        self.inputLocation = inputLocation                
        self.inputList = []
        self.twiceNum = 0
        self.thriceNum = 0

    # -------------------------------------------------------------------------
    # Loop through the strings
    # ------------------------------------------------------------------------- 
    def Go(self):            
        # Load each line in the file as an item in a list
        with open(self.inputLocation,"r") as file:
            self.inputList = file.readlines()
        file.close()        
        
        # NOTE: Range doesn't need the -1 because the max is not used
        for i in range(0,len(self.inputList)):             
            self.CheckForTwiceAndThrice(self.inputList[i].strip())                      
            
        print('Twice =', self.twiceNum)
        print('Twice =', self.thriceNum)
        print('Checksum =',self.twiceNum * self.thriceNum)
    
    # -------------------------------------------------------------------------
    # Check for Twice and Thrice
    # -------------------------------------------------------------------------    
    def CheckForTwiceAndThrice(self,*str1):        
        
        stringValue = str1[0]
        stringList = list(stringValue)        
        uniqueLetterList = []
        count = 0
        
        # Load up List of Letters
        for letter in stringList:
            if letter not in uniqueLetterList:
                uniqueLetterList.append(letter)

        # Create the list to count the counts for each letter
        letterCountList = list(range(len(uniqueLetterList)))
        
        # Determine how many times each letter shows up in the list
        for i in range(0,len(uniqueLetterList)):
            letter = uniqueLetterList[i]
            # Count the number of times the letters exists in the string
            count = stringValue.count(letter)
            # Set the number of times the letter exists in the string            
            letterCountList[i] = count
            
        #print(stringValue, uniqueLetterList, letterCountList)
        
        weHaveA2 = 0
        weHaveA3 = 0
        
        # Loop through looking for Twice and Thrice
        for num in letterCountList:
            # Update the master count for Twice and Thrice
            if num == 2 and weHaveA2 == 0:
                self.twiceNum = self.twiceNum + 1
                weHaveA2 = 1
            if num == 3 and weHaveA3 == 0:
                self.thriceNum = self.thriceNum + 1
                weHaveA3 = 1
            if weHaveA2 == 1 and weHaveA3 == 1:
                exit
           

######################################################################
cp = ChecksumPuzzel("input.txt")
cp.Go()





    