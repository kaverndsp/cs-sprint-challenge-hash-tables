def intersection(arrays):
    cache = {}
    result = []
    # two loops through to get each number
    for i in arrays:
        for j in i:
            # push each val into cache
            if j not in cache:
                cache[j] = 1
            else:
                cache[j] += 1
    # loop thru cache
    # print(cache)
    for key, v in cache.items():
        # if the value occured more than once, push into list
        if v > 1:
            result.append(key)

    # print(result)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
