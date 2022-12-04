# day 4: camp cleanup
import input

data = input.data.splitlines()
for i, x  in enumerate(data):
    data[i] = x.split(",") # split up between elves

def compare(one : list, two : list) -> bool: # is all of str2 in str1??
    start1, end1 = one[0], one[1]
    start2, end2 = two[0], two[1]
    return True if ((start2 == end2 and start2 <= end1 and start2 >= start1) or (start2 >= start1 and end2 <= end1)) else False

def splitUp(vals : str) -> list:
    i = vals.find("-") 
    return [int(vals[:i]), int(vals[i+1:])] # find range of values for each site (as integers)

# part 1
def laPrimeraParte(datos : list) -> int:
    total = 0
    for x in datos:
        a = splitUp(x[0])
        b = splitUp(x[1])

        if (compare(a, b) or compare(b, a)): total += 1
    return total
print(laPrimeraParte(data))
    

def overlap(one : list, two : list) -> bool:
    x = list(set(range(one[0], one[1] + 1)) & set(range(two[0], two[1]+ 1)))
    return True if len(x) > 0 else False # determine if the two ranges overalp

# part 2
def parteDos(datos) -> int:
    total = 0
    for x in datos:
        a = splitUp(x[0])
        b = splitUp(x[1])

        if (overlap(a, b)): total += 1
    return total
print(parteDos(data))

