import os
import pygame
import random


pathtofolder = os.path.abspath("")
pathtopics = os.path.join(pathtofolder, "Pictures")
pathtomodules = os.path.join(pathtofolder, "MacGyverModules", "MazeLevel1.data")

class Furnitures:

	def __init__(self,maze):
			
			#self.pathtopics = pathtopics
			self.needle = pygame.image.load(pathtopics + "/aiguille.png")
			self.needle = pygame.transform.scale(self.needle,(40,40))

			self.ether = pygame.image.load(pathtopics + "/ether.png")
			self.ether = pygame.transform.scale(self.ether,(40,40))

			self.syringe = pygame.image.load(pathtopics + "/seringue.png")
			self.syringe = pygame.transform.scale(self.syringe,(40,40))

			self.pipe = pygame.image.load("Pictures/tube_plastique.png")
			self.pipe = pygame.transform.scale(self.pipe,(40,40))

			self.maze = maze

			self.needleposition = (560,0)
			self.etherposition = (560,280)
			self.pipeposition = (0,560)
			self.syringeposition = (1000,1000)

			self.needlepiked = 0
			self.etherpiked = 0
			self.pipepiked = 0
			self.craftcompleting = 0

	def picking(self,px,py):

		if (px*40,py*40) == self.needleposition:
			self.needleposition = (0,620)
			self.needlepiked = 1
			self.craftcompleting = self.needlepiked + self.etherpiked + self.pipepiked

		elif (px*40,py*40) == self.etherposition:
			self.etherposition = (40,620)
			self.etherpiked = 1
			self.craftcompleting = self.needlepiked + self.etherpiked + self.pipepiked
		elif (px*40,py*40) == self.pipeposition:
			self.pipeposition = (80,620)
			self.pipepiked = 1
			self.craftcompleting = self.needlepiked + self.etherpiked + self.pipepiked

	def syringecrafting(self):

		if self.needlepiked + self.etherpiked + self.pipepiked == 3:
			self.syringeposition = (120,620)

	def furnituresposition(self):

		rowposi = []
		rowcounter = 0

		for rows in self.maze:
			rowcountercolo = 0
			columnposi = []
			for colo in rows:
				if colo == ".":
					columnposi.append((rowcountercolo, rowcounter))
					rowcountercolo = rowcountercolo + 1
				else:
					rowcountercolo = rowcountercolo + 1
		
			rowcounter = rowcounter + 1

			rowposi.extend(columnposi)

		listtorandompick = rowposi[1:116]

		needlerandomposi = random.choice(listtorandompick)
		
		listtorandompick.remove(needlerandomposi)
		needlecase = (needlerandomposi[0]*40,needlerandomposi[1]*40)

		self.needleposition = needlecase

		etherrandomposi = random.choice(listtorandompick)
		ethercase = (etherrandomposi[0]*40,etherrandomposi[1]*40)

		self.etherposition = ethercase
		listtorandompick.remove(etherrandomposi)
		piperandomposi = random.choice(listtorandompick)
		pipecase = (piperandomposi[0]*40,piperandomposi[1]*40)
		self.pipeposition = pipecase