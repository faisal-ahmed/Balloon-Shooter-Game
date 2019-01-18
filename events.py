#Events Management Package
from settings import *

class Events(object):
	"""docstring for Events"""

	def __init__(self):
		print ("Event Handler Started")

	def catchEvents(self, player, arrows):
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            pygame.quit() 
	            exit(0)
	        if event.type == pygame.MOUSEBUTTONDOWN:
	        	arrows.addArrow(player.PLAYER_POSITION)

