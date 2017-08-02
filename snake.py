import turtle
import random

turtle.tracer(1,0) # helps turtle move smoothly

SIZE_X = 800
SIZE_Y = 500
turtle.setup(SIZE_X, SIZE_Y) # turtle window size

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 2

# lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

# set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

# hide the turtle object (the arrow)
turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[1]
    x_pos+= SQUARE_SIZE
    my_pos =(x_pos,y_pos) # store position variable in a tuple
    snake.goto(x_pos, y_pos)
    pos_list.append(my_pos)
    STAMP = snake.stamp()
    stamp_list.append(STAMP)

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
TIME_STEP = 100 # updates snake pos after thi many milliseconds
SPACEBAR = "space"

UP = 0
LEFT = 2
DOWN = 1
RIGHT = 3

direction = UP

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    global direction
    direction = UP
    print("You pressed the up key!")

def down():
    global direction
    direction = DOWN
    print("You pressed the down key!")

def left():
    global direction
    direction = LEFT
    print("You pressed the left key!")

def right():
    global direction
    direction = RIGHT
    print("You pressed the right key!")


turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)

turtle.listen()
    
    

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")
    
    my_pos = snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)

    global food_stamps, food_pos
    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])


        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("You have eaten the food!")
        make_food()
    
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    elif new_y_pos >= UP_EDGE:
        print("You hit the top edge! Game over!")
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("You hit the bottom edge! Game over!")
        quit()
    
    turtle.ontimer(move_snake,TIME_STEP)

move_snake()

turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")

def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1

    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x, food_y)
    new_pos = (food_x,food_y)
    food_pos.append(new_pos)
    stamp_id = food.stamp()
    food_stamps.append(stamp_id)
make_food()




food.hideturtle()




























turtle.mainloop()

























