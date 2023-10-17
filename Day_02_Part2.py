
from difflib import SequenceMatcher

class ChecksumPuzzel:
    def __init__(self, inputLocation):
        self.inputLocation = inputLocation                
        self.inputList = []
        self.twiceNum = 0
        self.thriceNum = 0

    # -------------------------------------------------------------------------
    # Loop through the strings
    # ------------------------------------------------------------------------- 
    def Go_GetCheckSum(self):            
        self.LoadData()
        
        # NOTE: Range doesn't need the -1 because the max is not used
        for i in range(0,len(self.inputList)):             
            self.CheckForTwiceAndThrice(self.inputList[i].strip())                      
            
        print('Twice =', self.twiceNum)
        print('Twice =', self.thriceNum)
        print('Checksum =',self.twiceNum * self.thriceNum)
        
    # -------------------------------------------------------------------------
    # Loops through the two lists and looks for the two strings that only have a single difference
    # During testing, realized that only 2 strings had only a single difference --> so manually determined
    # which letters were the same...decided not to continue with a programatic way to figure out the answer.
    # -------------------------------------------------------------------------         
    def Go_FindBoxes(self):
        self.LoadData()  
        listLength = len(self.inputList)  
        idx = 0    
        for outerStr in self.inputList:
            # Shorten the inner list as we go, so that we aren't re-comparing strings
            for innerStr in self.inputList[idx + 1:listLength]:
                numDif = self.CompareStrings(outerStr,innerStr)
                if numDif == 1:                    
                    print(outerStr,innerStr)
            idx += 1

    # -------------------------------------------------------------------------
    # Returns the number of differences between 2 strings
    # -------------------------------------------------------------------------         
    #def CompareStrings(self,strs):            
    #    strA = strs[0]
    #    strB = strs[1]
    #    
    #    print(strA,strB)
        
    def CompareStrings(self,str1,str2):            
        strA = str1
        strB = str2        
        resultA = ""
        resultB = ""
        
        # Find the max length
        maxLength = len(strA) if len(strA) > len(strB) else len(strB)
        
        # Number of differences
        numDif = 0
        
        # Loop through both string and compare the letters
        # Keep count of the number of differences
        for i in range(maxLength):
            letterA = strA[i:i+1]
            letterB = strB[i:i+1]
            if letterA != letterB:
                numDif += 1
                resultA += letterA
                resultB += letterB
       
        #print("strA = "+strA,"resultA = "+resultA,"resultB = "+resultB)  
        return numDif      
        
        
        
      
    # -------------------------------------------------------------------------
    # Load data
    # -------------------------------------------------------------------------         
    def LoadData(self):
        # Load each line in the file as an item in a list
        with open(self.inputLocation,"r") as file:
            self.inputList = file.readlines()
        file.close() 
    
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
#cp.Go_GetCheckSum()
cp.Go_FindBoxes()





    