"""
#####   #####   #   #   #####
#   #   #   #   ##  #   #
#####   #   #   # # #   # ###
#       #   #   #  ##   #   #
#       #####   #   #   #####

Hi! This is a PONG game made with Turtle package, heavily inspired by a YouTube video ;)
Try your best to catch the ball, the unsolved imperfections won't make it easy for you!
Player A moves with "W" and "S".
Player B moves with arrows Up and Down.
Have fun :)
"""

# Import packages
import turtle
# import winsound
# import os


# Score table
def scoring(penA, penB, score_a, score_b):
    penA.clear()
    penA.color("red")
    penA.goto(-330, 260)
    penA.write(f"Player A: {score_a}", align="left", font=("Courier", 16, "bold"))
    penB.clear()
    penB.color("blue")
    penB.goto(330, 260)
    penB.write(f"Player B: {score_b}", align="right", font=("Courier", 16, "bold"))


def scorechange(score_a, score_b, window):
    if score_a > 5 or score_b > 5:
        over = turtle.Turtle()
        over.speed(0)
        over.hideturtle()
        over.penup()
        over.color("white")
        over.write("GAME OVER!", align="center", font=("Courier", 30, "bold"))
        over.goto(0, -40)
        if score_a > 5:
            over.write(f"\nTHE WINNER IS: Player A", align="center", font=("Courier", 30, "bold"))
        elif score_b > 5:
            over.write(f"\nTHE WINNER IS: Player B", align="center", font=("Courier", 30, "bold"))
        window.exitonclick()


# Adding all to main function
def main():
    # Table
    window = turtle.Screen()
    window.tracer(0)
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

    # Score
    score_a = 0
    score_b = 0

    # On-screen text
    penA = turtle.Turtle()
    penA.speed(0)
    penA.hideturtle()
    penA.penup()
    penA.color("red")
    penA.goto(-350, 260)
    penA.write(f"Player A: 0", align="left", font=("Courier", 16, "bold"))
    penB = turtle.Turtle()
    penB.speed(0)
    penB.hideturtle()
    penB.penup()
    penB.color("blue")
    penB.goto(350, 260)
    penB.write(f"Player B: 0", align="right", font=("Courier", 16, "bold"))

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

    window.listen()  # function tells the window (table) to wait for keyboard input
    window.onkeypress(paddle_a_up, "w")  # when you press "w" on keyboard, the function paddle_a_up() is called
    window.onkeypress(paddle_a_down, "s")
    window.onkeypress(paddle_b_up, "Up")  # must be Uppercase capital, to work for arrow
    window.onkeypress(paddle_b_down, "Down")

    while True:
        window.update()  # keeps the window open and updated

        # Moving ball
        ball.setx(ball.xcor() + ball.moveX)
        ball.sety(ball.ycor() + ball.moveY)

        # Top & bottom borders checking
        if ball.ycor() > 290:  # bouncing from the top (300 - 10 pixels)
            ball.sety(290)
            ball.moveY *= -1  # changing y direction to opposite
        if ball.ycor() < -290:  # bouncing from the top (300 - 10 pixels)
            ball.sety(-290)
            ball.moveY *= -1  # changing y direction to opposite

        # Bouncing from the paddles
        if 350 > ball.xcor() > 330 and paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50:
            ball.setx(330)
            ball.moveX *= -1
        if -350 > ball.xcor() < -330 and paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50:
            ball.setx(-330)
            ball.moveX *= -1

        # Getting points
        if ball.xcor() > 390:  # bouncing from the top (400 - 10 pixels)
            ball.goto(0, 0)
            ball.moveX *= -1
            score_a += 1
            scoring(penA, penB, score_a, score_b)
        if ball.xcor() < -390:  # bouncing from the top (400 - 10 pixels)
            ball.goto(0, 0)
            ball.moveX *= -1
            score_b += 1
            scoring(penA, penB, score_a, score_b)
        scoring(penA, penB, score_a, score_b)
        scorechange(score_a, score_b, window)


if __name__ == "__main__":
    main()
