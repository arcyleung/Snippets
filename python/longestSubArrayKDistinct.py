inp = [6, 5, 1, 2, 2, 2, 1, 2, 5, 1, 1, 1, 1, 1, 1]

class LSA:
    def __init__(self):
        self.arr = {6, 5, 1, 2, 3, 2, 1, 2, 5}
        # expect 1 2 3 2 1

    def findLongestSubArrKDistinct(self, arr, k):
        # longest subarray with at most k distinct elements
        numDistinct = 0
        maxLength = 0
        seen = dict()
        lIdx = 0

        for rIdx, r in enumerate(arr):

            if (r in seen.keys()):
                seen[r] += 1
            else:
                seen[r] = 1
            
            if (seen[r] == 1):
                numDistinct += 1

            # check if we exceeded k distinct items
            while (numDistinct > k):
                seen[arr[lIdx]] -= 1
                if (seen[arr[lIdx]] == 0):
                    numDistinct -= 1
                lIdx += 1
            
            if (rIdx - lIdx + 1 >= maxLength):
                # update best
                maxLength = rIdx - lIdx + 1

        print(maxLength)

    
test = LSA()
test.findLongestSubArrKDistinct(inp, 2)