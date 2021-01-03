import turtle

window = turtle.Screen() # Pop up a new window

turtle.bgcolor("yellow") # Change the background colour of the window
turtle.color("magenta", "cyan") #Stroke colour, Fill colour
turtle.pensize(5) # Change the stroke on the shape

# Draw the circle and fill it with colour
turtle.begin_fill()
turtle.circle(80) # Radius of 80px
turtle.end_fill()

window.exitonclick() # When the page is clicked, the app closes
