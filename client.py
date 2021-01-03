import pygame
import random as r
import pickle
from Network import Network
from Player import Player
pygame.init()

win = pygame.display.set_mode((700,400))
clock = pygame.time.Clock()

#load music & sound effects
hit_sound = pygame.mixer.Sound('badass music/bullet.mp3')
bg_music = pygame.mixer.music.load('badass music/batman.mp3')
pygame.mixer.music.play(fade_ms=10000)


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
	player1.draw(win)
	player2.draw(win)
	# ball.draw()
	pygame.display.update()


net = Network()                                            # connect to server
#player initiation
player1, player2 = net.get_players()
# ball = boom_ball()


run = True
while run:
	
	clock.tick(35)

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run = False
	
	player1.move()
	# ball.move()
	net.send(player1)                                 # send my pos 
	player2 = net.receive()                           # update player

	draw_stuff()

pygame.quit()

