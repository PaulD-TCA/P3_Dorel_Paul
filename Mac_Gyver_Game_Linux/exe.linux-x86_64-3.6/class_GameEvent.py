import pygame

class GameEvent:

  def __init__(self):
    self.gameloop = True
    self.way = "way1"
    self.way2 = "way2"

  def getgameevent(self):

    self.way2 = 1
    if self.way2 == 1:
      self.way = ""
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        self.gameloop = False
      if event.type == pygame.KEYDOWN:
        self.way2 = 0
        if self.way2 == 0:
          if event.key == pygame.K_RIGHT:
            self.way = "right"
          if event.key == pygame.K_LEFT:
            self.way = "left"
          if event.key == pygame.K_UP:
            self.way = "up"
          if event.key == pygame.K_DOWN:
            self.way = "down"