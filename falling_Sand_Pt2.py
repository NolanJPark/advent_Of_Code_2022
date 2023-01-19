# Function which prints out the falling sand list nicely
def prints(a):
    for r in range(len(a)):
        for c in range(len(a[0])):
            print(a[r][c], end='')
        print()
    print("\n\n")

# Opens file containing geography instructions and creates list holding the geography as well as the outer bounds vars
f = open("falling_Sand_File.txt", "r")
fall = []
end_y = [1000, 0]
end_x = 0
# Loop runs through file and determines the outer bounds of the geography
while 1:
    s = f.readline()
    if not s:
        break
    i = s.find(",")
    j = s.find(" ->")
    while j != -1:
        y = int(s[0:i])
        x = int(s[i+1:j])
        if x > end_x:
            end_x = x
        if y > end_y[1]:
            end_y[1] = y
        if y < end_y[0]:
            end_y[0] = y
        s = s[j+4:len(s)]
        i = s.find(",")
        j = s.find(" ->")
    y = int(s[0:i])
    x = int(s[i + 1:len(s)])
    if x > end_x:
        end_x = x
    if y > end_y[1]:
        end_y[1] = y
    if y < end_y[0]:
        end_y[0] = y
arr = [['.' for i in range(end_y[1]-end_y[0]+1)] for j in range(end_x+1)]
arr[0][500-end_y[0]] = "+"
# Adds two more rows to the bottom of the list
arr.append(['.']*len(arr[0]))
arr.append(['#']*len(arr[0]))
end_x += 2

f.seek(0)
# Loops through file and draws the geography depicted in the list
while 1:
    s = f.readline()
    if not s:
        break
    i = s.find(",")
    j = s.find(" ->")
    loc = (int(s[0:i]), int(s[i+1:j]))
    while j != -1:
        yo = int(s[0:i])
        xo = int(s[i+1:j])
        arr[xo][yo-end_y[0]] = "#"
        if loc[0] == xo and loc[1] != yo:
            if loc[1] > yo:
                for i in range(abs(loc[1]-yo)):
                    arr[xo][yo-end_y[0]+i] = "#"
            else:
                for i in range(abs(loc[1]-yo)):
                    arr[xo][yo-end_y[0]-i] = "#"
        if loc[1] == yo and loc[0] != xo:
            if loc[0] > xo:
                for i in range(abs(loc[0]-xo)):
                    arr[xo+i][yo-end_y[0]] = "#"
            else:
                for i in range(abs(loc[0]-xo)):
                    arr[xo-i][yo-end_y[0]] = "#"
        s = s[j+4:len(s)]
        i = s.find(",")
        j = s.find(" ->")
        loc = (xo, yo)
    yo = int(s[0:i])
    xo = int(s[i+1:len(s)])
    arr[xo][yo-end_y[0]] = "#"
    if loc[0] == xo and loc[1] != yo:
        if loc[1] > yo:
            for i in range(abs(loc[1]-yo)):
                arr[xo][yo-end_y[0]+i] = "#"
        else:
            for i in range(abs(loc[1]-yo)):
                arr[xo][yo-end_y[0]-i] = "#"
    if loc[1] == yo and loc[0] != xo:
        if loc[0] > xo:
            for i in range(abs(loc[0]-xo)):
                arr[xo+i][yo-end_y[0]] = "#"
        else:
            for i in range(abs(loc[0]-xo)):
                arr[xo-i][yo-end_y[0]] = "#"

sum = 0
# Loops until break statement, and during loop singular sand drop is simulated, adding columns to both sides when needed
while 1:
    loc = [0, 500-end_y[0]]
    b = False
    while 1:
        if loc[0]+1 != end_x and (loc[1]-1 < 0 or loc[1]+1 >= end_y[1]-end_y[0]):
            end_y[0] = end_y[0] - 1
            end_y[1] = end_y[1] + 1
            for i in range(len(arr)):
                if i != len(arr)-1:
                    arr[i].insert(0, '.')
                    arr[i].append('.')
                else:
                    arr[i].insert(0, '#')
                    arr[i].append('#')
            loc = [0, 500-end_y[0]]
        if arr[loc[0] + 1][loc[1]] == '.':
            loc[0] = loc[0] + 1
        elif arr[loc[0] + 1][loc[1] - 1] == '.':
            loc[0] = loc[0] + 1
            loc[1] = loc[1] - 1
        elif arr[loc[0] + 1][loc[1] + 1] == '.':
            loc[0] = loc[0] + 1
            loc[1] = loc[1] + 1
        elif loc == [0, 500-end_y[0]]:
            arr[loc[0]][loc[1]] = "o"
            sum += 1
            b = True
            break
        else:
            break
    if b:
        break
    arr[loc[0]][loc[1]] = "o"
    sum += 1
prints(arr)
# Prints number of sand units out nicely
print("A total of", sum, "units of sand came to rest")
