set = [10,5,1,44,2,29,24,22,22,3]

set.sort()

print(set)

def binSearch(val, start, end):
    mp = (start+end)/2
    if (end - start == 0):
        if (set[start] == val):
            return start
        else:
            return False

    if (set[mp] == val):
        return mp
    else:
        if (set[mp] < val):
            # Search RHS
            ix = binSearch(val, mp+1, end)
        else:
            # Search LHS
            ix = binSearch(val, start, mp)
        return ix

print(binSearch(44, 0, len(set)-1))