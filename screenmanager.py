import screen as sc

import mainmenu as mm

class ScreenManager(object):

	def __init__(self, disp):
		self.disp = disp
		self.screens = []

	def render(self) -> sc.Screen:
		screen  = self.screens.pop()
		screen.draw()
		self.screens.append(screen)

