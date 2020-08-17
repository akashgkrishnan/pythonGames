import turtle
import winsound


window = turtle.Screen()
window.title = 'Pong' # on itle bar
window.bgcolor('black')
window.setup(width=800, height = 600) # width of the screen
window.tracer(0) #makes the game faster. ie sets the speed to the maximum


def paddleA_up():
    '''
    this function is responsible for the upward movement of the
    paddle A
    '''
    y = paddleA.ycor() #ycor is a turtle objct method which returns the y cordinates
    y += 20
    paddleA.sety(y) # set the y cordinate of the paddleA to the newly calculated y

def paddleA_down():
    '''
    this function is responsible for the downward movement
    '''
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)



#score board object



#first paddle A
paddleA = turtle.Turtle() # creating a turtle object
paddleA.speed(0) # sets the speed to the maximum posible speed
paddleA.shape('square')
paddleA.shapesize(stretch_wid=5, stretch_len=1)#default size is 20*20
paddleA.color('red')
paddleA.penup()
paddleA.goto(-350, 0)

# the second paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape('square')
paddleB.color('green')
paddleB.penup()
paddleB.goto(350, 0)
paddleB.shapesize(stretch_wid=5, stretch_len = 1)


#ball turtle object

ball = turtle.Turtle()
ball.speed(0)
ball.penup()
ball.goto(0,0)
ball.shape('square')
ball.color('white')
ball.dx = 0.2
ball.dy = -0.2

#keyboard bindings:
#paddle A up and down movements
window.listen()
window.onkeypress(paddleA_up, 'w') #when user clicks on w call the function mentioned
window.onkeypress(paddleA_down, 's')
#paddle b up and down movements keyboard binding
window.onkeypress(paddleB_up, 'Up')
window.onkeypress(paddleB_down, 'Down')


#scores of the players
playerA_Score = 0
playerB_Score = 0

# score card score display objects for player A
playerA_score = turtle.Turtle()
playerA_score.speed(0)
playerA_score.penup()
playerA_score.color('red')
playerA_score.goto(-100, 260)
playerA_score.hideturtle()
playerA_score.write(f'Player A :{playerA_Score}', align = 'center', font=('Courier', 15, 'normal'))


# score card score display objects for player B
playerB_score = turtle.Turtle()
playerB_score.speed(0)
playerB_score.penup()
playerB_score.color('green')
playerB_score.goto(100, 260)
playerB_score.hideturtle()
playerB_score.write(f'Player B :{playerB_Score}', align = 'center', font=('Courier', 15, 'normal'))







#main game loop
while True:
    window.update()
    #this main game loop will keep the ball moving
    # in the screen


    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        playerA_Score += 1
        playerA_score.clear()
        playerA_score.write(f'Player A :{playerA_Score}', align = 'center', font=('Courier', 15, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        playerB_Score += 1
        playerB_score.clear()
        playerB_score.write(f'Player B :{playerB_Score}', align = 'center', font=('Courier', 15, 'normal'))


    #ball hits on right paddle

    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddleB.ycor() + 60 and ball.ycor() > paddleB.ycor() - 60):
        ball.setx(330)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddleA.ycor() + 60 and ball.ycor() > paddleA.ycor() - 60):
        ball.setx(-330)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)


'''
for the implementation of LRU Cache we use a hybrid data structure
which is implemented as a combination of hashmap and doubly linked list

hashMap will give us  O(1) retreival
Insertion in linked list can be done in O(1) time if implemented in a proper way


The constructor will initialise the Cache.
we use the instance varaible cache as dictionary(hash map)
for storing nodes. This will help us have O(1) retreive time for nodes
The dictionary cache will be store the new key as key and the linked list
node as the value

we maintain the current size and also the constructor is initialised with
maxSize of the cache

the final instance variable we use is the linkedList
'''
