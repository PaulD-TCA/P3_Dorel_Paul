#! /usr/bin/env python3
# coding: utf-8

import pygame
import os

#main modules import
from MacGyverModules import class_MacGyver, class_GameW, class_Furnitures, class_GameOver, class_Maze, class_GameEvent, class_Mainloop

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
	maingameloop = class_Mainloop.Mainloop()
	maingameloop.gamemainloop(gameevent, macgyver, gamedpy, furniture, gameover)