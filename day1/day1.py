# day 1: calorie counting
import input

data = input.data.split('\n\n') # each inividual elf data is separated by 2 newline chars
for i, x in enumerate(data):
    data[i] = x.split('\n') # each data point is separated by one newline char

# part 1
def laPrimeraParte(datos):
    max = 0
    currTotal = 0
    for elf in datos:
        for item in elf:
            currTotal += int(item) # sum up total calories for this elf
        if (currTotal > max): # if this elf's calories are greater than the max, update max
            max = currTotal
        currTotal = 0
    
    return max # return the total max calories

print(laPrimeraParte(data))


# part 2
def parteDos(datos):
    max1, max2, max3 = 0, 0, 0
    currTotal = 0
    for elf in datos:
        for item in elf:
            currTotal += int(item) # sum up total calories for this elf
        if (currTotal > max1): # figure out if this total is in the top 3 max values so far, update accordingly
            max3 = max2
            max2 = max1
            max1 = currTotal
        elif (currTotal > max2):
            max3 = max2
            max2 = currTotal
        elif (currTotal > max3):
            max3 = currTotal
        currTotal = 0
    
    return max1+max2+max3 # return sum of the top three calorie values

print(parteDos(data))

