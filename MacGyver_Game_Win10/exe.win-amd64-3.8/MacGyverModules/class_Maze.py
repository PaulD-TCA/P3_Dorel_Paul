import os
import pygame


pathtofolder = os.path.abspath("")
pathtomodules = os.path.join(pathtofolder, "MacGyverModules", "MazeLevel1.data")


class Maze:

	def __init__(self):

		#self.pathtomodules = pathtomodules
		self.mazefile = open(pathtomodules, "r")
		self.mazestr = 0

	def mazecrea(self):
		listesrow = []
		for caractersstring in self.mazefile:
			listcaracters = []
			for caracters in caractersstring:
				if caracters != "\n":
					listcaracters.append(caracters)
			listesrow.append(listcaracters)
		self.mazestr = listesrow
