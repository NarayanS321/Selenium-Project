x = (4)
y = (4)
z = (3)


def sum1(x, y, z):
    if x == y or y == z or z == x:
        sum = 2 * (x + y + z)
    else:
        sum = (x + y + z)

    return sum

for i in range (0, 3):
    print(sum1(x[i], y[i], z[i]))

