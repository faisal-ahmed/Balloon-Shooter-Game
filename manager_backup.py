from library import *


class Manager(object):
    """docstring for Manager"""

    BACKGROUND_IMAGE_URL = "myResources/images/background.jpg"
    GAMEOVER_IMAGE_URL = "myResources/images/gameover.png"
    YOUWIN_IMAGE_URL = "myResources/images/youwin.png"
    BACKGROUND_SOUND_URL = "resources/audio/moonlight.wav"

    def __init__(self):
        self.width = 640
        self.height = 480
        self.background = ""
        self.transformed_background = ""

    def prepareGameEnv():
        # 2 - Initialize the game
        pygame.init()
        pygame.mixer.init()
        screen = pygame.display.set_mode((self.width, self.height))
        self.loaded_background = pygame.image.load(Manager.BACKGROUND_IMAGE_URL)
        self.transformed_background = pygame.transform.scale(self.loaded_background, (self.width, self.height))

        pygame.mixer.music.load(Manager.BACKGROUND_SOUND_URL)
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.50)

        return screen
        


def main():
    # 3 - Load images
    manager = Manager()
    screen = manager.prepareGameEnv()


# 2 - Initialize the game
badtimer=100
badtimer1=0
badguys=[[480,370]]

# 3 - Load images
player = pygame.image.load("myResources/images/shooter.png")
arrow = pygame.image.load("myResources/images/bullet.png")
healthbar = pygame.image.load("myResources/images/healthbar.png")
health = pygame.image.load("myResources/images/health.png")
gameover = pygame.image.load("myResources/images/gameover.png")
youwin = pygame.image.load("myResources/images/youwin.png")

Red_Balloon = pygame.image.load("myResources/images/balloon/Red_Balloon.png")

player = pygame.transform.scale(player, (120, 120))
Red_Balloon = pygame.transform.scale(Red_Balloon, (80, 150))

# 3.1 - Load audio
hit = pygame.mixer.Sound("myResources/audio/explode.wav")
enemy = pygame.mixer.Sound("myResources/audio/enemy.wav")
shoot = pygame.mixer.Sound("myResources/audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)

# 4 - keep looping through
running = 1
exitcode = 0
while running:
    badtimer-=1
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(background, (0,0))
    screen.blit(castle,(160,370))
    screen.blit(castle,(320,370))
    screen.blit(castle,(480,370))

    # 6.1 - Set player position and rotation
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1) 

    # 6.2 - Draw arrows
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*arrowSpeed
        vely=math.sin(bullet[0])*arrowSpeed
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))

    # 6.3 - Draw badgers
    if badtimer==0:
#        badguys.append([160, random.randint(50,430)])
        badguys.append([160, 370])
        badtimer=100-(badtimer1*2)
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=5
    index=0
    for badguy in badguys:
        # if badguy[0]<-64:
        #     badguys.pop(index)
        # badguy[0]-=7
        badguy[1]-=7
        # 6.3.1 - Attack castle
        badrect=pygame.Rect(Red_Balloon.get_rect())
        badrect.top=badguy[1]
        badrect.left=badguy[0]
        if badrect.top<topWindowMargin:
            hit.play()
            healthvalue -= random.randint(5,20)
            badguys.pop(index)
        #6.3.2 - Check for collisions
        index1=0
        for bullet in arrows:
            bullrect=pygame.Rect(arrow.get_rect())
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]
            if badrect.colliderect(bullrect):
                enemy.play()
                acc[0]+=1
                badguys.pop(index)
                arrows.pop(index1)
            index1+=1
        # 6.3.3 - Next bad guy
        index+=1

    for badguy in badguys:
        screen.blit(Red_Balloon, badguy)

    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            shoot.play()
            position=pygame.mouse.get_pos()
            acc[1]+=1
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+60,playerpos1[1]+60])
