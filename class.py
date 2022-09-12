print('siddhopant')

def factoreal(n):
    if n == 1:
        return n
    else:
        return n* factoreal(n-1)

print(factoreal(5))
