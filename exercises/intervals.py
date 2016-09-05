
def initialize_groups(n):
    return [(1, n, 0)]


def apply_operation(groups, f, t, k):
    new_groups = []
    for group_from, group_to, value in groups:
        if (group_from <= f <= group_to) and (group_from <= t <= group_to):
            if group_from <= f - 1:
                new_groups.append((group_from, f - 1, value))
            new_groups.append((f, t, value + k))
            if t + 1 <= group_to:
                new_groups.append((t + 1, group_to, value))
        elif group_from <= f <= group_to:
            if group_from <= f - 1:
                new_groups.append((group_from, f - 1, value))
            new_groups.append((f, group_to, value + k))
        elif group_from <= t <= group_to:
            new_groups.append((group_from, t, value + k))
            if t + 1 <= group_to:
                new_groups.append((t + 1, group_to, value))
        else:
            new_groups.append((group_from, group_to, value))

    return merge(new_groups)


def merge(groups):
    merged_groups = []
    i = 0
    while i < len(groups):
        f, t, k = groups[i]
        j = i + 1
        while j < len(groups) and groups[j][2] == k:
            j += 1
        merged_groups.append((f, groups[j-1][1], k))
        i = j

    return merged_groups


if __name__ == '__main__':
    n = 100000
    groups = initialize_groups(n)
    for i in range(n - 2):
        print groups
        groups = apply_operation(groups, i + 1, i + 2, 100)

    print max(k for f, t, k, in groups)
