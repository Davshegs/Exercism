def is_armstrong_number(number):
    check = []
    for x in str(number):
        digit = int(x)
        check.append(digit ** (len(str(number))))
    if sum(check) == number:
        return True
    return False

