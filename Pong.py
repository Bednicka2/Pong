"""
Missing scoring system
Missing fluent movement
"""


import turtle

# Table
window = turtle.Screen()
window.title("Pong Table")
window.bgcolor("green")
window.setup(width=800, height=600)
# borders of windows are top=300, right=400, bottom=-300, left=-400
window.tracer(0)  # speeds up the game

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # speed of animation, 0 is maximum
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # stretching the size from square to vertical line
paddle_a.penup()  # so it does not draw lines
paddle_a.goto(-350, 0)  # starting position, axes x = -350, y = 0

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # speed of animation, 0 is maximum
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # stretching the size from square to vertical line
paddle_b.penup()  # so it does not draw lines
paddle_b.goto(350, 0)  # starting position, axes x = 350, y = 0

# Ball
ball = turtle.Turtle()
ball.speed(0)  # speed of animation, 0 is maximum
ball.shape("circle")  # default size of ball is 20x20 pixels
ball.color("white")
ball.penup()  # so it does not draw lines
ball.goto(0, 0)  # starting position in the middle
ball.moveX = 0.15  # speed of ball = number of pixels for horizontal movement
ball.moveY = 0.15  # speed of ball = number of pixels for vertical movement


# Moving paddles
def paddle_a_up():
    y = paddle_a.ycor()  # making variable y by giving it the y-coordinates already defined
    y += 20  # adding 20 pixels to go up
    paddle_a.sety(y)  # changing coordinates to new y


def paddle_a_down():
    y = paddle_a.ycor()  # making variable y by giving it the y-coordinates already defined
    y -= 20  # adding 20 pixels to go down
    paddle_a.sety(y)  # changing coordinates to new y


def paddle_b_up():
    y = paddle_b.ycor()  # making variable y by giving it the y-coordinates already defined
    y += 20  # adding 20 pixels to go up
    paddle_b.sety(y)  # changing coordinates to new y


def paddle_b_down():
    y = paddle_b.ycor()  # making variable y by giving it the y-coordinates already defined
    y -= 20  # adding 20 pixels to go down
    paddle_b.sety(y)  # changing coordinates to new y


# Keyboard binding
window.listen()  # function tells the window (table) to wait for keyboard input
window.onkeypress(paddle_a_up, "w")  # when you press "w" on keyboard, the function paddle_a_up() is called
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")  # must be Uppercase capital, to work for arrow
window.onkeypress(paddle_b_down, "Down")

# Ball movement
def ball_movement():
    ball.setx(ball.xcor() + ball.moveX)
    ball.sety(ball.ycor() + ball.moveY)
    # Top & bottom borders checking
    if ball.ycor() > 290:  # bouncing from the top (300 - 10 pixels)
        ball.sety(290)
        ball.moveY *= -1  # changing y direction to opposite
    elif ball.ycor() < -290:  # bouncing from the top (300 - 10 pixels)
        ball.sety(-290)
        ball.moveY *= -1  # changing y direction to opposite

    # Bouncing from the paddles
    elif 350 > ball.xcor() > 330 and paddle_b.ycor()-50 < ball.ycor() < paddle_b.ycor()+50:
        ball.setx(330)
        ball.moveX *= -1
    elif -350 > ball.xcor() < -330 and paddle_a.ycor()-50 < ball.ycor() < paddle_a.ycor()+50:
        ball.setx(-330)
        ball.moveX *= -1

    # Losing points
    elif ball.xcor() > 390:  # bouncing from the top (400 - 10 pixels)
        ball.goto(0, 0)
        ball.moveX *= -1
        print("GAME OVER")
    elif ball.xcor() < -390:  # bouncing from the top (400 - 10 pixels)
        ball.goto(0, 0)
        ball.moveX *= -1
        print("GAME OVER")


# Main game loop
while True:
    window.update()  # keeps the window open and updated
    ball_movement()
