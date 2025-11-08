
import turtle
import random

score = 0

scr = turtle.Screen()
scr.title("Space Game")
scr.bgpic("space_invaders_background.gif")
scr.setup(800,800)
scr.tracer(0)

scr.register_shape("player.gif")
scr.register_shape("invader.gif")

player = turtle.Turtle()
player.shape("player.gif")
player.penup()
player.goto(0,-275)

no_enemies = 5
enemies = []
for i in range(no_enemies):
    enemy = turtle.Turtle()
    enemy.shape("invader.gif")
    enemy.penup()
    x = random.randint(-270,270)
    y = random.randint(150,275)
    enemy.goto(x,y)
    enemies.append(enemy)
enemyspeed = 0.2


bullet = turtle.Turtle()
bullet.shape("triangle")
bullet.color("yellow")
bullet.setheading(90)
bullet.shapesize(.5)
bullet.penup()
bullet.goto(0,-265)
bulletstate = "ready"
#ready - ready for the shoot
#fire - already in movement
bulletspeed = 2
bullet.hideturtle()

pen = turtle.Turtle()
pen.color("yellow")
pen.shape("square")
pen.penup()
pen.goto(0,340)
pen.write("Score : 0",align = "center", font=("arial",22,"bold"))
pen.hideturtle()

def player_left():
    x = player.xcor()
    x-=20
    if x < -275:
        x = -275
    player.setx(x)

def player_right():
    x = player.xcor()
    x+=20
    if x > 275:
        x = 275
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet.goto(x,y)
        bullet.showturtle()
    
    
scr.listen()
scr.onkeypress(player_left,"Left")
scr.onkeypress(player_right,"Right")
scr.onkeypress(fire_bullet,"space")

while True:
    scr.update()
    for enemy in enemies:
        x = enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)

        if x > 275:
            for e in enemies:
                y = e.ycor()
                y-=40
                e.sety(y)
            enemyspeed *= -1

        if x < -275:
            for e in enemies:
                y = e.ycor()
                y-=40
                e.sety(y)
            enemyspeed *= -1

        if bullet.distance(enemy)<20:
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.goto(1000,1000)
            x = random.randint(-270,270)
            y = random.randint(150,275)
            enemy.goto(x,y)
            score += 10
            pen.clear()
            pen.write("Score : {}".format(score),align = "center", font=("arial",22,"bold"))

        if enemy.ycor()<-265:
            print("Game Over")
            exit()

    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate = "ready"












        





    






















