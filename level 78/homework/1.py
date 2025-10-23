def _if(bool, func1, func2):
    if bool:
      func1()
    else:
      func2()


def find_needle(haystack):
    ind= haystack.index("needle")
    return "found the needle at position " + str(ind)



def how_many_light_sabers_do_you_own(name=""):
    if name != "Zach":
        return 0
    return 18
        


def open_or_senior(data):
    result = []
    for person in data:
        age, handicap = person
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result