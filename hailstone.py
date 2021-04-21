def hailstone(start):
    counter = 0
    while start != 1:
        counter = counter +1

        if start % 2 == 0:
            start = start / 2
        else:
            start = start * 3 + 1
    return counter

