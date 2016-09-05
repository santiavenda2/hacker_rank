

def mergeArrays(a,  b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    if i < len(a):
        result.extend(a[i:])
    if j < len(b):
        result.extend(b[j:])
    return result


if __name__ == '__main__':
    # a = [1, 5, 7, 7]
    # b = [0, 1, 2, 3]
    a = [2, 4,5,9 ,9]
    b = [0,1,2,3,4]
    print mergeArrays(a, b)