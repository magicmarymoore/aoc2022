# day 6: tuning trouble
import input

data = input.data

# part 1
def laPrimeraParte(datos : list) -> int:
    a = []
    for x in range(3, len(datos)):
        for y in range(4):
            a.append(datos[x-y]) # find the 4 previous values
        b = [*set(a)] # remove duplicates
        if (len(b) == len(a)): # if the original didn't have duplicates, yay!!
            return x+1
        a.clear()
    return -1
print(laPrimeraParte(data))

# part 2
def parteDos(datos : list) -> int:
    a = []
    for x in range(13, len(datos)):
        for y in range(14):
            a.append(datos[x-y]) # find the 14 previous values
        b = [*set(a)] # remove duplicates
        if (len(b) == len(a)): # if the original didn't have duplicates, yay!!
            return x+1
        a.clear()
    return -1
print(parteDos(data))

