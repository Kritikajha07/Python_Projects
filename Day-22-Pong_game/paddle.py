from turtle import Turtle,Screen

screen=Screen()



class Paddle:

    def __init__(self,pos):
        self.paddle=Turtle()
        self.paddle.shape("square")
        self.paddle.color("cyan4")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.setpos(pos)


    def go_up(self):
        new_y=self.paddle.ycor() +20
        self.paddle.goto(self.paddle.xcor(),new_y)

    def go_down(self):
        new_y=self.paddle.ycor() -20
        self.paddle.goto(self.paddle.xcor(),new_y)
    
    def up(self):
        u=self.go_up
        d=self.go_down

        screen.onkey(u,"Up")
        screen.onkey(d,"Down")
        screen.listen()
    
    def down(self):
        w=self.go_up
        s=self.go_down
        
        screen.onkey(w,"w")
        screen.onkey(s,"s")
        screen.listen()
