import random
from graphics import *
win=GraphWin('       Ludo     ',500,500)
img=Image(Point(250,250),'Ludo_1.PNG')
img.draw(win)
big_rect1=Rectangle(Point(15,15),Point(485,485))
big_rect1.setFill(color_rgb(30,50,30))
big_rect1.setwidth(3)
big_rect1.draw(win)
red_rect1=Rectangle(point(25,475),Point(200,300))
red_rect1.setFill('red')
red_rect1.setWidth(1)
red_rect1.draw(win)
green_rect1=Rectangle(point(25,25),Point(200,200))
green_rect1.setFill('green')
green_rect1.draw(win)
blue_rect1=Rectangle(point(300,200),Point(475,25))
blue_rect1.setFill('blue')
blue_rect1.draw(win)
yellow_rect1=Rectangle(point(300,300),Point(475,475))
yellow_rect1.setFill('yellow')
yellow_rect1.draw(win)
red_rect2=Rectangle(point(200,300),Point(300,475))
red_rect2.setWidth(1)
red_rect2.draw(win)
green_rect2=Rectangle(point(25,30),Point(200,200))
green_rect2.setwidth(1)
green_rect2.draw(win)
yellow_rect2=Rectangle(point(200,200),Point(475,300))
yellow_rect2.setwidth(1)
yellow_rect2.draw(1)
blue_rect2=Rectangle(point(200,25),Point(300,200))
blue_rect2.setwidth(1)
blue_rect2.draw(win)
red_rect3=Rectangle(point(200,300),Point(230,475))
red_rect3.setWidth(1)
red_rect3.draw(win)
red_rect4=Rectangle(point(230,300),Point(270,475))
red_rect4.setWidth(1)
red_rect4.draw(win)
red_rect5=Rectangle(point(200,446),Point(300,475))
red_rect5.setWidth(1)
red_rect5.draw(win)
red_rect6=Rectangle(point(200,417),Point(300,446))
red_rect6.setWidth(1)
red_rect6.draw(win)
red_rect7=Rectangle(point(200,388),Point(300,417))
red_rect7.setWidth(1)
red_rect7.draw(win)
red_rect8=Rectangle(point(200,359),Point(300,388))
red_rect8.setWidth(1)
red_rect8.draw(win)
red_rect9=Rectangle(point(200,330),Point(300,359))
red_rect9.setWidth(1)
red_rect9.draw(win)
red_rect10=Rectangle(point(200,300),Point(300,330))
red_rect10.setWidth(1)
red_rect10.draw(win)
red_rect11=Rectangle(point(200,417),Point(230,446))
red_rect11.setFill('red')
red_rect11.draw(win)
red_rect12=Rectangle(point(230,446),Point(270,475))
red_rect12.setFill(color_rgb(30,50,30))
red_rect12.draw(win)
red_rect1=Rectangle(point(235,235),Point(265,265))
red_rect1.setFill('pink')
rect_main=Rectangle(Point(200,200),point(300,300))
rect_main.setFill('red')
rect_main.draw(win)
line_r1=polygon(Point(235,265),Point(200,300),Point(200,200))
line_r1.setFill('green')
line_r1.draw(win)
poly_r2=polygon(Point(235,235),Point(200,200),Point(300,200))
poly_r2.setFill('blue')
poly_r2.draw(win)
poly_r3=polygon(Point(300,300),Point(265,265),Point(265,235))
poly_r3.setFill('yellow')
poly_r3.draw(win)
rect2=Rectangle(point(235,235),point(265,265))
rect2.setFill('cyan')
rect2.draw(win)
blue_rect3=Rectangle(point(200,25),Point(230,200))
blue_rect3.setWidth(1)
blue_rect3.draw(win)
blue_rect4=Rectangle(point(230,25),Point(270,200))
blue_rect4.setWidth(1)
blue_rect4.setFill('blue')
blue_rect4.draw(win)
blue_rect5=Rectangle(point(200,171),Point(300,200))
blue_rect5.setWidth(1)
blue_rect5.draw(win)
blue_rect6=Rectangle(point(200,142),Point(300,171))
blue_rect6.setWidth(1)
blue_rect6.draw(win)
blue_rect7=Rectangle(point(200,113),Point(300,142))
blue_rect7.setWidth(1)
blue_rect7.draw(win)
blue_rect8=Rectangle(point(200,84),Point(300,113))
blue_rect8.setWidth(1)
blue_rect8.draw(win)
blue_rect9=Rectangle(point(200,25),Point(300,84))
blue_rect9.setWidth(1)
blue_rect9.draw(win)
blue_rect10=Rectangle(point(200,25),Point(300,55))
blue_rect10.setWidth(1)
blue_rect10.draw(win)
blue_rect11=Rectangle(point(270,55),Point(300,84))
blue_rect11.setFill('blue')
blue_rect11.draw(win)
blue_rect12=Rectangle(point(230,25),Point(270,55))
blue_rect12.setFill(color_rgb(30,50,30))
blue_rect12.draw(win)
yellow_rect3=Rectangle(point(300,200),Point(475,230))
yellow_rect3.setWidth(1)
yellow_rect3.draw(win)
yellow_rect4=Rectangle(point(300,230),Point(475,270))
yellow_rect4.setWidth(1)
yellow_rect4.setFill('yellow')
yellow_rect4.draw(win)
yellow_rect5=Rectangle(point(300,200),Point(329,300))
yellow_rect5.setWidth(1)
yellow_rect5.draw(win)
yellow_rect6=Rectangle(point(329,200),Point(358,300))
yellow_rect6.setWidth(1)
yellow_rect6.draw(win)
yellow_rect7=Rectangle(point(358,200),Point(387,300))
yellow_rect7.setWidth(1)
yellow_rect7.draw(win)
yellow_rect8=Rectangle(point(387,200),Point(416,300))
yellow_rect8.setWidth(1)
yellow_rect8.draw(win)
yellow_rect9=Rectangle(point(416,200),Point(445,300))
yellow_rect9.setWidth(1)
yellow_rect9.draw(win)
yellow_rect10=Rectangle(point(445,200),Point(475,300,))
yellow_rect10.setWidth(1)
yellow_rect10.draw(win)
yellow_rect11=Rectangle(point(416,270),Point(445,300))
yellow_rect11.setFill('yellow')
yellow_rect11.draw(win)
yellow_rect12=Rectangle(point(445,230),Point(475,270))
yellow_rect12.setFill(color_rgb(30,50,30))
yellow_rect12.draw(win)
red_rect14=Rectangle(point(50,450),Point(175,325))
red_rect14.setFill(color_rgb(255,40,35))
red_rect14.setWidth(1)
red_rect14.draw(win)                
green_rect14=Rectangle(point(50,175),Point(175,50))
green_rect14.setFill(color_rgb(45,255,15))
green_rect14.setWidth(1)
green_rect14.draw(win)
blue_rect14=Rectangle(point(325,175),Point(450,50))
blue_rect14.setFill(color_rgb(115,125,255))
blue_rect14.setWidth(1)
blue_rect14.draw(win)
yellow_rect14=Rectangle(point(325,450),Point(450,325))
yellow_ect14.setFill(color_rgb(255,255,120))
yellow_rect14.setWidth(1)
yellow_rect14.draw(win)
#creating players
P_red2=Circle(point(113,388),10)
p_red2.setFill('magenta')
p_red2.draw(win)
dice=[1,2,3,4,5,6]
Dice=random.choice(dice)

