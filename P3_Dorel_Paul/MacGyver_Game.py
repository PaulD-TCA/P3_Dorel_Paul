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
from MacGyverModules import class_GameEvent


maze = class_Maze.Maze()
maze.mazecrea()
gameevent = class_GameEvent.GameEvent()
macgyver = class_MacGyver.MacGyver(maze.mazestr)

gamedpy = class_GameW.GameW(maze.mazestr)
furniture = class_Furnitures.Furnitures(maze.mazestr)
furniture.furnituresposition()
gameover = class_GameOver.GameOver(gamedpy.mazedisplay)

while gameevent.gameloop == True:

	gamedpy.mazedisplay()
	furniture.picking(macgyver.mgx,macgyver.mgy)

	gamedpy.gamew.blit(furniture.needle,(furniture.needleposition))
	gamedpy.gamew.blit(furniture.ether,(furniture.etherposition))
	gamedpy.gamew.blit(furniture.pipe,(furniture.pipeposition))
	gamedpy.gamew.blit(furniture.syringe,(furniture.syringeposition))
	furniture.syringecrafting(gamedpy.gamew, gamedpy.inv)
	gamedpy.gamew.blit(macgyver.mgpic,(macgyver.mgpicx + 6,macgyver.mgpicy))
	gamedpy.gamew.blit(gameover.keeper,(gameover.keeperposition))
	if gameover.endgame == 1:
		gamedpy.mazedisplay()
	gameover.keeperneut(macgyver.mgx,macgyver.mgy,furniture.craftcompleting,gamedpy.gamew)

	pygame.display.flip()

	gameevent.getgameevent()
	macgyver.move(gameevent.way)

	continue