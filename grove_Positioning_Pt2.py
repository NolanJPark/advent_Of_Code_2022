# Opens file containing data and creates a tuple containing two list
f = open("grove_Positioning_File", "r")
a = ([], [])

# Runs through file, adding the numbers to the first list and their index/order to the first, and multiplies the number
while 1:
    s = f.readline()
    if not s:
        break
    a[0].append(int(s) * 811589153)
    a[1].append(len(a[0])-1)

# Runs 10 times through each element and looks for the one to do then moves it accordingly
for m in range(10):
    for i in range(len(a[0])):
        for j in range(len(a[1])):
            if i == a[1][j]:
                temp = a[0].pop(j)
                tempN = a[1].pop(j)
                # Adds to beginning if to be moved to the beginning
                if j+temp == 0:
                    a[0].append(temp)
                    a[1].append(tempN)
                # Adds to the end if to be moved to the end
                elif j+temp == len(a[0]):
                    a[0].insert(0, temp)
                    a[1].insert(0, tempN)
                else:
                    a[0].insert((j+temp) % len(a[0]), temp)
                    a[1].insert((j+temp) % len(a[1]), tempN)
                break
print("Final Places:", a[0])

# Looks for 0 in first list then finds the desired elements based on this
i = 0
for j in range(len(a[0])):
    if a[0][j] == 0:
        i = j
sum = a[0][(i + 1000) % len(a[0])] + a[0][(i + 2000) % len(a[0])] + a[0][(i + 3000) % len(a[0])]
print("Sum:", sum)
