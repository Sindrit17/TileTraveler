def tile_1(x,y):
    """ runs actions on tile (1,1) """
    print("You can travel: (N)orth.")
    while True:
        direction = input("Direction: ")
        if direction in north:
            y += 1
            break
        else:
            print("Not a valid direction!")
    return(x,y)

def tile_2(x,y):
    """ runs actions on tile (1,2) """
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    while True:
        direction = input("Direction: ")
        if direction in north:
            y += 1
            break
        elif direction in east:
            x += 1
            break
        elif direction in south:
            y -= 1
            break
        else:
            print("Not a valid direction!")
    return(x, y)

def tile_3(x,y):
    """ runs actions on tile (1,3) """
    print("You can travel: (E)ast or (S)outh.")
    while True:
        direction = input("Direction: ")
        if direction in east:
            x += 1
            break
        elif direction in south:
            y -= 1
            break
        else:
            print("Not a valid direction!")
    return(x, y)

def tile_4(x,y):
    """ runs actions on tile (2,1) """
    print("You can travel: (N)orth.")
    while True:
        direction = input("Direction: ")
        if direction in north:
            y += 1
            break
        else:
            print("Not a valid direction!")
    return(x, y)

def tile_5(x,y):
    """ runs actions on tile (2,2) """
    print("You can travel: (S)outh or (W)est.")
    while True:
        direction = input("Direction: ")
        if direction in west:
            x -= 1
            break
        elif direction in south:
            y -= 1
            break
        else:
            print("Not a valid direction!")
    return(x,y)

def tile_6(x,y):
    """ runs actions on tile (2,3) """
    print("You can travel: (E)ast or (W)est.") 
    while True:
        direction = input("Direction: ")
        if direction in east:
            x += 1
            break
        if direction in west:
            x -= 1
            break
        else:
            print("Not a valid direction!")
    return(x,y)

def tile_7():
    """ runs actions on tile (3,1) """
    print("Victory!")
        

def tile_8(x,y):
    """ runs actions on tile (3,2) """
    print("You can travel: (N)orth or (S)outh.")
    while True:
        direction = input("Direction: ")
        if direction in north:
            y += 1
            break
        elif direction in south:
            y -= 1
            break
        else:
            print("Not a valid direction!")
    return(x,y)

def tile_9(x,y):
    """ runs actions on til (3,3) """
    print("You can travel: (S)outh or (W)est.")
    while True:
        direction = input("Direction: ")
        if direction in south:
            y -= 1
            break
        elif direction in west:
            x -= 1
            break
        else:
            print("Not a valid direction!")
    return (x,y)

x = 1
y = 1

north = 'Nn'
south = 'Ss'
west = 'Ww'
east = 'Ee'

while True:
    if x == 1 and y == 1:
        x, y = tile_1(x,y)
    elif x == 1 and y == 2:
        x, y = tile_2(x,y)
    elif x == 1 and y == 3:
        x, y = tile_3(x,y)
    elif x == 2 and y == 1:
        x, y = tile_4(x,y)
    elif x == 2 and y == 2:
        x, y = tile_5(x,y)
    elif x == 2 and y == 3:
        x, y = tile_6(x,y)
    elif x == 3 and y == 1: 
        tile_7()
        break
    elif x == 3 and y == 2:
        x, y = tile_8(x,y)
    elif x == 3 and y == 3:
        x, y = tile_9(x,y)
    

