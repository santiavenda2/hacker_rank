
open_braces_c = {'{', '[', '('}
closed_braces_c = {'{': '}', '[': ']', '(': ')'}


def braces(values):
    stack = []
    for w in values:
        if w in open_braces_c:
            stack.append(w)
        else:
            if stack and closed_braces_c[stack[-1]] == w:
                stack.pop(-1)
            else:
                return "NO"

    if stack:
        print "NO"
    else:
        print "YES"

if __name__ == '__main__':
    # a = "{}()[]"
    # a = "{{}}"
    # a = "{(})"
    a = "("
    braces(a)