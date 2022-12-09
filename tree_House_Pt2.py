"""
A file holds the height of trees in a forest ranging from 0 to 9, and this time you need to find the
most scenic tree in the forest. How scenic a tree is depends on how many trees can be seen on its left,
right, up, and down ending and counting trees that are as tall or taller than it.
"""

f = open("tree_House_File.txt", "r") #File containing tree heights is opened for reading
a = [] #List 'a' will hold the tuples of each row of tree heights
a1 = [] #List 'a1' will be a temp that holds each row before it's put in 'a'
score = 0 #score will hold the highest scenic score
tree = 0 #tree represents how tall the tree with the best scenic score is
tree_coord = (0,0) #tree_coord is a tuple representing the coordinates of the best tree
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
y = 0 #y will represent a variable from the file

for r in range(len(a)): #for loops run through 2D List
    for c in range(len(a[0])):
        btot = 1 #btot is the scenic score of the current tree, starts at 1 for multiplication purpuses
        b = [0, 0, 0, 0] #b holds a num representing how many trees can be seen in each direction around the tree [left, right, up, down]
        y = a[r][c] #Sets y to variable at row r and column c
        for c2 in range(c, 0, -1): #Runs through every num to the left of y
            z = a[r][c2-1] #Sets z to variable at row r and column c2 (-1 from c2 to compensate)
            if y > z: #Runs if tree y is greater than or equal to tree z
                b[0] += 1 #Adds 1 to b element representing left
            else:
                b[0] += 1 #Adds 1 to b element representing left and breaks loop
                break
        for c2 in range(c+1, len(a[0])): #Runs through every num to the right of y
            z = a[r][c2] #Sets z to variable at row r and column c2
            if y > z: #Runs if tree y is greater than or equal to tree z
                b[1] += 1 #Adds 1 to b element representing right
            else:
                b[1] += 1 #Adds 1 to b element representing right and breaks loop
                break
        for r2 in range(r, 0, -1): #Runs through every num above y
            z = a[r2-1][c] #Sets z to variable at row r2 (-1 to compensate) and column c
            if y > z: #Runs if tree y is greater than or equal to tree z
                b[2] += 1 #Adds 1 to b element representing up
            else:
                b[2] += 1 #Adds 1 to b element representing up and breaks loop
                break
        for r2 in range(r+1, len(a[0])): #Runs through every num below y
            z = a[r2][c] #Sets z to variable at row r2 and column c
            if y > z: #Runs if tree y is greater than or equal to tree z
                b[3] += 1 #Adds 1 to b element representing down
            else:
                b[3] += 1 #Adds 1 to b element representing down and breaks loop
                break
        for i in b: #Runs through every variable in b
            if i != 0: #If value of i isn't 0 then btot is multiplied by i
                btot *= i
        if btot > score: #Runs if btot is greater than score
            score = btot #Sets score to btot
            tree = y #Sets tree to y
            tree_coord = (r+1, c+1) #Sets tree_coord to (r,c) +1 to compensate for index
print("Tree number",tree,"at position (",tree_coord[0],",",tree_coord[1],") has the highest score with:",score) #Prints everything out nicely
f.close() #Closes file f