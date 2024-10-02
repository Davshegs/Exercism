def response(hey_bob):
    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    elif hey_bob.strip().endswith("?"):
        if hey_bob.strip()[:-1].isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    return "Whatever."
    

