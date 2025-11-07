def descending_order(num):
    q = str(num)
    w = sorted(q)
    r= w[::-1]
    res = ''.join(r)
    return int(res)


def merge_arrays(arr1, arr2):
    return sorted(set(arr1+arr2))

def divisible_by(numbers, divisor):
    result = []
    for i in numbers:
        if i % divisor == 0:
            result.append(i)
    return result


def between(a,b):
    return list(range(a,b +1))


def switch_it_up(number):
    if number == 0:
        return "Zero"
    elif number == 1:
        return "One"
    elif number == 2:
        return "Two"
    elif number == 3:
        return "Three"
    elif number == 4:
        return "Four"
    elif number == 5:
        return "Five"
    elif number == 6:
        return "Six"
    elif number == 7:
        return "Seven"
    elif number == 8:
        return "Eight"
    else:
        return "Nine"