def get1():
    circ1=Circle(Point(250,250),3)
    circ1.setFill('black')
    #rectangles.draw(win)
    circ1.draw(win)
    text=Text(Point(250,40),'1')
    text.setSize(28)
    text.setFill('red')
    text.draw(win)
def get2():
    circ1=Circle(Point(242,250),3)
    circ1.setFill('black')
    circ2=Circle(Point(258,250),3)
    circ2.setFill('black')
#rect1.draw(win)
circ1.draw(win)
circ2.draw(win)
text=Text(Point(250,40),'2')
text.setSize(28)
text.setFill('red')
text.draw(win)
def get3():
    circ1=Circle(Point(240,240),2.5)
    circ1.setFill('black')
    circ2=Circle(Point(250,250),2.5)
    circ2.setFill('black')
    circ3=Circle(Point(260,260),2.5)
    circ3.setFill('black')
    #rect1.draw(win)
    circ1.draw(win)
    circ2.draw(win)
    circ3.draw(win)
    text=Text(Point(250,40),'3')
    text.setSize(28)
    text.setFill('red')
    text.draw(win)
def get4():
    circ1=Circle(Point(242,242),2.5)
    circ1.setFill('black')
    circ2=Circle(Point(258,242),2.5)
    circ2.setFill('black')
    circ3=Circle(Point(242,258),2.5)
    circ3.setFill('black')
    circ4=Circle(Point(258,258),2.5)
    circ4.setFill('black')
    #rect1.draw(win)
    circ1.draw(win)
    circ2.draw(win)
    circ3.draw(win)
    circ4.draw(win)
    text=Text(Point(250,40),'4')
    text.setSize(28)
    text.setFill('red')
    text.draw(win)
def get5():
    circ1=Circle(Point(241,241),2.5)
    circ1.setFill('black')
    circ2=Circle(Point(259,241),2.5)
    circ2.setFill('black')
    circ3=Circle(Point(241,259),2.5)
    circ3.setFill('black')
    circ4=Circle(Point(259,259),2.5)
    circ4.setFill('black')
    circ5=Circle(Point(250,250),2.5)
    circ5.setFill('black')
    #rect1.draw(win)
    circ1.draw(win)
    circ2.draw(win)
    circ3.draw(win)
    circ4.draw(win)
    circ5.draw(win)
    text=Text(Point(250,40),'5')
    text.setSize(28)
    text.setFill('red')
    text.draw(win)
def get6():
    circ1=Circle(Point(240,242),2.5)
    circ1.setFill('black')
    circ2=Circle(Point(250,242),2.5)
    circ2.setFill('black')
    circ3=Circle(Point(260,242),2.5)
    circ3.setFill('black')
    circ4=Circle(Point(240,257),2.5)
    circ4.setFill('black')
    circ5=Circle(Point(250,257),2.5)
    circ5.setFill('black')
    circ6=Circle(Point(260,257),2.5)
    circ6.setFill('black')
    #rect1.draw(win)
    circ1.draw(win)
    circ2.draw(win)
    circ3.draw(win)
    circ4.draw(win)
    circ5.draw(win)
    circ6.draw(win)
    text=Text(Point(250,40),'6')
    text.setSize(28)
    text.setFill('red')
    text.draw(win)
def reset():
    rect2+Rectangle(Point(235,235),Point(265,265))
    rect2.setFill('cyan')
    rect2.draw(win)
    rect=Rectangle(Point(230,25),Point(270,55))
    rect.setFill(color_rgb(30,50,30))
    rect.draw(win)
def main():
    while True:
        win.getMouse()
        Dice=random.choice(dice)
        if Dice==1:
            shuffle.get1()
        if Dice==2:
            shuffle.get2()
        if Dice==3:
            shuffle.get3()
        if Dice==4:
            shuffle.get4()
        if Dice==5:
            shuffle.get5()
        if Dice==6:
           shuffle.get6()
           win.getMouse()
           shuffle.reset()
           Dice=random.choice(dice)
if __name__=='__main__':
    main()
                        
                        
