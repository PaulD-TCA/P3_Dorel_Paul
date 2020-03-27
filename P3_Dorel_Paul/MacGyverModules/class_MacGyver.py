import os
import pygame


pathtofolder = os.path.abspath("")
pathtopics = os.path.join(pathtofolder, "Pictures")
pathtomodules = os.path.join(pathtofolder, "MacGyverModules", "MazeLevel1.data")

class MacGyver:
	def __init__(self,maze1):

		#self.pathtopics = pathtopics
		self.mgpic = pygame.image.load(pathtopics + "/MacGyver.png")
		self.mgpic = pygame.transform.scale(self.mgpic,(28,38))
		self.mgx = 0
		self.mgy = 0
		self.mgpicx = 0
		self.mgpicy = 0
		self.way = ""
		self.maze1 = maze1

	def move(self, way):
		if way == "right":
			
			if self.mgx == 14:
				pass

			elif self.maze1[self.mgy][self.mgx + 1] == ".": 
				self.mgx = self.mgx + 1
				self.mgpicx = self.mgx * 40

			elif self.maze1[self.mgy][self.mgx + 1] == "#":
				self.mgx = self.mgx + 0
			self.way = way
				
		if way == "left":
			if self.maze1[self.mgy][self.mgx - 1] == ".": 
				if self.mgx > 0:
					self.mgx = self.mgx - 1
					self.mgpicx = self.mgx * 40
				else:
					self.mgx = self.mgx + 0

			elif self.maze1[self.mgy][self.mgx - 1] == "#":
				self.mgx = self.mgx + 0
			self.way = way

		if way == "up":
			if self.maze1[self.mgy - 1][self.mgx] == ".": 
				if self.mgy > 0:
					self.mgy = self.mgy - 1
					self.mgpicy = self.mgy * 40
			self.way = way

		if way == "down":
			if self.maze1[self.mgy + 1][self.mgx] == ".": 
				if self.mgy < 14:
					self.mgy = self.mgy + 1
					self.mgpicy = self.mgy * 40
			self.way = way
