"""
A file holds the height of trees in a forest ranging from 0 to 9, and you need to find out how many
of the trees are visible from outside the forest. All the trees on the edge of the forest are considered
visible, and for an interior tree to be considered visible it must have no trees on its right, left, up,
or down that are as tall or taller than it.
"""

f = open("tree_House_File.txt", "r") #File containing tree heights is opened for reading
a = [] #List 'a' will hold the tuples of each row of tree heights
a1 = [] #List 'a1' will be a temp that holds each row before it's put in 'a'
tot = 0 #tot will hold the number of visible trees
while 1: #Infinite while loop
    c = f.read(1) #Reads a singe character from file and stores it as c
    if not c: #Runs if the end of the file has been hit
        a.append(a1) #Adds current a1 to end of a
        break #Ends while loop
    else: #Runs if the end of the file hasn't been hit
        x = ord(c) - 48 #Converts c to an ASCII int and subtracts 48 from it
        if x == -38: #Runs if the converted character is a new line
            a.append(a1) #Adds current a1 to end of a
            a1 = [] #Clears a1
        else:
            a1.append(x) #Adds x to the end of a1
tot += (len(a) - 1) + (len(a) - 1) + (len(a[0]) - 1) + (len(a[0]) - 1) #Adds the number of trees on the edge of the forest to tot
y = 0 #y will represent a variable from the file

for r in range(len(a)): #for loops run through 2D List
    for c in range(len(a[0])):
        if (r > 0 and r < len(a)-1) and (c > 0 and c < len(a[0]) - 1): #Runs if r and c represent the inside of the forest
            b = [1, 1, 1, 1] #b holds a 1 representing each direction around the tree [left, right, up, down]
            y = a[r][c] #sets y to variable at row r and column c
            for c2 in range(len(a[0])): #Runs through the column y is in
                z = a[r][c2] #z holds variable at row r and column c2
                if z >= y and c2 < c: #Runs if tree z is greater than or equal to tree y and we're on the left of y
                    b[0] = 0 #Makes the list b representing left equal to 0
                if z >= y and c2 > c: #Runs if tree z is greater than or equal to tree y and we're on the right of y
                    b[1] = 0 #Makes the list b representing right equal to 0
            for r2 in range(len(a)): #Runs through the row y is in
                z = a[r2][c] #z holds variable at row r2 and column c
                if z >= y and r2 < r: #Runs if tree z is greater than or equal to tree y and we're above y
                    b[2] = 0 #Makes the list b representing up equal to 0
                if z >= y and r2 > r: #Runs if tree z is greater than or equal to tree y and we're below y
                    b[3] = 0 #Makes the list b representing down equal to 0
            for i in b: #Runs through every variable in b
                if i == 1: #If any of the variables in b is still 1 then the tree is visible and adds 1 to tot
                    tot += 1
                    break #breaks for loop so more is added than necessary
print(tot, "trees are visible from outside the grid") #Prints out total nicely
f.close() #Closes file f