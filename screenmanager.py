import screen as sc

import mainmenu as mm

class ScreenManager(object):

	def __init__(self, disp):
		self.disp = disp
		self.screen = mm.MainMenuScreen(disp)

	def render(self) -> sc.Screen:
		self.screen = self.screen.draw()