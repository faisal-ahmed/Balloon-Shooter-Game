from settings import *

class Manager(object):
    """docstring for Manager"""

    BACKGROUND_IMAGE_URL = "myResources/images/background.jpg"
    GAMEOVER_IMAGE_URL = "myResources/images/gameover.png"
    YOUWIN_IMAGE_URL = "myResources/images/youwin.png"
    BACKGROUND_SOUND_URL = "myResources/audio/moonlight.wav"
    GAME_RUNNING = True
    GAME_EXITCODE = False

    def __init__(self, eventHandler):
        self.background = ""
        self.transformed_background = ""
        self.eventHandler = eventHandler
        self.gameover_image = pygame.image.load(Manager.GAMEOVER_IMAGE_URL)
        self.gameover = pygame.transform.scale(self.gameover_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.youwin_image = pygame.image.load(Manager.YOUWIN_IMAGE_URL)
        self.youwin = pygame.transform.scale(self.youwin_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    def loadBackgroundMusic(self):
        # Load Initial Music
        pygame.mixer.music.load(Manager.BACKGROUND_SOUND_URL)
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.50)

    def loadBackgroundImage(self):
        # 2 - Initialize the game
        self.loaded_background = pygame.image.load(Manager.BACKGROUND_IMAGE_URL)
        self.transformed_background = pygame.transform.scale(self.loaded_background, (WINDOW_WIDTH, WINDOW_HEIGHT))
        WINDOW.blit(self.transformed_background,(0,0))

    def play(self):
        # 5 - clear the screen before drawing it again
        WINDOW.fill(0)
        accuracy = 0
        player = Player()
        arrows = Arrows()
        castle = BalloonCastle()
        types_of_balloon = len(Balloon.BALLOON_TYPE)
        balloonTimer = 50
        balloonTimer1 = 0
        balloonHolder = []
        #First Balloon
        castle_no = random.randint(0, 2)
        balloon_no = random.randint(0, (types_of_balloon-1) )
        balloon = Balloon(castle_no, balloon_no)
        balloonHolder.append(balloon)

        while Manager.GAME_RUNNING:
            balloonTimer -= 1
            self.loadBackgroundImage()
            player.rotatePlayer()
            castle.blitCastle()
            arrows.drawArrows()
            if balloonTimer == 0:
                castle_no = random.randint(0, 2)
                balloon_no = random.randint(0, (types_of_balloon-1) )
                balloon = Balloon(castle_no, balloon_no)
                balloonHolder.append(balloon)

                #Random timing for balloon addition
                balloonTimer = 100 - (balloonTimer1 * 2)
                if balloonTimer1 >= 25:
                    balloonTimer1 = 25
                else:
                    balloonTimer1 += 5

            castle.fireBalloon(balloonHolder, player, arrows)

            #player.drawClock()
            player.healthBar()

            # 7 - update the screen
            pygame.display.flip()

            # 8 - catch events
            self.eventHandler.catchEvents(player, arrows)

            #10 - Win/Lose check
            if pygame.time.get_ticks() >= 90000:
                Manager.GAME_RUNNING = False
                Manager.GAME_EXITCODE = True
            if player.health_value <= 0:
                Manager.GAME_RUNNING = False
                Manager.GAME_EXITCODE = False
            if Arrows.ACCURACY[1] != 0:
                accuracy = Arrows.ACCURACY[0]*1.0 / Arrows.ACCURACY[1]*100
            else:
                accuracy = 0
        
        # 11 - Win/lose display
        if Manager.GAME_EXITCODE == 0:
            pygame.font.init()
            font = pygame.font.Font(None, 24)
            text = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
            textRect = text.get_rect()
            textRect.centerx = WINDOW.get_rect().centerx
            textRect.centery = WINDOW.get_rect().centery+24
            WINDOW.blit(self.gameover, (0,0))
            WINDOW.blit(text, textRect)
        else:
            pygame.font.init()
            font = pygame.font.Font(None, 24)
            text = font.render("Accuracy: "+str(accuracy)+"%", True, (0,255,0))
            textRect = text.get_rect()
            textRect.centerx = WINDOW.get_rect().centerx
            textRect.centery = WINDOW.get_rect().centery+24
            WINDOW.blit(self.youwin, (0,0))
            WINDOW.blit(text, textRect)

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

            self.button("QUIT", 470, 420, 150, 60, green, bright_green, 2)
            pygame.display.flip()


    def button(self, msg, x, y, w, h, ic, ac, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(WINDOW, ac, (x, y, w, h))
            if click[0] == 1 and action == Manager.GAME_RUNNING:
                self.play()
            elif click[0] == 1 and action == Manager.GAME_EXITCODE:
                pygame.quit()
                exit(0)
            elif click[0] == 1 and action == 2:
                pygame.quit()
                exit(0)

        else:
            pygame.draw.rect(WINDOW, ic, (x, y, w, h))

        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        WINDOW.blit(textSurf, textRect)

    def startSplashScreen(self):
        self.loadBackgroundMusic()
        self.loadBackgroundImage()
        while Manager.GAME_RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                    
            largeText = pygame.font.SysFont("comicsansms",115)
            TextSurf, TextRect = self.text_objects("Balloon Shooter Game", largeText)
            TextRect.center = ((WINDOW_WIDTH/2), (WINDOW_HEIGHT/2))
            WINDOW.blit(TextSurf, TextRect)

            self.button("START!", 280, 450, 150, 60, green, bright_green, Manager.GAME_RUNNING)
            self.button("QUIT", 640, 450, 150, 60, red, bright_red, Manager.GAME_EXITCODE)

            pygame.display.update()
            CLOCK.tick(15)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

def main():
    eventHandler = Events()
    manager = Manager(eventHandler)
    manager.startSplashScreen()

main()