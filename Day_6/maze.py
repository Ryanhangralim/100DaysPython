#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_left():
    #turns the robot to left
    pass

def move():
    #moves the robot 1 block to the direction it's facing
    pass


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
move()
jump()
move()
jump()
move()
jump()
move()
jump()
move()
jump()
move()
jump()