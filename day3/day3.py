# day 3: rugsack reorganization
import input

data = input.data.split('\n')

def priority(char : str) -> int:
    return ord(char) - 96 if (char.islower()) else ord(char) - 38 # 1-26 for lowercase & 27-52 for uppercase letters

def both(str1 : str, str2 : str) -> str:
    for x in str1:
        if x in str2: # find common character
            return x
    return "-1" # error

def laPrimeraParte(datos : list) -> int:
    sum = 0
    for x in datos:
        l = int(len(x)//2) # split into two halves
        sum += priority(both(x[:l], x[-l:]))
    return sum

print(laPrimeraParte(data))


def group(str1 : str, str2 : str, str3 : str) -> str:
    for x in str1:
        if ((x in str2) and (x in str3)): # find common character
            return x
    return "-1" # error

def parteDos(datos : list) -> int:
    sum, x = 0, 0
    while (x < len(datos)):
        sum += priority(group(datos[x], datos[x+1], datos[x+2]))
        x += 3 # incremet to next group of 3 elves
    return sum

print(parteDos(data))

