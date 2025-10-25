def excluding_vat_price(price):
    if price == None:
        return -1
    else:
        cost = price / 1.15
        return cost

def flick_switch(lst):
    res = []
    state = True
    for i in lst:
        if i == "flick":
            state = not state
        res.append(state)
    return res

def quadrant(x, y):
    if x == 0 or y == 0:
        return False
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4
    
def quarter_of(month):
    if month<=3:
        return 1
    elif month<=6:
        return 2
    elif month <=9:
        return 3
    else:
        return 4
    
def warn_the_sheep(queue):
    res = queue.index('wolf')
    if res == len(queue) - 1:
        return "Pls go away and stop eating my sheep"
    s = len(queue) - res - 1
    return f"Oi! Sheep number {s}! You are about to be eaten by a wolf!"