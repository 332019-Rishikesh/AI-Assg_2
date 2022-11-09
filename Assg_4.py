a = [0, 0, 0, 0, 0, 0, 0, 3, 5, 6, 9, 1, 2, 0, -1]
Max = 100000
Min = -100000
def minMax(depth, nodeIndex, isMax, a, Alpha, Beta):
 Max = 100000
 Min = -100000
 if(depth == 3):
    return a[nodeIndex]

 if isMax:
    best = Min
    for i in range(0, 2):
        val = minMax(depth+1, nodeIndex*2 + (i+1), False, a, Alpha, Beta)
        best = max(val, best)
        Alpha = max(best, Alpha)

        if Beta <= Alpha:
         break

 else:
    best = Max
    for i in range(0, 2):
        val = minMax(depth+1, nodeIndex*2 + (i+1), True, a, Alpha, Beta)
        best = min(best, val)
        Beta = min(Beta, best)

        if Beta <= Alpha:
            break

 return best

print("Optimal Value is ",minMax(0, 0, True, a, -100000, 100000))