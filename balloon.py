#Balloon Management Package
from settings import *

class BalloonCastle(object):
	"""docstring for BalloonCastle"""
	
	CASTLE_IMAGE_URL = "myResources/images/castle.png"
	CASTLE_POSITIONS = [[270,530], [540,530], [810,530]]

	def __init__(self):
		self.castle = pygame.image.load(BalloonCastle.CASTLE_IMAGE_URL)
		self.blitCastle()

	def blitCastle(self):
		for position in BalloonCastle.CASTLE_POSITIONS:
			WINDOW.blit(self.castle, position)

	def fireBalloon(self, balloonHolder, player, arrows):
		arrowHolder = arrows.arrows
		index=0

		for balloon in balloonHolder:
			if balloon.balloon_initial_position[0]<-64:
				balloonHolder.pop(index)

			balloon.balloon_initial_position[1] -= 10
			# 6.3.1 - Attack castle
			balloonRect = pygame.Rect(balloon.transformed_balloon.get_rect())
			balloonRect.top = balloon.balloon_initial_position[1]
			balloonRect.left = balloon.balloon_initial_position[0]
			if balloonRect.top < TOP_WINDOW_MARGIN:
				balloon.playHit()
				player.health_value -= balloon.hit_value
				balloonHolder.pop(index)
			#6.3.2 - Check for collisions
			index1 = 0
			for bullet in arrowHolder:
				bullrect = pygame.Rect(arrows.loaded_arrow.get_rect())
				bullrect.left=bullet[1]
				bullrect.top=bullet[2]
				if balloonRect.colliderect(bullrect):
					balloon.playEnemy()
					Arrows.ACCURACY[0] += 1
					if (balloon.hit_value == 0):
						player.health_value -= 100
					balloonHolder.pop(index)
					arrowHolder.pop(index1)
				index1 += 1
			# 6.3.3 - Next bad guy
			index += 1

		for balloon in balloonHolder:
			WINDOW.blit(balloon.transformed_balloon, balloon.balloon_initial_position)

class Balloon(object):
	"""docstring for Balloon"""

	BALLOON_TYPE = ["Blue_Balloon", "Green_Balloon", "Purple_Balloon", "Red_Balloon", "Yellow_Balloon", "Red_Giant_Balloon", "Dark_Blue_Giant_Balloon", "Danger_Balloon"]
	BALLOON_BASE_URL = "myResources/images/balloon/"
	BALLOON_SIZE = (60, 150)
	BALLOON_HIT_SOUND_URL = "myResources/audio/explode.wav"
	BALLOON_DESTROY_SOUND_URL = "myResources/audio/enemy.wav"	
	BALLOON_POSITIONS = [[270,520], [540,520], [810,520]]

	def __init__(self, balloon_castle = 0, selected_balloon = 0):
		super(Balloon, self).__init__()
		position = Balloon.BALLOON_POSITIONS[balloon_castle]
		self.balloon_initial_position = [position[0]+random.randint(0,10), position[1]+random.randint(0,10)]
		self.balloon_image_url = Balloon.BALLOON_BASE_URL + Balloon.BALLOON_TYPE[selected_balloon] + ".png"
		self.loaded_balloon = pygame.image.load(self.balloon_image_url)
		self.transformed_balloon = pygame.transform.scale(self.loaded_balloon, Balloon.BALLOON_SIZE)

		if (len(Balloon.BALLOON_TYPE) == (selected_balloon+1)):
			self.hit_value = 0
		else:
			self.hit_value = selected_balloon * 5
		self.hit = pygame.mixer.Sound(Balloon.BALLOON_HIT_SOUND_URL)
		self.hit.set_volume(0.25)
		self.enemy = pygame.mixer.Sound(Balloon.BALLOON_DESTROY_SOUND_URL)
		self.enemy.set_volume(0.25)

	def playHit(self):
		self.hit.play()

	def playEnemy(self):
		self.enemy.play()
