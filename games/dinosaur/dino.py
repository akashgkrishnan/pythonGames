import turtle
import random
import time
import winsound


window = turtle.Screen()
window.title('DinoJump')
window.bgpic('bg.jpg')
window.setup(width=900, height= 700)
window.tracer(0)

#registering GIF shape as bird
turtle.register_shape('birdie.gif')

bird = turtle.Turtle()
bird.speed(0)
bird.shape('birdie.gif')
bird.penup()
bird.goto(0,0)
bird.dy = -0.1

def birdUp():
    winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    bird.sety(bird.ycor() + 120)

def birdDown():
    winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    bird.sety(bird.ycor() - 120)

window.listen()
window.onkeypress(birdUp,'Up')
window.onkeypress(birdDown,'Down')



#user final score
FINAL_SCORE = 0



#all pillars
topPillar = turtle.Turtle()
topPillar.speed(0)
topPillar.shape('square')
topPillar.color('green')
topPillar.shapesize(stretch_wid=23, stretch_len=3)
topPillar.penup()
topPillar.goto(700,350)
topPillar.dx = -0.5


topPillar2 = turtle.Turtle()
topPillar2.speed(0)
topPillar2.shape('square')
topPillar2.color('green')
topPillar2.shapesize(stretch_wid=25, stretch_len=3)
topPillar2.penup()
topPillar2.goto(1000,350)
topPillar2.dx = -0.5


topPillar3 = turtle.Turtle()
topPillar3.speed(0)
topPillar3.shape('square')
topPillar3.color('green')
topPillar3.shapesize(stretch_wid=25, stretch_len=3)
topPillar3.penup()
topPillar3.goto(1300,350)
topPillar3.dx = -0.5



bottomPillar = turtle.Turtle()
bottomPillar.speed(0)
bottomPillar.shape('square')
bottomPillar.color('green')
bottomPillar.shapesize(stretch_wid=22, stretch_len=4)
bottomPillar.penup()
bottomPillar.goto(700,-350)
bottomPillar.dx = -0.5



bottomPillar2 = turtle.Turtle()
bottomPillar2.speed(0)
bottomPillar2.shape('square')
bottomPillar2.color('green')
bottomPillar2.shapesize(stretch_wid=26, stretch_len=4)
bottomPillar2.penup()
bottomPillar2.goto(1000,-350)
bottomPillar2.dx = -0.5


bottomPillar3 = turtle.Turtle()
bottomPillar3.speed(0)
bottomPillar3.shape('square')
bottomPillar3.color('green')
bottomPillar3.shapesize(stretch_wid=26, stretch_len=4)
bottomPillar3.penup()
bottomPillar3.goto(1300,-350)
bottomPillar3.dx = -0.5


scoreBoard = turtle.Turtle()
scoreBoard.speed(0)
scoreBoard.penup()
scoreBoard.color('black')
scoreBoard.goto(100, 260)
scoreBoard.hideturtle()
scoreBoard.write(f'Score :{FINAL_SCORE}', align = 'right', font=('Courier', 15, 'normal'))


def isCollidingFirstPillar():
    if bird.xcor() < topPillar.xcor() + 70 and bird.xcor() > topPillar.xcor() -70 and bird.ycor() > topPillar.ycor() - 300 and bird.ycor() < topPillar.ycor():
        return True

    if bird.xcor() < topPillar2.xcor() + 50 and bird.xcor() > topPillar2.xcor() -50 and bird.ycor() > topPillar2.ycor() - 200 and bird.ycor() < topPillar2.ycor():
        print()
        return True

    if bird.xcor() < topPillar3.xcor() + 70 and bird.xcor() > topPillar3.xcor() -70 and bird.ycor() > topPillar3.ycor() - 300 and bird.ycor() < topPillar3.ycor():
        print()
        return True

    if bird.xcor() < bottomPillar.xcor() + 70 and bird.xcor() > bottomPillar.xcor() -70 and bird.ycor() < bottomPillar.ycor() + 300 and bird.ycor() > bottomPillar.ycor():
        print()
        return True

    if bird.xcor() < bottomPillar2.xcor() + 70 and bird.xcor() > bottomPillar2.xcor() -70 and bird.ycor() < bottomPillar2.ycor() + 300 and bird.ycor() > bottomPillar2.ycor():
        print()
        return True

    if bird.xcor() < bottomPillar3.xcor() + 70 and bird.xcor() > bottomPillar3.xcor() -70 and bird.ycor() < bottomPillar3.ycor() + 300 and bird.ycor() > bottomPillar3.ycor():
        print()
        return True
    return False

count = 0
while True:
    window.update()
    #bird movement
    bird.sety(bird.ycor() + bird.dy)

    count += 1
    #pillar movement update
    topPillar.setx(topPillar.xcor() + topPillar.dx)
    bottomPillar.setx(bottomPillar.xcor() + bottomPillar.dx)

    topPillar2.setx(topPillar2.xcor() + topPillar2.dx)
    bottomPillar2.setx(bottomPillar2.xcor() + bottomPillar2.dx)

    topPillar3.setx(topPillar3.xcor() + topPillar3.dx)
    bottomPillar3.setx(bottomPillar3.xcor() + bottomPillar3.dx)



    #checking the bounds and replacing the pilar
    if topPillar.xcor() < -450:
        topPillar.goto(700,350)

    if topPillar2.xcor() < -450:
        topPillar2.goto(700,350)

    if topPillar3.xcor() < -450:
        topPillar3.goto(700,350)

    if bottomPillar.xcor() < -450:
        bottomPillar.goto(700,-350)

    if bottomPillar2.xcor() < -450:
        bottomPillar2.goto(700,-350)

    if bottomPillar3.xcor() < -450:
        bottomPillar3.goto(700,-350)


    if bird.xcor() > topPillar.xcor() + 50:
        FINAL_SCORE += 1

    if bird.xcor() > topPillar2.xcor() + 50:
        FINAL_SCORE += 1

    if bird.xcor() > topPillar3.xcor() + 5:
        FINAL_SCORE += 1


    scoreBoard.clear()
    scoreBoard.write(f'Score :{FINAL_SCORE}', align = 'right', font=('Courier', 15, 'normal'))



    if isCollidingFirstPillar():
        scoreBoard.clear()
        scoreBoard.write(f'Score :{FINAL_SCORE}', align = 'right', font=('Courier', 35, 'normal'))
        winsound.PlaySound('Bomb+2.wav', winsound.SND_ASYNC)
        time.sleep(3)
        break
