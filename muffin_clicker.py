
import turtle

# Start the Turtle graphics
wn = turtle.Screen()
wn.title("Muffin clicker by @TokyoEdtech")
wn.bgcolor("yellow")

wn.register_shape("muffin.gif")


muffin = turtle.Turtle()
muffin.shape("muffin.gif")
muffin.speed(0)

shadow = turtle.Turtle()
shadow.hideturtle()
clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("black")
pen.penup()
pen.goto(0, 200)
pen.write(f"Clicks: {clicks}", align="center", font=("Comic Sans MS", 32, "normal"))

def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Comic Sans MS", 32, "normal"))
    shadow.showturtle()
    wn.ontimer(lambda: shadow.hideturtle(), 200)  # Hide the shadow after 0.2 seconds

muffin.onclick(clicked)

wn.mainloop()
