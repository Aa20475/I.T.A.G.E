import component as cp
import pygame as pg

class Box(cp.Component):
	def __init__(self,disp,x,y,l,b,color):
		super(Box,self).__init__(disp)
		self.dims = [x,y,l,b]
		self.color = color


	def render(self):
		pg.draw.rect(self.disp,self.color,self.dims)



class HoverBox(Box):
	def __init__(self,disp,x,y,l,b,color,hovercolor):
		super(HoverBox,self).__init__(disp,x,y,l,b,color)
		self.dims = pg.rect.Rect(x,y,l,b)
		self.idlecolor = color
		self.color = self.idlecolor
		self.hovercolor = hovercolor
		self.actions.append(self.hover)


	def render(self):
		pg.draw.rect(self.disp,self.color,self.dims)

	def changecolor(self,b):
		if b:
			self.color = self.hovercolor
		else:
			self.color = self.idlecolor


	def hover(self,event):
		self.changecolor(self.dims.collidepoint(pg.mouse.get_pos()))
			
