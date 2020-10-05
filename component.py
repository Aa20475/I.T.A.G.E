class Component(object):
	def __init__(self,disp):
		self.disp =disp
		self.actions = []

	def render(self):
		pass

class NestedComponent(Component):

	def __init__(self,disp):
		super(NestedComponent,self).__init__(disp)
		self.components = []

	def addComponent(self,component):
		self.components.append(component)
		for act in component.actions:
			self.actions.append(act)

	def render(self):
		for comp in self.components:
			comp.render()