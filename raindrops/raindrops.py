def convert(number):
    result = ""
    # if (number % 3 == 0 and number % 5 == 0 and number % 7 == 0):
    #       return "PlingPlangPlong"
    # elif number % 3 == 0:
    #     if number % 5 == 0:
    #         return  "PlingPlang"
    #     elif number % 7 == 0:
    #         return  "PlingPlong"
    #     return  "Pling"
    # elif number % 5 == 0:
    #     if number % 7 == 0:
    #         return "PlangPlong"
    #     return "Plang"
    # elif number % 7 == 0:
    #     return "Plong"
    # return str(number)

    if number % 3 == 0:
        result += 'Pling'
    if number % 5 == 0:
        result += 'Plang'
    if number % 7 == 0:
        result += 'Plong'
    return result or str(number)
