import actioncontainer as ac

class Screen(object):

	def __init__(self,disp):
		self.disp = disp
		self.actioncontainer = ac.ActionContainer()
		self.components = []
		self.BG = (255,255,255)

	def draw(self):
		#comp.render() for comp in self.components
		pass


	def addComponent(self,component):
		self.components.append(component)
		for act in component.actions:
			self.actioncontainer.actions.append(act)