import pgzrun
from random import randint, choice


# define additional functions
def update_ball_position():
    # x axis update
    if ball.direction_x == "left":
        ball.x -= ball.speed
    elif ball.direction_x == "right":
        ball.x += ball.speed

    # y axis update
    if ball.direction_y == "up":
        ball.y -= ball.speed
    elif ball.direction_y == "down":
        ball.y += ball.speed

    # checking if ball hit something
    if ball.x < 5:
        ball.direction_x = "right"
    elif ball.x > WIDTH - 5:
        ball.direction_x = "left"

    # checking if someone win
    if ball.y < 5:
        ball.winner = "PLAYER B"
    elif ball.y > HEIGHT - 5:
        ball.winner = "PLAYER A"


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

# additional variables
ball.direction_x = choice(("left", "right"))
ball.direction_y = choice(("up", "down"))
ball.speed = 2
ball.winner = None


def update():
    # control functions
    update_ball_position()


def draw():
    # generating screen
    screen.blit("nature-2384_1280.jpg", (0, 0))
    palette_a.draw()
    palette_b.draw()
    ball.draw()


pgzrun.go()
