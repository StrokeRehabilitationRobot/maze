import turtle
import math
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Maze game for stroke rehab")
screen.setup(700,700)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 0


    def go_up(self):
        move_x = player.xcor()
        move_y = player.ycor() + 24
        #self.goto(self.xcor(),self.ycor()+24)
        if (move_x,move_y) not in walls:
            self.goto(move_x,move_y)

    def go_down(self):
        move_x = player.xcor()
        move_y = player.ycor() - 24
        #self.goto(self.xcor(),self.ycor()-24)
        if (move_x,move_y) not in walls:
            self.goto(move_x,move_y)


    def go_left(self):
        move_x = player.xcor()-24
        move_y = player.ycor()
        #self.goto(self.xcor()-24,self.ycor())
        if (move_x,move_y) not in walls:
            self.goto(move_x,move_y)


    def go_right(self):
        move_x = player.xcor()+24
        move_y = player.ycor()
        #self.goto(self.xcor()+24,self.ycor())
        if (move_x,move_y) not in walls:
            self.goto(move_x,move_y)

    def collision(self,other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        d = math.sqrt((a**2)+(b**2))

        if d < 5:
            return True
        else:
            return False

class Goal(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

levels = [""]
treasures = []
level_1 = [
"WWWWWWWWWWWWWWWWWWWWWWWWW",
"WP WWWWWWW          WWWWW",
"W  WWWWWWW  WWWWWW  WWWWW",
"W       WW  WWWWWW  WWWWW",
"W       WW  WWW        WW",
"WWWWWW  WW  WWW        WW",
"WWWWWW  WW  WWWWWW  WWWWW",
"WWWWWW  WW    WWWW  WWWWW",
"W  WWW        WWWW  WWWWW",
"W  WWW  WWWWWWWWWWWWWWWWW",
"W         WWWWWWWWWWWWWWW",
"W                WWWWWWWW",
"WWWWWWWWWWWW     WWWWW  W",
"WWWWWWWWWWWWWWW  WWWWW  W",
"WWW  WWWWWWWWWW         W",
"WWW                     W",
"WWW         WWWWWWWWWWWWW",
"WWWWWWWWWW  WWWWWWWWWWWWW",
"WWWWWWWWWW              W",
"WWT WWWWWW              W",
"WW  WWWWWWWWWWWWWW  WWWWW",
"WW   WWWWWWWWWWWWW  WWWWW",
"WW           WWWW       W",
"WWWW                    W",
"WWWWWWWWWWWWWWWWWWWWWWWWW"
]

levels.append(level_1)

def maze_setup(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 +(x*24)
            screen_y = 288 -(y*24)

            if character =="W": #W = wall
                pen.goto(screen_x,screen_y)
                pen.stamp()
                walls.append((screen_x,screen_y))# coordinated pair
            if character =="P":#P = player
                player.goto(screen_x,screen_y)

            if character == "T": #T = treasure
                treasures.append(Goal(screen_x,screen_y))

pen = Pen()# class instances
player = Player()

walls=[]

maze_setup(levels[1])
#print(walls)
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

screen.tracer(0)

while True:
    for treasure in treasures:
        if player.collision(treasure):
            player.gold +=treasure.gold
            print ("Player Gold:{}".format(player.gold))

            treasure.destroy()
            treasures.remove(treasure)
    screen.update()
