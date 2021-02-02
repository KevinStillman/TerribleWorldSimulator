import random, json




# create 'year' class with functions for checking the population born, population alive/dead, deleting the year,
# determining how many people are evil,

class Year:

    populationDataFile = open("population.json", "r+")



    def __init__(self, amountBorn, actualYear, chunktier):
        self.amountBorn = amountBorn
        self.actualYear = actualYear
        self.chunktier = chunktier
        self.yearAge = 0

    # function to determine how many were born
    def bornThisYear(self, chunktier):
        pass


    #function to determine how many are evil
    def howManyEvil(self, chunktier):
        # IF CHUNK IS 1ST WORLD



        #IF CHUNK IS 3RD WORLD



    # function to determine death rate (include calculation for evil effect)




    # function to add 1 to the years age (called every new year)
    def addOneToAge(self):
        self.yearAge += 1


    def getPopultionForYear(self):
        print(f"Amount of people born in this year: {self.amountBorn}")
        return self.amountBorn

    def getPopulationAlive(self):
        pass


            # Function to compile the years data to send to json
    def yearDataCompile(self):
        yearInfo = {
            "year": self.actualYear,
            "born": self.amountBorn,
            "alive": self.getPopulationAlive()

        }


