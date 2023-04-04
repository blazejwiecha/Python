from turtle import Turtle, Screen

timmy_zolwik = Turtle()

#mozemy działać z ekranem
screen = Screen()
#Zaczynam z poruszaniem zolwia w kwadrat

timmy_zolwik.position()
for _ in range(4):
    timmy_zolwik.forward(25)
    timmy_zolwik.right(90)
for _ in range(4):
    timmy_zolwik.forward(40)
    timmy_zolwik.right(90)

for _ in range(4):
    timmy_zolwik.forward(60)
    timmy_zolwik.right(90)
for _ in range(4):
    timmy_zolwik.forward(80)
    timmy_zolwik.right(90)
#for ulatwia sprawe
#timmy_zolwik.forward(25)
#timmy_zolwik.right(90)
#timmy_zolwik.forward(25)
#timmy_zolwik.right(90)
#timmy_zolwik.forward(25)
#timmy_zolwik.right(90)
    timmy_zolwik.position()

#timmy_zolwik.forward(-75)
#timmy_zolwik.position()

#skreca w prawo
#timmy_zolwik.heading()

#timmy_zolwik.right(90)
#timmy_zolwik.heading()


#timmy_zolwik.forward(25)
#timmy_zolwik.position()

#timmy_zolwik.forward(-75)
#timmy_zolwik.position()


#daje nam możliwość na pozostanie ekranu na koncu zadania
screen.exitonclick()