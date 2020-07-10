def has_negatives(a):
    result = []
    # turn list into a dict
    num_dict = {num: True for num in a}
    # loop through a
    for num in a:
        # if the number is not negative, and the inverse of that number exists, append to result
        if num > 0 and (num*-1) in num_dict:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
