# background:
#   Create a program that 'emulates' the world, but in numerical values for everything. (At least in the back end)
#   Have a simple GUI where it's something like a graph or some sort of display to show data, and below that
#   display area, there can be buttons for things like Start, Stop, Reset, Quit, etc. The data shown in the 'display'
#   will contain things like "# of people alive" "day/month/year", "% of good/bad people", and more

# Timelines: the sim will move at a rate of 1s = 30 days. It will probably work in a loop that looks loosely like this


# while gameOver is False:
#   *code for whatever happens in a month*
#   time.sleep(1)
#   *code to add that last seconds/months data, aswell as update variables to keep displayed time correct



# Thoughts ~~
# People can be 'classified' as good and bad. If they're a good person, the number that represents them will be
# a positive number, if they're a bad person, a negative number. This will be chosen on 'spawn' at random.
# There can be a chance for people to spawn as 100% good or 100% bad too, which will have effects on their life
# that can be figured out later.

# There can be a random chance for a natural disaster where sims could die/stuff like that?


import random, time
import tkinter as tk
from PIL import ImageTk



population = 2

def startSim():
    print("Start button pressed")



def quitGame():
    print("Game Quit")
    quit()



def pop_label(label):
    def growPop():
        global population
        population += 1
        label.config(text=str(population))
        label.after(1000, growPop)

    growPop()


def popLabel(label):
    def growPopulation():
        global population
        population += (population / 2)
        population = round(population)
        label.config(text=str(population))
        label.after(1000, growPopulation)
    growPopulation()


root = tk.Tk() #init the tkinter window
root.title("Absolutely Horrendous Life and World Simulator")    # Window title
root.geometry("800x900") #window size
frame = tk.Frame(root)
frame.pack()


#canvas test

canvasTest = tk.Canvas(root, bg="light grey", height="450", width="750")
canvasBgImage = ImageTk.PhotoImage(file=".\worldmap.gif")
canvasTest.create_image(450, 750, image=canvasBgImage)
canvasTest.pack()


textPopulationLabel = tk.Label(root, text="Population") # 'Population' text above population counter
textPopulationLabel.pack()

populationLabel = tk.Label(root)    # dynamic population counter lobel
populationLabel.pack()
popLabel(populationLabel)

startButton = tk.Button(root, text="Start Sim", command =startSim, height="5", width="15")
startButton.pack(anchor="se")
quitButton = tk.Button(root, text="Quit", command=quitGame, height="5", width="15") # kills app
quitButton.pack(anchor="se")






root.mainloop()