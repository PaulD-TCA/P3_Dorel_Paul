#! /usr/bin/env python3
# coding: utf-8

import pygame
import os

#main modules import
from MacGyverModules import class_MacGyver, class_GameW, class_Furnitures, class_GameOver, class_Maze, class_GameEvent

if __name__ == '__main__':
	
	#Instances creation
	maze = class_Maze.Maze()
	maze.mazecrea()# maze creation with maze data file and a class method inside class_Maze
	gameevent = class_GameEvent.GameEvent()
	macgyver = class_MacGyver.MacGyver(maze.mazestr)
	gamedpy = class_GameW.GameW(maze.mazestr)
	furniture = class_Furnitures.Furnitures(maze.mazestr)
	furniture.furnituresposition()# random layout of needle, pipe and ether
	gameover = class_GameOver.GameOver(gamedpy.mazedisplay)

	#Main game loop
	while gameevent.gameloop == True:

		gamedpy.mazedisplay()#Maze picture creation with an assemble of game pictures
		furniture.picking(macgyver.mgx,macgyver.mgy)#items picking with a comparison between Mac Gaver and item position
		gamedpy.gamew.blit(furniture.needle,(furniture.needleposition))#needle display
		gamedpy.gamew.blit(furniture.ether,(furniture.etherposition))#ether display
		gamedpy.gamew.blit(furniture.pipe,(furniture.pipeposition))#pipe display
		gamedpy.gamew.blit(furniture.syringe,(furniture.syringeposition))#syringe display
		furniture.syringecrafting(gamedpy.gamew, gamedpy.inv)#syringe crafting with the 3 other idems (needle, ether and pipe)
		gamedpy.gamew.blit(macgyver.mgpic,(macgyver.mgpicx + 6,macgyver.mgpicy))#Mac Gyver display and displacement
		gamedpy.gamew.blit(gameover.keeper,(gameover.keeperposition))#keeper position
		if gameover.endgame == 1:#maze display just after the end of the game
			gamedpy.mazedisplay()
		gameover.keeperneut(macgyver.mgx,macgyver.mgy,furniture.craftcompleting,gamedpy.gamew)#end screen display after the end of the game
		pygame.display.flip()#pygame display
		gameevent.getgameevent()#game event input (keyboard event and closing)
		macgyver.move(gameevent.way)#Mac Gyver displacement management

		continue