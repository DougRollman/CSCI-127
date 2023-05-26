##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: November 7th 2022


def computePrice(liquid, size):
    price = 0.0
    if liquid == "coffee":
        if size == "small":
            price = 2.5
        elif size == "medium":
             price = 2.75
        elif size == "large":
             price = 3.00
        else:
            return -1
    elif liquid== "misto":
        if size == "small":
             price = 3.15
        elif size == "medium":
             price = 3.35
        elif size == "large":
             price = 3.7
        else:
            return -1
    elif liquid == "mocha":
        if size == "small":
             price = 3.5
        elif size == "medium":
             price = 3.8
        elif size == "large":
             price = 4.25
        else:
            return -1
    elif liquid == "tea":
        if size == "small":
             price = 2.35
        elif size == "medium":
             price = 2.45
        elif size == "large":
             price = 2.90
        else:
            return -1
    else:
        return -1

    return price
