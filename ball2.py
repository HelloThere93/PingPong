import pgzrun

WIDTH = 500
HEIGHT = 500
score = 0
ball = Rect((150,400), (30,30))
bat = Rect((200,480), (60, 20))
speedx = 2
speedy = 2

def draw():
    screen.clear()
    screen.draw.filled_rect(ball, "red")
    screen.draw.filled_rect(bat, "gray")
    screen.draw.text("Score Is: "+str(score), (50, 50), color = "white" )

def update():
    global speedx, speedy, score
    ball.x += speedx
    ball.y += speedy
    if ball.colliderect(bat):
        speedy = -speedy
        score += 100
    if ball.right > WIDTH or ball.left < 0:
        speedx = -speedx
    if ball.top < 0:
        speedy = -speedy
    if ball.bottom > HEIGHT:
        exit()
    if (keyboard.right):
        bat.x += 2
    if (keyboard.left):
        bat.x -= 2

pgzrun.go()