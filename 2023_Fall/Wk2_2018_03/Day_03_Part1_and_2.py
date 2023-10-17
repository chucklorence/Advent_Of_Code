import numpy as np

# -----------------------------------------------------------------------------
# Class for solving Day 3: No Matter How You Slice It
# https://adventofcode.com/2018/day/3 
# -----------------------------------------------------------------------------
class NoMatterHowYouSliceIt:
    def __init__(self, inputLocation):
        # Holds the path to the file with the the data inputs
        # NOTE: This class expects the data in the file to be formatted as 
        #   comma delimited numbers. For example:
        #   #1 @ 185,501: 17x15 is formatted to 1,185,501,17,15
        self.inputLocation = inputLocation                
        # This list will hold the list of 'claims' from the data input file
        self.claimList = []

    # -------------------------------------------------------------------------
    #  Load each claim into a list of dictionaries
    #  Then call the funtion to calculate the overlaps
    # ------------------------------------------------------------------------- 
    def Go(self):            
        
        # Load each line in the file as an item in a list
        with open(self.inputLocation,"r") as file:
            for line in file:
                # Each line of data represents a claim.
                # Each claim has been formatted to be seperated by commas. Use the commas
                #   to split each line of the data into a list of values
                claimItemList = line.split(',')
                # We're using a dictionary to hold the values for each claim.
                # This will make it easier to keep track of what each data elements means
                #   later in the code.
                # The claimList is a list that will hold each claim (which is stored as a dictionary)
                self.claimList.append({
                    'claimNumber': int(claimItemList[0]),
                    'X':int(claimItemList[1]),
                    'Y':int(claimItemList[2]),
                    'width':int(claimItemList[3]),
                    'height':int(claimItemList[4])
                })            
        # Close the data input file.
        file.close()          
        # Call the function that will perform the calculations.
        self.CalcOverLaps()        
        
    # -------------------------------------------------------------------------
    # Performs the calculations for the overlaps
    # -------------------------------------------------------------------------    
    def CalcOverLaps(self):        
        
        # Represents the 1000x1000 square inches of fabric. This 2D array will 
        #   keep track of the number of times claims overlap with another.
        fabric2DArray = np.zeros((1000,1000))
        
        # -----
        # Determine the overlaps by incrementing the value of
        #   each squire of fabric by one where a claim exists
        for dic in self.claimList:            
            X = dic['X']
            Y = dic['Y']
            width = dic['width']
            height = dic['height']
            
            # We've turned the 1000x1000 inches of fabric into a grid of squares.
            # We can locate each claim using X,Y coordinates as follows:
            #   X = The number of inches between the left edge of the fabric and the left edge of the rectangle
            #   Y = The number of inches between the top edge of the fabric and the top edge of the rectangle
            # We can use the width and height of the claim to determine where each square inch of the fabric 
            #   is located within the grid.
            #   X + The width of the rectangle in inches --> tells us the X coordinates
            #   Y + The height of the rectangle in inches --> tells us the Y coordinates
            
            # The following set of 'for loops' loops through the 2D array.                        
            # The outter loop loops through the rows             
            for xLoc in range(X, X + width):        
                # The inner loop loops through the columns for each row        
                for yLoc in range(Y, Y + height):                    
                    # For each square location of the claim, add 1 to each value in the square
                    # This allows us to keep track of the number of times a square is included
                    #   in aother claim.
                    fabric2DArray[xLoc,yLoc] = fabric2DArray[xLoc,yLoc] + 1
            
        # -----
        # Now that we've identified where each square inch of fabric which a claim exists
        # We can loop through and locate each squire of fabric with more than 1 claim
        # Remember --> We added a 1 to each location where a claim exists, so if more than one
        #   claim overlaps another, then the square will have a value greater than 1.  
        overLaps = 0
        
        # The outter loop loops through the rows --> of which we have 1000 rows
        for xLoc in range(0,1000):
            # The outter loop loops through the columns of each row --> we have 1000 columns in each row
            for yLoc in range(0,1000):
                # Gets the value of the X,Y coordinate
                val = fabric2DArray[xLoc,yLoc]
                # Check to see if the value is greater than 1
                # If the value is greater than one, then more than one claim includes the square
                if val > 1:
                    overLaps += 1
                    
        # -----
        # This is part 2 of the exercise. In this code, we're trying to find the claims that are not
        #   overlapped by other. The exercise says there is only one, but we're using a list to keep track
        #   just in case more than one exists in our data set.
        # Loop through each claim, check to see if any part of the claim
        # is overlapped by other claim. If it isn't overlapped, then add
        # that claim to the list of claims that aren't overlapped
        claimsWithoutOverLapsList = []
        for dic in self.claimList:    
            # The following pulls out all the values for the claim        
            X = dic['X']
            Y = dic['Y']
            width = dic['width']
            height = dic['height']
            claimNumber = dic['claimNumber']
            claimOverLaps = 0
            # Loop through the claim's rows
            for xLoc in range(X, X + width):                
                # Loop through each column for each row in the claim
                for yLoc in range(Y, Y + height):                   
                    # Get the value for the coordinate we're evaluating 
                    val = fabric2DArray[xLoc,yLoc] 
                    # If the square for the claim is greater than 1, that means 
                    #   the claim is overlapping another claim.
                    if val > 1:
                        claimOverLaps += 1
                    # If we've discovered that the claim overlaps another
                    #   let's get out of this claim and skip to the next claim
                    if claimOverLaps > 0:
                        # Exit the 'for loop' because we've found that the claim overlaps another
                        break;
            # After checking the entire claim, if none of its squares overlap another claim's square
            #   then we add that claim to the list of claims that do not overlap another claim.
            if claimOverLaps == 0:
                claimsWithoutOverLapsList.append(claimNumber)
        
        # -----
        # Show the number of square inches of fabric that exist within two or more claims.
        print(overLaps,'square inches of fabric are within two or more claims.')
        # Show the claims that do not overlap with another claim.
        print('The claim(s) that do not overlap are:',claimsWithoutOverLapsList)

######################################################################
if __name__ == "__main__":
    # Create the class, passing in the location of the formatted data inputs.
    cp = NoMatterHowYouSliceIt("input_formatted.txt")
    # Start the calcuations and discover the answers.
    cp.Go()





    