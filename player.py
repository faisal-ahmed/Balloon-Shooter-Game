#Player Management Package
from settings import *

class Player(object):
	"""docstring for Player"""

	PLAYER_IMAGE_URL = "myResources/images/shooter.png"
	HEALTHBAR_IMAGE_URL = "myResources/images/healthbar.png"
	HEALTH_IMAGE_URL = "myResources/images/health.png"
	PLAYER_POSITION = [80, 80]
	PLAYER_SIZE = (120, 120)

	def __init__(self):
		self.health_value = 194 #194
		self.loaded_player = pygame.image.load(Player.PLAYER_IMAGE_URL)
		self.transformed_player = pygame.transform.scale(self.loaded_player, Player.PLAYER_SIZE)
		self.healthbar = pygame.image.load(Player.HEALTHBAR_IMAGE_URL)
		self.health = pygame.image.load(Player.HEALTH_IMAGE_URL)

	def rotatePlayer(self):
		position = pygame.mouse.get_pos()
		angle = math.atan2(position[1]-(Player.PLAYER_POSITION[1]+32), position[0]-(Player.PLAYER_POSITION[0]+26))
		playerrot = pygame.transform.rotate(self.transformed_player, 360-angle*57.29)
		playerpos1 = (Player.PLAYER_POSITION[0]-playerrot.get_rect().width/2, Player.PLAYER_POSITION[1]-playerrot.get_rect().height/2)
		WINDOW.blit(playerrot, playerpos1)

	def healthBar(self):
		WINDOW.blit(self.healthbar, (5,5))
		for health1 in range(self.health_value):
			WINDOW.blit(self.health, (health1+8, 8))

	def drawClock(self):
		# 6.4 - Draw clock
		font = pygame.font.Font(None, 24)
		survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
		textRect = survivedtext.get_rect()
		textRect.topright=[635,5]
		WINDOW.blit(survivedtext, textRect)


