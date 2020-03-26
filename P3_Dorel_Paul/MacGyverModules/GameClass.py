import os
import pygame


pathtofolder = os.path.abspath("")
pathtopics = os.path.join(pathtofolder, "Pictures")
pathtomodules = os.path.join(pathtofolder, "MacGyverModules", "MazeLevel1.data")

class Furnitures:

	def __init__(self):
			
			#self.pathtopics = pathtopics
			self.needle = pygame.image.load(pathtopics + "/aiguille.png")
			self.needle = pygame.transform.scale(self.needle,(40,40))

			self.ether = pygame.image.load(pathtopics + "/ether.png")
			self.ether = pygame.transform.scale(self.ether,(40,40))

			self.syringe = pygame.image.load(pathtopics + "/seringue.png")
			self.syringe = pygame.transform.scale(self.syringe,(40,40))

			self.pipe = pygame.image.load("Pictures/tube_plastique.png")
			self.pipe = pygame.transform.scale(self.pipe,(40,40))

			self.needleposition = (560,0)
			self.etherposition = (560,280)
			self.pipeposition = (0,560)
			self.syringeposition = (1000,1000)

			self.needlepiked = 0
			self.etherpiked = 0
			self.pipepiked = 0
			self.craftcompleting = 0

	def picking(self,px,py):

		if px == 14 and py == 0:
			self.needleposition = (0,620)
			self.needlepiked = 1
			self.craftcompleting = self.needlepiked + self.etherpiked + self.pipepiked

		elif px == 14 and py == 7:
			self.etherposition = (40,620)
			self.etherpiked = 1
			self.craftcompleting = self.needlepiked + self.etherpiked + self.pipepiked
		elif px == 0 and py == 14:
			self.pipeposition = (80,620)
			self.pipepiked = 1
			self.craftcompleting = self.needlepiked + self.etherpiked + self.pipepiked

	def syringecrafting(self):

		if self.needlepiked + self.etherpiked + self.pipepiked == 3:
			self.syringeposition = (120,620)

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

class GameOver:
	def __init__(self):

		#self.pathtopics = pathtopics
		self.keeper = pygame.image.load(pathtopics + "/Gardien.png")
		self.keeperposition = (564,561)
		self.loosepic = pygame.image.load(pathtopics + "/loose.png")
		self.loosepic = pygame.transform.scale(self.loosepic,(400,400))

		self.winpic = pygame.image.load(pathtopics + "/win.png")
		self.winpic = pygame.transform.scale(self.winpic,(400,400))
		self.endgame = 0

	def keeperneut(self, mx,my,syringe,gamew):
		if mx == 14 and my == 14:
			if syringe == 3:
				gamew.blit(self.winpic, (100,100))
				self.endgame = 1
				self.keeperposition = (160,660)

		if mx == 14 and my == 14:
			if syringe != 3:
				gamew.blit(self.loosepic, (100,100))
				self.endgame = 1

#class GameW:
#	def __init__(self,mazo):
#		#self.pathtopics = pathtopics
#		self.gamew = pygame.display.set_mode((600,660))
#		self.wall = pygame.image.load(pathtopics + "/structures.png").subsurface(200,40,40,40)
		
#		self.floor = pygame.image.load(pathtopics + "/floor-tiles-20x20.png")
#		self.floor1 = self.floor.subsurface(120,60,20,20)

#		self.inv = self.floor.subsurface(160,40,20,20)
#		self.inv = pygame.transform.scale(self.inv,(40,40))
#		self.invsep = self.floor.subsurface(380,180,20,20)
#		self.mamazo = mazo


#	def mazedisplay(self):
#		mazeindex = 0
#		for mazei in self.mamazo:
			
#			mazecolumn = 0
#			for sprite in mazei:
#				x = mazecolumn * 40
#				y = mazeindex * 40

#				if sprite == "#":
#					self.gamew.blit(self.wall, (x,y))
#				if sprite == ".":
#					self.gamew.blit(self.floor1, (x,y))
#					self.gamew.blit(self.floor1, (x+20,y+20))
#					self.gamew.blit(self.floor1, (x+20,y))
#					self.gamew.blit(self.floor1, (x,y+20))
#				if sprite == "I":
#					self.gamew.blit(self.inv, (x+0,y+20))
#					self.gamew.blit(self.invsep, (x+0,y+0))
#					self.gamew.blit(self.invsep, (x+20,y+0))

										
#				mazecolumn = mazecolumn + 1
					
#			mazeindex = mazeindex + 1	
