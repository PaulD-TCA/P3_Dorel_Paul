import os
import pygame


pathtofolder = os.path.abspath("")
pathtopics = os.path.join(pathtofolder, "Pictures")


class GameOver:
	def __init__(self,mazedisplay):

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
