
class SpaceImageFormat:
    def __init__(self, inputLocation, width, height):
        self.inputLocation = inputLocation
        self.width = width
        self.height = height
        self.inputString = ""
        self.inputList = []
        self.layers = []
        self.layerCounts = []

    # Import the puzzel input
    def ImportData(self):
        self.inputString = open("puzzel_input.txt","r").read()            

    # Construct Layers - loop through the string of numbers and add them to 
    # lists of columns and layers
    def ConstructLayers(self):            
        # Split the string of numbers into a list of integers
        self.inputList = list(map(int,self.inputString))        
        cols = []
        rows = []
        for i in range(0,len(self.inputList)):
            cols.append(self.inputList[i])
            if len(cols) == self.width:
                rows.append(cols.copy())
                cols.clear()
            if len(rows) == self.height:
                self.layers.append(rows.copy())
                rows.clear()
    
    # Count the number of zeros, ones, and twos in each layer
    # Create a list of the results
    def SetLayerCounts(self):        
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

    def PerformTest(self):        
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
        self.ImportData()
        self.ConstructLayers()
        self.SetLayerCounts()
        result = self.PerformTest()
        print(f"The answer is {result}")

# 
spaceImageFormat = SpaceImageFormat("puzzel_input.txt",25,6)
spaceImageFormat.TestForCorruption()




    