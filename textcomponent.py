import component as cp
import pygame as pg


class Text(cp.Component):
	def __init__(self,disp,text="sample",size=14,font='Calibri',color=(0,0,0),bold=True,italic=False,antialias=True,pos=(0,0)):
		super(Text,self).__init__(disp)
		font = pg.font.SysFont(font,size, bold, italic)
		self.text = font.render(text,antialias,color)
		self.pos = pos

	def render(self):
		self.disp.blit(self.text,self.pos)


class HoverText(cp.Component):

	def __init__(self,disp,text="sample",size=14,font='Calibri',color=(0,0,0),hovercolor=(255,255,255),bold=True,italic=False,antialias=True,pos=(0,0)):
		super(HoverText,self).__init__(disp)
		self.idlecolor = color
		self.color = self.idlecolor
		self.hovercolor = hovercolor
		self.font = pg.font.SysFont(font,size, bold, italic)
		self.string = text
		self.antialias = antialias
		self.text = self.font.render(self.string,self.antialias,self.color)
		self.rect = pg.rect.Rect(pos,(self.text.get_width(),self.text.get_height()))

		self.pos = pos #can be removed?
		self.actions.append(self.hover)

	def render(self):
		self.text = self.font.render(self.string,self.antialias,self.color)
		self.disp.blit(self.text,self.pos)

	def hovercheck(self):
		if self.rect.collidepoint(pg.mouse.get_pos()):
			return True
		else:
			return False

	def hover(self,event):
		if self.hovercheck():
			self.color = self.hovercolor
		else:
			self.color = self.idlecolor