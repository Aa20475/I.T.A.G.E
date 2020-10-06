import component as cp
import pygame as pg

import boxcomponent as bc
import textcomponent as tc


class Button(cp.NestedComponent):
	def __init__(self,disp,rect,rec=True,bcolor=(0,0,0),bhcolor=(-1,-1,-1),txt=True,text="sample",size=14,font='Calibri',tcolor=(0,0,0),thcolor=(-1,-1,-1),bold=True,italic=False,antialias=True,offset=(0,0)):
		super(Button,self).__init__(disp)
		if bhcolor==(-1,-1,-1):
			self.box  = bc.HoverBox(disp,rect.x,rect.y,rect.width,rect.height,bcolor,bcolor)
		else:
			self.box  = bc.HoverBox(disp,rect.x,rect.y,rect.width,rect.height,bcolor,bhcolor)
		if thcolor==(-1,-1,-1):
			self.text = tc.HoverText(disp,text,size,font,tcolor,tcolor,bold,italic,antialias,(rect.x+offset[0],rect.y+offset[1]))	
		else:
			self.text = tc.HoverText(disp,text,size,font,tcolor,thcolor,bold,italic,antialias,(rect.x+offset[0],rect.y+offset[1]))
		

		self.actions.append(self.hover)
		self.actions.append(self.click)
		self.clickscreen = None


	def render(self):
		self.box.render()
		self.text.render()

	def hover(self,event):
		x,y = pg.mouse.get_pos()
		self.box.changecolor(self.box.dims.collidepoint(x,y) or self.text.rect.collidepoint(x,y))
		self.text.changecolor(self.box.dims.collidepoint(x,y) or self.text.rect.collidepoint(x,y))


	def linkClick(self,screen):
		self.clickscreen=screen

	def click(self,event):
		if event.type ==  pg.MOUSEBUTTONDOWN:
			if event.button == 1:
				if self.clickscreen is not None:
					return self.clickscreen



