def length(l):
    counter = 0
    for elem in l:
        counter += 1
    return counter

def add_list(l, num):
    return l.append(num)

def delet(l, index):
    if 0 <= index <= len(l):
        return l[:index - 1] + l[index::]
    else:
         return 'error'

def reverse(l):
    return l[::-1]

