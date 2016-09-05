

def maxDifference(a):
    i = 0
    max_difference = -1
    while i < len(a) - 1:
        j = i + 1
        while j < len(a):
            diff = a[j] - a[i]
            if diff > max_difference:
                max_difference = diff
            j += 1
        i += 1

    return max_difference


def maxDifference2(a):
    max_diff = max(max_value - min_value for min_value, max_value in zip(min_left_values(a), max_right_values(a)))
    return max_diff if max_diff > 0 else -1


def max_right_values(a):
    max_value = -1
    result = [max_value]
    for v in reversed(a[1:]):
        if v > max_value:
            max_value = v
        result.append(max_value)
    return reversed(result)


def min_left_values(a):
    min_value = a[0]
    yield min_value
    for v in a[1:]:
        if v < min_value:
            min_value = v
        yield min_value

if __name__ == '__main__':
    # print maxDifference([7, 9,5,6,3,2])
    print maxDifference2([7, 9,5,6,3,2])
    print maxDifference2([1, 1])
