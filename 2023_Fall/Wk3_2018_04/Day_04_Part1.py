import numpy as np

# -----------------------------------------------------------------------------
# Class for solving Day 4: Repose Record
# https://adventofcode.com/2018/day/4 
# -----------------------------------------------------------------------------
class ReposeRecord:
    def __init__(self, inputLocation):
        # Holds the path to the file with the the data inputs        
        self.inputLocation = inputLocation                
        self.GuardList = []

    # -------------------------------------------------------------------------
    # List of List of Guard entries 
    # Guard #, total mins asleep, min-0, min-1, ..., min-58, min-59
    # 
    # ------------------------------------------------------------------------- 
    def Go(self):            
        # Load each line in the file as an item in a list
        with open(self.inputLocation,"r") as file:
            for line in file:
                claimItemList = line.split(',')
        return
    
    def ExtractEntry(self):
        return


######################################################################
if __name__ == "__main__":
    # Create the class, passing in the location of the formatted data inputs.
    cp = ReposeRecord("input.txt")
    # Start the calcuations and discover the answers.
    cp.Go()





    