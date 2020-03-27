#! /usr/bin/env python3
# coding: utf-8

import pygame
import os
import random

from MacGyverModules import class_MacGyver
from MacGyverModules import class_GameW
from MacGyverModules import class_Furnitures
from MacGyverModules import class_GameOver
from MacGyverModules import class_Maze


maze = class_Maze.Maze()
maze.mazecrea()
macgyver = class_MacGyver.MacGyver(maze.mazestr)
gameover = class_GameOver.GameOver()
gamedpy = class_GameW.GameW(maze.mazestr)

furniture = class_Furnitures.Furnitures(maze.mazestr)


furniture.furnituresposition()

gameloop = True

while gameloop == True:
	for event in pygame.event.get():
			gamedpy.mazedisplay()
			furniture.picking(macgyver.mgx,macgyver.mgy)

			gamedpy.gamew.blit(furniture.needle,(furniture.needleposition))
			gamedpy.gamew.blit(furniture.ether,(furniture.etherposition))
			gamedpy.gamew.blit(furniture.pipe,(furniture.pipeposition))

			gamedpy.gamew.blit(furniture.syringe,(furniture.syringeposition))
			furniture.syringecrafting()
			if furniture.craftcompleting == 3:
				gamedpy.gamew.blit(gamedpy.inv,(0,620))
				gamedpy.gamew.blit(gamedpy.inv,(40,620))
				gamedpy.gamew.blit(gamedpy.inv,(80,620))
			gamedpy.gamew.blit(macgyver.mgpic,(macgyver.mgpicx + 6,macgyver.mgpicy))
			gamedpy.gamew.blit(gameover.keeper,(gameover.keeperposition))
			if gameover.endgame == 1:
				gamedpy.mazedisplay()
			gameover.keeperneut(macgyver.mgx,macgyver.mgy,furniture.craftcompleting,gamedpy.gamew)

			pygame.display.flip()

			if event.type == pygame.QUIT:
				gameloop = False
 
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					macgyver.move("right")
				if event.key == pygame.K_LEFT:
					macgyver.move("left")
				if event.key == pygame.K_UP:
					macgyver.move("up")
				if event.key == pygame.K_DOWN:
					macgyver.move("down")
				
	continue


