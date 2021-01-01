import pygame
import random as r
# from Network imoprt Network
pygame.init()

win = pygame.display.set_mode((700,400))
clock = pygame.time.Clock()

#load music & sound effects
hit_sound = pygame.mixer.Sound('badass music/bullet.mp3')
bg_music = pygame.mixer.music.load('badass music/batman.mp3')
pygame.mixer.music.play(fade_ms=10000)


class player1():
	# LEFT PLAYER

	def __init__(self):
		self.x, self.y = 15,175
		self.speed = 10

	def draw(self):
		pygame.draw.rect(win,(255,255,255), (self.x,self.y, 10, 50))

	def move(self):
		if keys[pygame.K_w] and player1.y > 0:
			player1.y -= player1.speed
		elif keys[pygame.K_s] and player1.y < 350:
			player1.y += player1.speed


class player2(player1):
	#RIGHT PLAYER

	def __init__(self):
		super().__init__()
		self.x = 670

	def move(self):
		if keys[pygame.K_UP] and player2.y > 0:
			player2.y -= player2.speed
		elif keys[pygame.K_DOWN] and player2.y < 350:
			player2.y += player2.speed	


class boom_ball():

	def __init__(self):
		self.x, self.y = 350, 200
		self.speed = r.choices([-10,10],k=2)      #ball speed = 10


	def draw(self):
		pygame.draw.circle(win,(255,255,255), (self.x,self.y), 7)

	def move(self):
		if (self.x - 7 <= player1.x + 10) and (player1.y <= self.y <= player1.y + 50):   #ball collides with player
			self.speed[0] = -self.speed[0]
			hit_sound.play()
		elif (self.x + 7 >= player2.x) and (player2.y <= self.y <= player2.y + 50):  #ball collides with player
			self.speed[0] = -self.speed[0]
			hit_sound.play()
		elif (self.y - 7 < 20) or (self.y + 7 > 380):
			self.speed[1] = -self.speed[1]
		elif self.x > 680 or self.x < 15:
			self.point_lost()

		self.x += self.speed[0] 
		self.y += self.speed[1]

	def point_lost(self):
		font = pygame.font.SysFont('comicsans',50)
		text = font.render('LETS GO AGAIN', 1, (255,0,0))
		win.blit(text, (350-text.get_width()//2, 200))
		pygame.display.update()
		pygame.time.delay(1500)
		self.__init__()
		player1.__init__()
		player2.__init__()

	

def draw_stuff():
	win.fill((0,0,0))
	player1.draw()
	player2.draw()
	ball.draw()
	pygame.display.update()

def str_to_tup(arr):
	arr = arr.split(",")
	return int(arr[0]) , int(arr[1])

def tup_to_str(tup):
	return str(tup[0]) + "," + str(tup[1])


# net = Network()
# start_pos = str_to_tup(net.get_pos())

# player initiation
player1 = player1()
player2 = player2()
ball = boom_ball()


run = True
while run:
	
	clock.tick(35)

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	player1.move()
	player2.move()
	ball.move()

	draw_stuff()

pygame.quit()

