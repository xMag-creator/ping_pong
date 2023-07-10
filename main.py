import pgzrun
from random import randint, choice


# define palette class
class Palette:
    def __init__(self, palette, position, width=140, ball_width=10):
        """properties"""
        self.palette = palette
        self.palette.x = position[0]
        self.palette.y = position[1]
        self.palette.speed = 5
        self.palette.pcenter = width // 2
        self.palette.ball_width = ball_width

    def drawing(self):
        """draw object"""
        self.palette.draw()

    def move(self, direction):
        """move object"""
        if direction == "left":
            self.palette.x -= self.palette.speed
            if self.palette.x < self.palette.pcenter:
                self.palette.x = self.palette.pcenter + 5
        elif direction == "right":
            self.palette.x += self.palette.speed
            if self.palette.x > (WIDTH - self.palette.pcenter):
                self.palette.x = WIDTH - self.palette.pcenter + 5

    def bounce(self):
        """ball bouncing"""
        # if ball is too far from palette -> not bounce
        if self.palette.distance_to(ball) > self.palette.pcenter + self.palette.ball_width:
            return False

        # if palette is far that ball
        # in y axis -> not bounce
        if abs(self.palette.y - ball.y) > self.palette.ball_width * 2:
            return False

        # if ball hit palette
        if self.palette.x > ball.x and ball.direction_x == "left":
            ball.direction_x = "right"
        elif self.palette.x < ball.x and ball.direction_x == "right":
            ball.direction_x = "left"

        return True


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


def check_bounce():
    if palette_a.bounce():
        ball.direction_y = "down"
    if palette_b.bounce():
        ball.direction_y = "up"


def update_palettes():
    # player A
    if keyboard.a:
        palette_a.move("left")
    elif keyboard.s:
        palette_a.move("right")

    # player B
    if keyboard.k:
        palette_b.move("left")
    elif keyboard.l:
        palette_b.move("right")


def check_winner():
    if ball.winner:
        winner_txt = f"And the winner is: {ball.winner}"
        screen.draw.text(winner_txt, (WIDTH // 3, HEIGHT // 2), color="red", fontsize=60)


# start program
WIDTH = 1280
HEIGHT = 853
TITLE = "PONG - The best game ever ;)"


# define objects
palette_a = Palette(Actor("palette.png"), (randint(70, 1210), 10))
palette_b = Palette(Actor("palette.png"), (randint(70, 1210), 843))
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
    update_palettes()
    check_bounce()


def draw():
    # generating screen
    screen.blit("nature-2384_1280.jpg", (0, 0))
    palette_a.drawing()
    palette_b.drawing()
    ball.draw()
    check_winner()


pgzrun.go()
