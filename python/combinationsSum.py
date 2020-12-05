scores = [1, 2, 5]
goal = 10

solutionSets = set()

def findAllSums(remaining, currentSet):
    if (remaining == 0):
        solutionSets.add(currentSet)
    for idx, s in enumerate(scores):
        if (remaining - s >= 0):
            findAllSums(remaining - s, currentSet[:idx] + (currentSet[idx] + 1,) + currentSet[idx+1:])

    return solutionSets

print(findAllSums(10, (0,0,0)))
print(len(findAllSums(10, (0,0,0))))
