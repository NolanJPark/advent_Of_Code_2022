f = open("cycle_Signal_File.txt", "r")
# Cycle represents the cycle on, x is the value of the register, and sum is value of the six signal strengths
cycle = 1
x = 1
sum = 0
# desired_cycle is used to represent the important signal cycles
desired_cycle = 20
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
    # Now that the instructions have been identified one cycle is run
    cycle += 1
    # If the current desired cycle has been reached sum is increased by cycle * x and desired cycles is increased by 40
    if cycle == desired_cycle:
        desired_cycle += 40
        sum += cycle * x
    # If instructions are to add cycle is increased by 1 and x is increased by value
    if instru == "addx":
        cycle += 1
        x += value
    # If the current desired cycle has been reached sum is increased by cycle * x and desired cycles is increased by 40
    if cycle == desired_cycle:
        desired_cycle += 40
        sum += cycle * x
# Prints the sum out nicely
print("The sum of the signal strength is", sum)
