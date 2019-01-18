#Arrows Management Package
from settings import *

class Arrows(object):
	"""docstring for Arrows"""

	ARROW_IMAGE_URL = "myResources/images/bullet.png"
	SHOOT_SOUND_URL = "myResources/audio/shoot.wav"
	ACCURACY = [0, 0]

	def __init__(self):
		self.arrows_speed = 40
		self.arrows = []
		self.loaded_arrow = pygame.image.load(Arrows.ARROW_IMAGE_URL)
		self.shoot = pygame.mixer.Sound(Arrows.SHOOT_SOUND_URL)
		self.shoot.set_volume(0.25)

	def drawArrows(self):
		for bullet in self.arrows:
			index=0
			velx=math.cos(bullet[0]) * self.arrows_speed
			vely=math.sin(bullet[0]) * self.arrows_speed
			bullet[1]+=velx
			bullet[2]+=vely
			if bullet[1]<-64 or bullet[1]>WINDOW_WIDTH or bullet[2]<-64 or bullet[2]>WINDOW_HEIGHT:
				self.arrows.pop(index)
			index+=1
			for projectile in self.arrows:
				arrow1 = pygame.transform.rotate(self.loaded_arrow, 360-projectile[0]*57.29)
				WINDOW.blit(arrow1, (projectile[1], projectile[2]))

	def playShoot(self):
		self.shoot.play()

	def addArrow(self, player_position):
		self.playShoot()
		playerpos1 = player_position
		position = pygame.mouse.get_pos()
		Arrows.ACCURACY[1] += 1
		self.arrows.append([math.atan2(position[1]-(playerpos1[1]+32), position[0]-(playerpos1[0]+26)), playerpos1[0], playerpos1[1]])


