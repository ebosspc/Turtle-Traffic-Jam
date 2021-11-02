#Import Turtle library for drawing functions
import turtle as trtl

#Create 2 empty lists for turtles
horiz_turtles = []
vert_turtles = []

#Create lists of shapes and colors to use
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

#Changing distance variable
tloc = 50

#For loop to horizontal and vertical turtles and set their initial conditions and locations
for s in turtle_shapes:
  #Create the horiontal turtle objects with a color, shape, and heading using the lists above
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)

  #Create the vertical turtle objects with a color, shape, and heading using the lists above
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  #Increase tloc by 50 every iteration so that every tutle is 50 units apart.
  tloc += 50

#Set initial step condition
steps = 0
max_steps = 850

#Set initial moving distance
move_length = 2

#While loop to handle turtle collisions
while steps < max_steps + 1:
    #Make turtles speed up
    if (steps % 25 == 0):
        move_length = move_length + 1
        
    #Slow turtles down if they get too fast
    if (move_length > 4):
        move_length = 2

    #For loop to handle each horizontal turtle
    for ht in horiz_turtles:
        #Nested for loop to handle each vertical turtle
        for vt in vert_turtles: 
            #Create stopping point
            if (steps > max_steps):
                #For loop to reset turtles
                #Set all horizontal turtles to end conditions
                for ht in horiz_turtles:
                    #Set ending color and shape
                    end_color = "green"
                    end_shape = "classic"

                    #Set all turtles to their ending states
                    ht.shape(end_shape)
                    ht.fillcolor(end_color)
                    vt.shape(end_shape)
                    vt.fillcolor(end_color)

                #Set all vertical turtles to end conditions
                for vt in vert_turtles:
                    #Set ending color and shape
                    end_color = "green"
                    end_shape = "classic"

                    #Set all turtles to their ending states
                    ht.shape(end_shape)
                    ht.fillcolor(end_color)
                    vt.shape(end_shape)
                    vt.fillcolor(end_color)

            else:
                #Move each horiontal turtle foward  
                ht.forward(move_length)
                vt.forward(move_length)
                steps = steps + 1

                #Check if horiontal turtle is overlapping with vertical turtle
                if (abs(ht.xcor() - vt.xcor()) < 10):
                    if (abs(ht.ycor()-vt.ycor()) < 10):
                        #Remember Original shape and color values for later
                        h_original_shape = ht.shape()
                        v_original_shape = vt.shape()
                        h_original_color = ht.fillcolor()
                        v_original_color = vt.fillcolor()

                        #Remove turtle
                        horiz_turtles.remove(ht)
                        vert_turtles.remove(vt)

                        #Define collision shape and color
                        collision_color = "red"
                        collision_shape = "classic"

                        #Set collision shape and color to turtles
                        ht.fillcolor(collision_color)
                        vt.fillcolor(collision_color)
                        ht.shape(collision_shape)
                        vt.shape(collision_shape)

                        #Move turtles backwards before trying again
                        dist_back = 40
                        ht.back(dist_back)
                        vt.back(dist_back)

                        #Restore Old properties
                        ht.shape(h_original_shape)
                        ht.fillcolor(h_original_color)
                        vt.shape(v_original_shape)
                        vt.fillcolor(v_original_color)
                        
                        #Add turtles back into lists so they can move again
                        horiz_turtles.append(ht)
                        vert_turtles.append(vt)

#Keep screen persistent and displayed
wn = trtl.Screen()
wn.mainloop()