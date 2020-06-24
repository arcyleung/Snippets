weights = [3, 2, 1]
values = [12, 10, 6]
maxWeight = 5

def bottomUp(weights, values, maxWeight):
    # 2d array/ memoization approach
    # row: items allowed in knapsack
    # col: incremental weight limit
    # cache[len(weights)][maxWeight] = max value possible at final weight limit and all items allowed/ considered 
    cache = [[0] * (maxWeight + 1) for y in range(len(weights) + 1)]

    # items allowed in knapsack
    for idx in range(1, len(weights) + 1):
        # current weight limit
        for w in range(1, maxWeight + 1):
            if (weights[idx-1] > w):
                # over current limit; exclude
                cache[idx][w] = cache[idx-1][w]
            else:
                # is it better to include or exclude item at idx?
                cache[idx][w] = max(
                    # exclude
                    cache[idx-1][w],
                    # include
                    cache[idx-1][w-weights[idx-1]] + values[idx-1]
                )
            

    return cache[len(weights)][maxWeight]

print(bottomUp(weights, values, maxWeight))
