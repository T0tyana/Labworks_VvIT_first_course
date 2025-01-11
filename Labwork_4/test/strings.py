def length(s):
    counter = 0
    for elem in s:
        counter += 1
    return counter

def big(s):
    return s.upper()

def counter(s, x):
    return s.count(x)

def reverse(s):
    ans = ''
    for index in range(len(s) - 1, -1, -1):
        ans += s[index]
    return ans