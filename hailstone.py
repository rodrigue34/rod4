# Rodrigue Andela
# 21/04/2021
# describe how to calculate how many steps does it take before the function reaches 1
def hailstone(start):
    counter = 0
    while start != 1:
        counter = counter +1

        if start % 2 == 0:
            start = start / 2
        else:
            start = start * 3 + 1
    return counter

