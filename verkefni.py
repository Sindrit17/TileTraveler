# Verkefnið: 9 Reitir eru í boði 3x3 (x-ás og y-ás). Notandinn getur fært sig
#suður-vestur-norður-austur, notandinn getur ekki farið í gegnum veggi eða út
#út fyrir kassann. Þegar hann er kominn á endastöð á hættir forritið að keyra 
#og segir "victory" Byrjunarreitiur = 1,1
#  (3,1) (3,2) 
x = 1
y = 1

north = 'Nn'
south = 'Ss'
west = 'Ww'
east = 'Ee'



while True:
    # (1,1)
    if x == 1 and y == 1:
        print("You can travel: (N)orth.")
        while True:
            direction = input("Direction: ")
            if direction in north:
                y += 1
                break
            else:
                print("Not a valid direction!")
        
    # (1,2)
    if x == 1 and y == 2:
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
        
    # (2,2)
    if x == 2 and y == 2:
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
            
    # (2,1)
    if x == 2 and y == 1:
        print("You can travel: (N)orth.")
        while True:
            direction = input("Direction: ")
            if direction in north:
                y += 1
                break
            else:
                print("Not a valid direction!")
        
    # (1,3)
    if x == 1 and y == 3:
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
            
    # (2,3)
    if x == 2 and y == 3:
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
        
    # (3,3)
    if x == 3 and y == 3: 
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
            
    # (3,2)
    if x == 3 and y == 2:
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
            
    # (3,1)
    if x == 3 and y == 1:
        print("Victory!")
        break

            
        


