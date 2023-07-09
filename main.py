import pgzrun
from random import randint


# start program
WIDTH = 1280
HEIGHT = 853
TITLE = "PONG - The best game ever ;)"


# define objects
palette_a = Actor("palette.png")
palette_a.y = 10
palette_a.x = randint(70, 1210)
palette_b = Actor("palette.png")
palette_b.y = 843
palette_b.x = randint(70, 1210)
ball = Actor("ball.png")
ball.y = HEIGHT // 2
ball.x = WIDTH // 2


def update():
    # control functions

    pass


def draw():
    # generating screen

    screen.blit("nature-2384_1280.jpg", (0, 0))
    palette_a.draw()
    palette_b.draw()
    ball.draw()


pgzrun.go()
