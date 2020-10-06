class ActionContainer(object):
	def __init__(self):
		self.actions = []

	def process(self,event):
		screen = None
		for action in self.actions:
			screen= action(event)
		return screen
