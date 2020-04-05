import os
import pygame

pathtofolder = os.path.abspath("")
pathtopics = os.path.join(pathtofolder, "Pictures")

class GameW:
	def __init__(self,maze):
		#self.pathtopics = pathtopics
		self.gamew = pygame.display.set_mode((600,660))
		self.wall = pygame.image.load(pathtopics + "/structures.png").subsurface(200,40,40,40)
		
		self.floor = pygame.image.load(pathtopics + "/floor-tiles-20x20.png")
		self.floor1 = self.floor.subsurface(120,60,20,20)

		self.inv = self.floor.subsurface(160,40,20,20)
		self.inv = pygame.transform.scale(self.inv,(40,40))
		self.invsep = self.floor.subsurface(380,180,20,20)
		self.maze = maze


	def mazedisplay(self):

		mazeindex = 0
		for mazei in self.maze:
			
			mazecolumn = 0
			for sprite in mazei:
				x = mazecolumn * 40
				y = mazeindex * 40

				if sprite == "#":
					self.gamew.blit(self.wall, (x,y))
				if sprite == ".":
					self.gamew.blit(self.floor1, (x,y))
					self.gamew.blit(self.floor1, (x+20,y+20))
					self.gamew.blit(self.floor1, (x+20,y))
					self.gamew.blit(self.floor1, (x,y+20))
				if sprite == "I":
					self.gamew.blit(self.inv, (x+0,y+20))
					self.gamew.blit(self.invsep, (x+0,y+0))
					self.gamew.blit(self.invsep, (x+20,y+0))

										
				mazecolumn = mazecolumn + 1
					
			mazeindex = mazeindex + 1	
