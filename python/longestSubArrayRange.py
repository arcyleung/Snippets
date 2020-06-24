inp = [6, 1, 1, 2, 2, 2, 1, 2, 1, 3, 1, 1, 1, 1, 1, 1]
print(len(inp))

class LSA:
    def __init__(self):
        self.arr = {6, 5, 1, 2, 3, 2, 1, 2, 5}
        # expect 1 2 3 2 1

    def findLongestSubArrRange(self, arr, k):
        # longest subarray with elements in range of k
        numDistinct = 0
        maxLength = 0
        elements = set()
        seen = dict()
        lIdx = 0

        for rIdx, r in enumerate(arr):

            elements.add(r)

            if (r in seen.keys()):
                seen[r] += 1
            else:
                seen[r] = 1

            # check if range exceeded k
            while (max(elements) - min(elements) > k):
                seen[arr[lIdx]] -= 1
                if (seen[arr[lIdx]] == 0):
                    elements.remove(arr[lIdx])
                lIdx += 1
            
            if (rIdx - lIdx + 1 > maxLength):
                # update best
                maxLength = rIdx - lIdx + 1

        print(maxLength)

    
test = LSA()
test.findLongestSubArrRange(inp, 1)