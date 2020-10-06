import screen as sc
import boxcomponent as bc
import textcomponent as tc
import polygoncomponent as pc
import buttoncomponent as butc
import pygame as pg


class MainMenuScreen(sc.Screen):

	def __init__(self, disp):
		super(MainMenuScreen, self).__init__(disp)
		self.BG = (255,0,0)
		self.addComponent(bc.Box(disp,100,100,200,200,(0,0,0)))
		self.addComponent(bc.HoverBox(disp,300,300,200,200,(0,0,0),(255,255,255)))
		self.addComponent(tc.HoverText(disp,pos=(430,120)))
		self.addComponent(pc.Polygon(disp,[[500,500],[600,500],[500,600]]))
		button = butc.Button(disp,rect=pg.Rect(600,300,100,100),bcolor=(255,255,0),bhcolor=(0,0,0))
		button.linkClick(dummyscreen(disp))
		self.addComponent(button)


	def draw(self):
		self.disp.fill(self.BG)
		for comp in self.components:
			comp.render()
		return self


class dummyscreen(sc.Screen):
	def __init__(self,disp):
		super(dummyscreen,self).__init__(disp)

	def draw(self):
		self.disp.fill((0,255,0))