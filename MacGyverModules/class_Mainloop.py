import pygame

class Mainloop:

	def gamemainloop(self,gameevent,macgyver,gamedpy, furniture, gameover):

		while gameevent.gameloop == True:
			gamedpy.mazedisplay()#Maze picture creation with an assemble of game pictures
			gamedpy.gamew.blit(furniture.needle,(furniture.needleposition))#needle display
			gamedpy.gamew.blit(furniture.ether,(furniture.etherposition))#ether display
			gamedpy.gamew.blit(furniture.pipe,(furniture.pipeposition))#pipe display
			gamedpy.gamew.blit(furniture.syringe,(furniture.syringeposition))#syringe display
			gamedpy.gamew.blit(macgyver.mgpic,(macgyver.mgpicx + 6,macgyver.mgpicy))#Mac Gyver display and displacement
			furniture.picking(macgyver.mgx,macgyver.mgy)#items picking with a comparison between Mac Gaver and item position
			gamedpy.gamew.blit(gameover.keeper,(gameover.keeperposition))#keeper position
			if gameover.endgame == 1:#maze display just after the end of the game
				gamedpy.mazedisplay()
			gameover.keeperneut(macgyver.mgx,macgyver.mgy,furniture.craftcompleting,gamedpy.gamew)#end screen display after the end of the game
			macgyver.move(gameevent.way)#Mac Gyver displacement management
			furniture.syringecrafting(gamedpy.gamew, gamedpy.inv)#syringe crafting with the 3 other idems (needle, ether and pipe)
			pygame.display.flip()#pygame display
			gameevent.getgameevent()#game event input (keyboard event and closing)

			continue
