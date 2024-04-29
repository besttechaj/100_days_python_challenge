### Logic to pass the game

def rightClear():
    for i in range(3):
        turn_left()
    if right_is_clear():
        move()
        for i in range(3):
            turn_left()
        while not wall_in_front():
            move()
def jump():
    if wall_in_front() and not wall_on_right():
        rightClear()
    elif wall_in_front():
        turn_left()
    else:
        while front_is_clear():
            if right_is_clear():
                rightClear()
            else:
                move()
                
def totalWalls():
    while not at_goal():
        if wall_in_front():
            jump()
        elif right_is_clear():
            rightClear()
        else:
            move()
totalWalls()

