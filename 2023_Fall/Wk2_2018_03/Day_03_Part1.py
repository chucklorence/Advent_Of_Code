import numpy as np

class NoMatterHowYouSliceIt:
    def __init__(self, inputLocation):
        self.inputLocation = inputLocation                
        self.claimList = []

    # -------------------------------------------------------------------------
    #  Load each claim into a list of dictionaries
    #  Then call the funtion to calculate the overlaps
    # ------------------------------------------------------------------------- 
    def Go(self):            
        
        # Load each line in the file as an item in a list
        with open(self.inputLocation,"r") as file:
            for line in file:
                claimItemList = line.split(',')
                self.claimList.append({
                    'claimNumber': int(claimItemList[0]),
                    'X':int(claimItemList[1]),
                    'Y':int(claimItemList[2]),
                    'width':int(claimItemList[3]),
                    'height':int(claimItemList[4])
                })            
        file.close()          
        self.CalcOverLaps()        
        
    # -------------------------------------------------------------------------
    # Calculate the overlaps
    # -------------------------------------------------------------------------    
    def CalcOverLaps(self):
        
        
        fabric2DArray = np.zeros((1000,1000))
        
        # Determine the overlaps by incrementing the value of
        # each squire of fabric by one where a claim exists
        for dic in self.claimList:            
            X = dic['X']
            Y = dic['Y']
            width = dic['width']
            height = dic['height']
            # Loop through and add 1 to each value in the square
            for xLoc in range(X, X + width):                
                for yLoc in range(Y, Y + height):                    
                    fabric2DArray[xLoc,yLoc] = fabric2DArray[xLoc,yLoc] + 1
            
        # Loop through and find each squire of fabric with more than 1 claim
        overLaps = 0
        for xLoc in range(0,1000):
            for yLoc in range(0,1000):
                val = fabric2DArray[xLoc,yLoc]
                if val > 1:
                    overLaps += 1
                    
        # Loop through each claim, check to see if any part of the claim
        # is overlapped by other claim. If it isn't overlapped, then add
        # that claim to the list of claims that aren't overlapped
        claimsWithoutOverLapsList = []
        for dic in self.claimList:            
            X = dic['X']
            Y = dic['Y']
            width = dic['width']
            height = dic['height']
            claimNumber = dic['claimNumber']
            claimOverLaps = 0
            for xLoc in range(X, X + width):                
                for yLoc in range(Y, Y + height):                    
                    val = fabric2DArray[xLoc,yLoc] 
                    if val > 1:
                        claimOverLaps += 1
                    if claimOverLaps > 0:
                        break;
            if claimOverLaps == 0:
                claimsWithoutOverLapsList.append(claimNumber)
        
        print(overLaps,'square inches of fabric are within two or more claims.')
        print('The claim(s) that do not overlap are:',claimsWithoutOverLapsList)

######################################################################
if __name__ == "__main__":
    cp = NoMatterHowYouSliceIt("input_formatted.txt")
    cp.Go()





    