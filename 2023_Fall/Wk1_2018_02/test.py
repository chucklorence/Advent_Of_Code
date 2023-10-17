
class TestClass:
    def __init__(self):
        self.inputStr = ""
        
    def testPrint(self, str1):
        print(str1)        
       
tmp = TestClass()
tmp.testPrint("Testing")


# In order for the PRINT to print the string "Testing" instead of the string's memoray location
# Why do we have to (1) specify pass by reference
# and (2) specify the first element of str1 - e.g., str1[0]
class TestClass:
    def __init__(self):
        self.inputStr = ""
        
    def testPrint(self, str1):
        print(str1)        
       
tmp = TestClass()
tmp.testPrint("Testing")




thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  #print(thislist[i])
  i = i + 1

testStr = "ivjlczdtkeiltwgsfamqprbnuyll"
for i in range(0,len(testStr)):
    #print(testStr[i])
    i = 2
    



def CheckForTwice(str1):
    idx = 0
    countList = []
    value = ""
    # Main loop - looping through each letter
    for letter in str1:
        countList.append(0)
        # Loop to check for matches
        for i in range(0,len(str1)):
            if i != idx:
                if letter == str1[i]:
                    yyy = 1                    
        # Set the index for the next letter in the main loop
        idx = idx + 1
    