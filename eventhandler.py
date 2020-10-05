import pygame as pg

class EventHandler(object):

	def __init__(self, screenmanager): 
		self.screenmanager =  screenmanager


	def update(self):
		for event in pg.event.get():
			if event.type ==pg.QUIT:
				return True

			self.screenmanager.screen.actioncontainer.process(event)
