class ActionContainer(object):
	def __init__(self):
		self.actions = []

	def process(self,event):
		for action in self.actions:
			action(event); 
