from monkey import monkey
f = open("monkey_Business_File.txt", "r")
# Variable m will be a list that'll hold the monkey classes
m = []
while 1:
    s = f.readline()
    # Breaks loop when end of file is reached
    if not s:
        break
    # Runs if the  current line starts with monkey
    if s[0:6] == "Monkey":
        s = f.readline()
        # Variable item_s is the string list of starting items of current monkey
        items_s = s[18:len(s)]
        # List items will hold the ints from the monkeys starting items
        items = []
        # Saves index of first , as i and if it's not -1 then the number before i is added to items and i is found again
        i = items_s.find(",")
        while i != -1:
            items.append(int(items_s[0:i]))
            items_s = items_s[i+2:len(items_s)]
            i = items_s.find(",")
        # After while loop ends the last int in the starting items string is added to items
        items.append(int(items_s[0:len(items_s)]))
        s = f.readline()
        # Finds and saves the string representing the operation to be done
        op = s[23: len(s)]
        s = f.readline()
        # Saves the int that the items worry level will be divided by
        test = int(s[21:len(s)])
        s = f.readline()
        # Saves the number of the monkey that the item will be thrown to if true
        true = int(s[29:len(s)])
        s = f.readline()
        # Saves the number of the monkey that the item will be thrown to if false
        false = int(s[30:len(s)])
        # Calls monkey class and adds it to the end of list m
        m.append(monkey(items, op, test, true, false))
# For loop runs 20 rounds
for r in range(20):
    # For loop runs through each monkey in the list
    for n in range((len(m))):
        # Runs through each item of monkey n
        for i in range(len(m[n].items)):
            # Calls the removeItem function from the monkey class and saves the returned value as x
            x = m[n].removeItem()
            # Adds 1 to monkey n's inspections
            m[n].inspections += 1
            # Determines the type of operation to be done and the number the operation is done with as type and num
            type = m[n].operation[0:1]
            num = m[n].operation[2:len(m[n].operation)]
            # Runs the operation to be done
            if type == "*":
                if num == "old\n":
                    x = x*x
                else:
                    x *= int(num)
            elif type == "+":
                if num == "old":
                    x = x + x
                else:
                    x += int(num)
            # Divides worry by 3
            x = int(x/3)
            # Determines whether the test is true or not then uses the addItem function to give o the proper monkey
            if x % m[n].test == 0:
                m[m[n].true].addItem(x)
            else:
                m[m[n].false].addItem(x)
# Makes a list of two ints representing the two monkeys with the greatest inspection levels
nums = [m[0].inspections, 0]
# Runs through each monkey and if they're inspection level is greater than the first monkey nums is updated
for i in range((len(m))):
    x = m[i].inspections
    print("Monkey", i, "inspected items", x, "times.")
    if x > nums[0]:
        nums[0] = x
        nums[1] = m[i-1].inspections
# Runs through each monkey and if they're inspection level is greater than nums[1] and isn't equal to nums[0] it updates
for i in range((len(m))):
    x = m[i].inspections
    if x > nums[1] and x != nums[0]:
        nums[1] = x
# Prints everything out nicely
print("The level of monkey business after 20 rounds is", nums[0]*nums[1])