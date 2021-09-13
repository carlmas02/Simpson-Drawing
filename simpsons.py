import turtle

#initializing the Drawing Objects
tee = turtle.Turtle()
outline = turtle.Turtle()
eyes = turtle.Turtle()
nose = turtle.Turtle()
eye_ball = turtle.Turtle()

#Adjusting the attributes
eye_ball.speed(0)
outline.speed(0)
eyes.speed(0)
eye_ball.pensize(8)

#Design for the outline
outline.color("black","yellow")
outline.begin_fill()

outline.left(96)
outline.forward(150)

for i in range(8):
	outline.right(140)
	outline.forward(23)

	outline.left(120)
	outline.forward(23)

	outline.left(17)

outline.right(160)

outline.forward(95)
outline.penup()
outline.forward(53)
outline.pendown()
outline.forward(70)


outline.right(55)

outline.circle(-120,66)
point_2 = (outline.xcor(),outline.ycor())

outline.penup()
outline.goto(5,-1)
outline.pendown()
outline.circle(10,270)
outline.circle(10,-50)

outline.right(100)
outline.forward(70)

outline.left(45)
outline.circle(60,75)
outline.left(45)

co_ord = tuple(map(round,(outline.xcor(),outline.ycor())))

outline.forward(10)
outline.right(70)
outline.circle(10,120)
point_3 = (outline.xcor(),outline.ycor())


outline.end_fill()
outline.hideturtle()

outline.color("yellow","yellow")
outline.penup()
outline.begin_fill()
outline.goto(5,-1)

outline.goto(point_2[0],point_2[1])
outline.goto(point_3[0],point_3[1])
outline.end_fill()

#Design for the eyes
eyes.color("black","white")
eyes.begin_fill()

eyes.penup()
eyes.goto(119,45)
eyes.pendown()

eyes.left(90)

eyes.circle(33)
eyes.circle(-33)

eyes.end_fill()
eyes.hideturtle()

#Design for the nose
nose.penup()
nose.goto(115,0)
nose.pendown()
nose.forward(26)
nose.circle(-10,180)
nose.forward(26)
nose.hideturtle()

#Desing for the eyeball
eye_ball.penup()
eye_ball.goto(75,45)
eye_ball.pendown()

eye_ball.circle(1)

eye_ball.penup()
eye_ball.goto(155,45)
eye_ball.pendown()

eye_ball.circle(1)
eye_ball.hideturtle()

#Design for the tee
tee.penup()
tee.goto(co_ord[0],co_ord[1])
tee.pendown()

tee.color("black","red")
tee.begin_fill()

tee.circle(-12,90)
tee.left(13)
tee.forward(60)
tee.left(40)
tee.circle(-90,35)
tee.right(85)
tee.circle(-200,50)
tee.right(60)
tee.circle(-80,60)
tee.left(54)
tee.forward(45)
tee.right(130)
tee.circle(60,75)
tee.end_fill()


#End the turtle working screen
turtle.done()
