
class SpaceImageFormat:
    def __init__(self, inputLocation, width, height):
        self.inputLocation = inputLocation
        self.width = width
        self.height = height
        self.inputString = ""
        self.inputList = []
        self.decodedMessage = []
        self.layers = []
        self.layerCounts = []

    # Import the puzzel input
    def ImportData(self):
        self.inputString = open(self.inputLocation,"r").read()            

    # Construct Layers - loop through the string of numbers and add them to 
    # lists of columns and layers
    def ConstructLayers(self):            
        self.ImportData()
        # Split the string of numbers into a list of integers
        self.inputList = list(map(int,self.inputString))        
        cols = []
        rows = []
        for i in range(0,len(self.inputList)): ## Range doesn't need the -1 because the max is not used
            cols.append(self.inputList[i])
            if len(cols) == self.width:
                rows.append(cols.copy())
                cols.clear()
            if len(rows) == self.height:
                self.layers.append(rows.copy())
                rows.clear()       
    
    def SetupMessageContainer(self):
        row = []
        for x in range(0,self.height):
            for i in range(0,self.width):
                row.append(-1)
                if len(row) == self.width:
                    self.decodedMessage.append(row.copy())
            row.clear()

    def DecodeMessage(self):    
        # 0 == Black, 1 == White, 2 == Transparent    
        widthPointer = 0                
        heightPointer = 0
        self.ConstructLayers()
        self.SetupMessageContainer()
        for layer in self.layers:
            for row in layer:
                for num in row:
                    if self.decodedMessage[heightPointer][widthPointer] == -1:
                        self.decodedMessage[heightPointer][widthPointer] = num
                    elif self.decodedMessage[heightPointer][widthPointer] == 2:
                        self.decodedMessage[heightPointer][widthPointer] = num                    
                    
                    # Manage the pointer that indicates the col we just worked
                    widthPointer = widthPointer + 1
                    if widthPointer == self.width:
                        widthPointer = 0

                # Manage the pointer that indicates the row we just worked on
                heightPointer = heightPointer + 1
                if heightPointer == self.height:
                    heightPointer = 0

        result = ""
        for row in self.decodedMessage:
            for num in row:
                result = result + str(num)
        
        # Can do this OR Copy the output into notepad and replace the 1s with periods and the 0s with a space to see 5 letters formed
        correctPixels=[[''.join(str(pixel)).replace('0',' ').replace('1','.') for pixel in row] for row in self.decodedMessage]
        for i in range(6): print("".join(correctPixels[i]))

        print(result)


    # Count the number of zeros, ones, and twos in each layer
    # Create a list of the results
    def Testing_SetLayerCounts(self):        
        for layer in self.layers:
            # Count the number of Zeros            
            countZeros = 0
            countOnes  = 0
            countTwos  = 0
            # Review each row in the layer
            for rows in layer:                
                # Review each column (which is a number) in the row
                for col in rows:                                        
                    if col == 0:
                        countZeros = countZeros + 1
                    elif col == 1:
                        countOnes = countOnes + 1
                    elif col == 2:
                        countTwos = countTwos + 1
            
            self.layerCounts.append([countZeros,countOnes,countTwos])

    def Testing_PerformTest(self):        
        layerFewestZeros = []
        layerNumber = 0
        # Loop through our list that contains the counts of 0s, 1s, and 2s
        # Find the layer with the least zeros
        for layerCount in self.layerCounts:            
            if len(layerFewestZeros) == 0:
                layerFewestZeros = [layerNumber,layerCount[0]]
            elif layerCount[0] < layerFewestZeros[1]:
                layerFewestZeros[0] = layerNumber
                layerFewestZeros[1] = layerCount[0]
            layerNumber = layerNumber + 1

        # Multiply the number of 1 digits by the number of 2 digits
        # To get our answer
        fewestZeros = self.layerCounts[layerFewestZeros[0]]
        result = fewestZeros[1] * fewestZeros[2]     
        return result
    
    # All all the functions needed to test for corruption
    def TestForCorruption(self):        
        self.ConstructLayers()
        self.Testing_SetLayerCounts()
        result = self.Testing_PerformTest()
        print(f"The answer is {result}")

# 
spaceImageFormat = SpaceImageFormat("puzzel_input.txt",25,6)
# spaceImageFormat = SpaceImageFormat("puzzel_input_example.txt",2,2)
# spaceImageFormat.TestForCorruption()
spaceImageFormat.DecodeMessage()




    