import turtle
t = turtle.Pen()
def get_square():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
       
def get_module():
    get_square()
    t.forward(100) 
    get_square()
    t.forward(100)
    get_square()
    
def change_position():
    #t.right(90)
    t.back(200)
    t.left(90)
    t.forward(100)
    t.right(90)
   
def get_play_area():
    get_module()
    change_position()
    get_module()
    change_position()
    get_module()