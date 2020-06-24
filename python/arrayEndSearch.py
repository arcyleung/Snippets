# Given an array, find whether it's possible to move from index 0 to last index
# Each value in array represents number of steps that can be advanced

# Ex. for a = [1,2,0,1], a[0] is "1" so we can advance by a[0+1] to "2"
# Then from index 1, a[1] is "2" we can advance to a[1+1] = a[2] or a[1+2] to a[3]; which is the end, therefore seach should return True

# Ex. for a = [1,0,2], there are no steps after a[1] so search should return False

# set = [1,2,0,1]
# set = [1,0,2]
set = [1,3,0,0,2,0,5]
print(set)

# Naive approach: start to end
def arrayEndSearchRecursive(set, current):
    if (current >= len(set)):
        return True
    else: 
        found = False
        for i in range(1, set[current]+1):
            found = found | arrayEndSearchRecursive(set, current+i)
        return found

# Reverse approach: End to start
def arrayEndSearchReverse(set):
    found = False
    length = len(set)
    currIx = length-1
    lastIx = currIx
    for i in range(0, length):
        currIx = length-i-1
        if (set[currIx] >= lastIx-currIx):
            lastIx = currIx
            found = True
        else:
            found = False
    return found

print("Naive approach: " + str(arrayEndSearchRecursive(set, 0)))
print("Reverse approach: " + str(arrayEndSearchReverse(set)))