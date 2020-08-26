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
# import tkinter as tk
# from PIL import ImageTk
# import pygame
#
#
# population = 2
#
# def startSim():
#     print("Start button pressed")
#
# def pauseSim():
#     print("Pause button pressed")
#
# def quitGame():
#     print("Game Quit")
#     quit()
#
#
# pygame.init() #pygame init
#
# display_width = 750     # letting the dimensions be variable rather than
# display_height = 850    # hard coded in.
#
# gameDisplay = pygame.display.set_mode((display_width, display_height)) # window creation
# pygame.display.set_caption("A Terrible World Simulator") # Window title
#
# black = (0,0,0)         # defining colors
# white = (255,255,255)   # defining colors
#
# clock = pygame.time.Clock() # game timing
#
# crashed = False
#
# worldMapImg = pygame.image.load("worldmap.png")
#
# def map(x,y):
#     gameDisplay.blit(worldMapImg, (x,y))
#
#
# x = (display_width * -1)
# y = (display_height * -1)
#
# while not crashed:  # runs game until crash
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             crashed = True
#
#     gameDisplay.fill(white)
#     map(x,y)
#
#
#     pygame.display.update()
#     clock.tick(60)
#
# pygame.quit()
# quit()
#
#
#
#
#
#
#








## Below is the commented out code for tkinter UI

# def pop_label(label):
#     def growPop():
#         global population
#         population += 1
#         label.config(text=str(population))
#         label.after(1000, growPop)
#
#     growPop()
#
#
# def popLabel(label):
#     def growPopulation():
#         global population
#         population += (population / 2)
#         population = round(population)
#         label.config(text=str(population))
#         label.after(1000, growPopulation)
#     growPopulation()
#
#
# root = tk.Tk() #init the tkinter window
# root.title("Absolutely Horrendous Life and World Simulator")    # Window title
# root.geometry("800x900") #window size
#
#
# belowMap = tk.Frame(root)
# belowMap.pack(side="bottom", fill="both", expand=True)
# #canvas test
#
# canvasTest = tk.Canvas(root, bg="light grey", height="450", width="750")
# canvasTest.pack(expand="no", fill="none")
#
#
# canvasBgImage = tk.PhotoImage(file=".\worldmap.gif")
# canvasTest.create_image(1, 1, image=canvasBgImage, anchor="nw")
#
#
# textPopulationLabel = tk.Label(root, text="Population") # 'Population' text above population counter
# textPopulationLabel.pack()
#
# populationLabel = tk.Label(root)    # dynamic population counter lobel
# populationLabel.pack()
# popLabel(populationLabel)
#
# startButton = tk.Button(root, text="Start Sim", command =startSim, height="5", width="15")
# startButton.pack(in_=belowMap, side="left")
# pauseButton = tk.Button(root, text="Pause Sim", command=pauseSim, height="5", width="15")
# pauseButton.pack(in_=belowMap, side="left")
# quitButton = tk.Button(root, text="Quit Sim", command=quitGame, height="5", width="15") # kills app
# quitButton.pack(in_=belowMap, side="left")
#
#
#
#
#
#
# root.mainloop()