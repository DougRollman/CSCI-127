names = input("Enter a list of names, separated by semicolon: ")
name_split = names.split(";")
for i in range(len(name_split)):
    temp = name_split[i]
    first_last = temp.split(" ")
    first = first_last[0]
    last = first_last[1]
    first_initial = first[0]
    print(first_initial + ".", last)
