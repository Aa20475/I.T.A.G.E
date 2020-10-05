import component as cp
import pygame as pg

class Polygon(cp.Component):
	def __init__(self,disp,vertices,color=(0,0,0),width=0):
		super(Polygon,self).__init__(disp)
		self.vertices = vertices
		self.color =color
		self.width =width

	def render(self):
		pg.draw.polygon(self.disp,self.color,self.vertices,self.width)
