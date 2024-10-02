
def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    global grain
    grain = [1]
    for x in range(1, 64):
        grain.append(grain[-1] * 2)
    return grain[number - 1]


def total():
    return sum(grain)
  
