def prob4():
    verse = "jam tomorrow and jam yesterday"
    print("ther rule is,")
    c = mystery(verse)
    w = enigma(verse)
    print(c,w)

def mystery(v):
    print(v)
    c = v.count("jam")
    return(c)

def enigma(v,c):
    print("but never", v[-1])
    for i in range(c):
        print("jam")
    return("day.")

prob4()
