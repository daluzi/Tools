def kidsWithCandies(self, candies, extraCandies: int):
    m = max(candies)
    a = []
    for i in candies:
        if (i + extraCandies) >= m:
            a.append(True)
        else:
            a.append(False)
    return a