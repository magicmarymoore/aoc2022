# day 5: supply stacks
import input

data = input.data.splitlines()
data.remove('') # that one random new line lmao

# find total
for x in data:
    if x[1] == '1':
        total = int(x[-2])
        break

# create a list of 'stacks'
stacks = [[]for x in range(total)]
stacks2 = [[]for x in range(total)]


def move(instruction : str) -> None:
    # find the numbers of interest
    amount = int(instruction[instruction.find('e') + 2 : instruction.find('f')])
    start = int(instruction[instruction.find('om ') + 2 : instruction.find(' to')])
    end = int(instruction[instruction.find('to ') + 2 : len(instruction)])

    # push and pop crates to stacks
    for x in range(amount):
        stacks[end-1].insert(0, stacks[start-1].pop(0))

# part 1
def laPrimeraParte(datos : list) -> str:
    for x in datos: # line of numbers, this was already accounted for above
        if x[1] == '1':
            continue
        elif x[0] == 'm': # line with a move on it
            move(x)
        else: # crate values
            for y in range(1, len(x), 4):
                if (x[y].isupper()):
                    stacks[y//4].append(x[y])
    
    return "".join(thingy[0] for thingy in stacks)
print(laPrimeraParte(data))


def moveP2(inst : str) -> None:
    # find the numbers of interest
    amount = int(inst[inst.find('e') + 2 : inst.find('f')])
    start = int(inst[inst.find('om ') + 2 : inst.find(' to')])
    end = int(inst[inst.find('to ') + 2 : len(inst)])

    # push and pop crates to stacks
    index = amount - 1 # reverse the order from before basically
    for x in range(amount):
        stacks2[end-1].insert(0, stacks2[start-1].pop(index))
        index -= 1

# part 2
def parteDos(datos : list) -> str:
    for x in datos:
        if x[1] == '1': # line of numbers, this was already accounted for above
            continue
        elif x[0] == 'm': # line with a move on it
            moveP2(x)
        else: # crate values
            for y in range(1, len(x), 4):
                if (x[y].isupper()):
                    stacks2[y//4].append(x[y])
    
    return "".join(thingy[0] for thingy in stacks2)
print(parteDos(data))

