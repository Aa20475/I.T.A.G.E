import pygame as pg

class EventHandler(object):

	def __init__(self, screenmanager): 
		self.screenmanager =  screenmanager


	def update(self):
		for event in pg.event.get():
			if event.type ==pg.QUIT:
				return True

			screen  = self.screenmanager.screens.pop()
			result = screen.actioncontainer.process(event)
			self.screenmanager.screens.append(screen)

			if result is not None:
				self.screenmanager.screens.append(result)

