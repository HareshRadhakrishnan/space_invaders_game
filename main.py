from turtle import Turtle, Screen
import turtle
import random

#TODO: class for creating defence
class Defence(Turtle):
    def __init__(self):
        super().__init__()
        self.all_fence = []

    def create_fence(self):
        Fx = 5
        Fy = 100
        X_addintion = 5
        fence_count = 0

        for i in range(0,2):
            for color in ['green','blue','orange'] :
                for _ in range(0,70):
                    fence = Turtle()
                    fence.speed('fastest')
                    fence.shape('square')
                    fence.penup()
                    fence.color(color)
                    fence.shapesize(1, 0.1)
                    fence.goto(Fx,Fy)
                    fence_count +=1
                    Fx += X_addintion
                    Fy -= 0.5
                    if fence_count % 13 == 1:
                        fence.hideturtle()
                        fence.clear()
                        continue
                    self.all_fence.append(fence)
                fence_count = 0
                Fy -= 10
                Fx = 5
            Fx = -5
            Fx *= -1
            X_addintion *= -1
            Fy = 100


#TODO: class for crating aliens
class Aliens():
    def __init__(self):
        self.move = 2.5
        self.all_aliens = []
        self.all_bullets = []
        self.bullet_delay = 0
    def create_alines(self):
        Ax = -120
        Ay = 280
        for i in range(0,3):
            for _ in range(0,6):
                alien = Turtle("tenor.gif")
                alien.penup()
                alien.goto(Ax, Ay)
                Ax += 30
                self.all_aliens.append(alien)
            Ax = -120
            Ay -=20

    def start_shooting(self):

        # this function includes moving the aliens also
        if len(self.all_aliens) !=0 and self.bullet_delay %20 == 1 :
              shooter = random.choice(self.all_aliens)
              bullet = Turtle()
              bullet.penup()
              bullet.right(90)
              bullet.shapesize(0.4,0.4)
              bullet.color('green')
              bullet.goto(shooter.xcor(),shooter.ycor())
              self.all_bullets.append(bullet)
        for a in self.all_aliens:
            a.goto((a.xcor() + self.move), a.ycor())
        for al in self.all_aliens:
            if (self.all_aliens[-1].xcor() == 400 and al.xcor() == 400) or (self.all_aliens[0].xcor() == -400 and al.xcor() == -400):
                self.move *= -1

        for b in self.all_bullets:
          b.goto(b.xcor(), b.ycor()-2)
#TODO: crating shooter
class Paddle():
    def __init__(self):
        self.all_paddles = []
        self.all_asthras =[]
    def crate_paddles(self):
        Px = - 450
        Py = -240
        for p in range(0,3):
            paddle = Turtle('attacker.gif')
            paddle.penup()
            paddle.goto(Px,Py)
            self.all_paddles.append(paddle)
            Px += 50
    def left(self):
         pad = self.all_paddles[0]
         pad.goto(pad.xcor()-3, pad.ycor())
    def right(self):
         pad = self.all_paddles[0]
         pad.goto(pad.xcor()+3, pad.ycor())
    def shoot(self):
        pad = self.all_paddles[0]
        asthiram = Turtle()
        asthiram.penup()
        asthiram.color('blue')
        asthiram.shapesize(0.4,0.4)
        asthiram.left(90)
        asthiram.goto(pad.xcor(),pad.ycor())
        self.all_asthras.append(asthiram)
    def move_asthras(self):
        for asthram in self.all_asthras:
            asthram.goto(asthram.xcor(), asthram.ycor()+5)

def finish_game ():
    if len(alien.all_aliens) < 1:
        text = " You Won"
    else:
        text = " You Lost"
    end_card = Turtle()
    end_card.penup()
    end_card.color('white')
    end_card.goto(0,0)
    end_card.write(f"Game Over \n{text} " ,align="center", font=("Arial", 36, "bold"))
def end_game():
    global game_over
    game_over = True
game_over = False
current_player = None
screen = Screen()
screen.register_shape('tenor.gif')
screen.register_shape('attacker.gif')
screen.setup(width=1000, height=600)
screen.bgcolor('black')
defence = Defence()
alien = Aliens()
turtle.tracer(0,0)
defence.create_fence()
alien.create_alines()
player = Paddle()
player.crate_paddles()
if len(player.all_paddles) > 0:
    player.all_paddles[0].goto(0, -210)
    current_player =player.all_paddles[0]
screen.listen()
screen.onkeypress(player.left, 'Left')
screen.onkeypress(player.right, 'Right')
screen.onkey(player.shoot,'space')
while not game_over:
    player.move_asthras()
    alien.bullet_delay +=1
    alien.start_shooting()
    if len(alien.all_aliens) < 1:
        end_game()

    for bullet in alien.all_bullets:
        if bullet.ycor() < -230:
            bullet.hideturtle()
            alien.all_bullets.remove(bullet)
        for fence in defence.all_fence:
            if fence.distance(bullet) < 5:
                fence.hideturtle()
                bullet.hideturtle()
                defence.all_fence.remove(fence)
                alien.all_bullets.remove(bullet)
        if bullet.distance(current_player) < 20:
            bullet.hideturtle()
            current_player.hideturtle()
            alien.all_bullets.remove(bullet)
            player.all_paddles.remove(current_player)
            try:
                player.all_paddles[0].goto(0, -210)
                current_player = player.all_paddles[0]
            except IndexError:

                end_game()
    for asthra in player.all_asthras:
        for f in defence.all_fence:
            if asthra.distance(f) < 5:
                f.hideturtle()
                asthra.hideturtle()
                player.all_asthras.remove(asthra)
                defence.all_fence.remove(f)
        for al in alien.all_aliens:
            if asthra.distance(al) < 10:
                al.hideturtle()
                asthra.hideturtle()
                player.all_asthras.remove(asthra)
                alien.all_aliens.remove(al)
        for bul in alien.all_bullets:
            if asthra.distance(bul) < 5:
                bul.hideturtle()
                asthra.hideturtle()
                alien.all_bullets.remove(bul)
                player.all_asthras.remove(asthra)

    screen.update()
screen.ontimer(finish_game, 500 )
screen.mainloop()