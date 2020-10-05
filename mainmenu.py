import screen as sc
import boxcomponent as bc
import textcomponent as tc
import polygoncomponent as pc
import buttoncomponent as butc


class MainMenuScreen(sc.Screen):

	def __init__(self, disp):
		super(MainMenuScreen, self).__init__(disp)
		self.BG = (255,0,0)
		self.addComponent(bc.Box(disp,100,100,200,200,(0,0,0)))
		self.addComponent(bc.HoverBox(disp,300,300,200,200,(0,0,0),(255,255,255)))
		self.addComponent(tc.HoverText(disp,pos=(430,120)))
		self.addComponent(pc.Polygon(disp,[[500,500],[600,500],[500,600]]))
		self.addComponent(butc.Button(disp,bc.HoverBox(disp,300,50,200,200,(0,0,0),(255,255,255)),tc.HoverText(disp,pos=(340,200))))


	def draw(self):
		self.disp.fill((255,0,0))
		for comp in self.components:
			comp.render()
		return self