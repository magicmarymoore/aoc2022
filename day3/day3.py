# day 3: rugsack reorganization
import input

data = input.data.split('\n')

def priority(char : str) -> int:
    return ord(char) - 96 if (char.islower()) else ord(char) - 38 # 1-26 for lowercase & 27-52 for uppercase letters

def both(str1 : str, str2 : str) -> list:
    return [x for x in str1 if x in str2] # find common character

def laPrimeraParte(datos : list) -> int:
    return sum(priority(both(x[:int(len(x)//2)], x[-int(len(x)//2):])[0]) for x in datos) # sum the priorities
print(laPrimeraParte(data))


def group(str1 : str, str2 : str, str3 : str) -> list:
    return [x for x in str1 if ((x in str2) and (x in str3))] # find common character

def parteDos(datos : list) -> int:
    return sum([priority(group(datos[x], datos[x+1], datos[x+2])[0]) for x in range(0, len(datos), 3)]) # sum the priorities
print(parteDos(data))

