import pygame as pg
import random, json




# create 'year' class with functions for checking the population born, population alive/dead, deleting the year,
# determining how many people are evil,

class Year:

    populationDataFile = open("population.json", "w")


    def __init__(self, amountBorn):
        self.amountBorn = amountBorn


    def getPopultionForYear(self):
        print(f"Amount of people born in this year: {self.amountBorn}")
        return self.amountBorn

    def getPopulationAlive(self):
        pass

