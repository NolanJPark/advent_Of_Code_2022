f = open("cycle_Signal_File.txt", "r")
# Cycle represents the cycle on, x is the value of the register, and sprite represents the 40 string line
cycle = 0
crt = ""
x = 1
sprite = ""
while 1:
    s = f.readline()
    # Used to break loop if end of file is reached
    if not s:
        break
    # Variable instru holds the instructions for this line and value will hold the number to be added to x
    instru = s[0:4]
    value = None
    # If instru is addx then value is set to the value added to  x
    if instru == "addx":
        value = int(s[5:len(s)])
    cycle += 1
    # Sprite is emptied and the filled, where # is every space x represents
    sprite = ""
    for i in range(40):
        if i+1 == x:
            sprite += "#"
        elif i+1 == x+1:
            sprite += "#"
        elif i+1 == x+2:
            sprite += "#"
        else:
            sprite += "."
    # If cycle has reached 41 40 is subtracted from cycle and a new line is added to crt
    if cycle == 41:
        cycle -= 40
        crt += "\n"
    # a value from sprite based on the cycle is added to crt
    crt += sprite[cycle-1:cycle]

    # If instructions are to add cycle is increased by 1 and x is increased by value after the sprite is determined
    if instru == "addx":
        cycle += 1
        sprite = ""
        for i in range(40):
            if i+1 == x:
                sprite += "#"
            elif i+1 == x+1:
                sprite += "#"
            elif i+1 == x+2:
                sprite += "#"
            else:
                sprite += "."
        x += value
        if cycle == 41:
            cycle -= 40
            crt += "\n"
        crt += sprite[cycle-1:cycle]
# Prints everything out nicely
print("Look for letters in this... good luck:\n\n"+crt)