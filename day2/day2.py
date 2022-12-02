# day 2: rock paper scissors
import input

data = input.data.split('\n')
for i, x in enumerate(data):
    data[i] = x.split(' ')


def round(p1, p2) -> int:
    # convert ascii to ints
    p1 = ord(p1)
    p2 = ord(p2) - 23 # normalize to a, b, c
    
    a = p2 - p1
    print(a)
    if (a == 0): # draw
        print("draw", p2-64)
        return (3 + p2 - 64)
    elif (a == 1 or a == -2): # win
        print("win", p2-64)
        return (6 + p2 - 64)
    else: # loss
        print("loss", p2-64)
        return (p2 - 64)
    
    '''
        rock    paper   scissors
    r   draw    paper   rock
    p   paper   draw    scissors
    s   rock    scissors    draw

        A       B       C
    X   draw    p1      p2
    Y   p2      draw    p1
    Z   p1      p2      draw

        65  66  67
    65  0   -1  -2
    66  1   0   -1
    67  2   1   0
    '''


def laPrimeraParte(datos : list) -> int:
    score = 0
    for x in datos:
        score += round(x[0], x[1])
        #print(score)
    return score
        
print(laPrimeraParte(data))

"""A Y
B X
C Z"""

def round2(p1, p2):
    if (p2 == 'X'):
        if (p1 == 'A'): p1 = 3
        elif (p1 == 'B'): p1 = 1
        else: p1 = 2
        return p1
    elif (p2 == 'Y'):
        if (p1 == 'A'): p1 = 1
        elif (p1 == 'B'): p1 = 2
        else: p1 = 3
        return 3 + p1
    else:
        if (p1 == 'A'): p1 = 2
        elif (p1 == 'B'): p1 = 3
        else: p1 = 1
        return 6 + p1

def parteDos(datos : list) -> int:
    score = 0
    for x in datos:
        score += round2(x[0], x[1])
        #print(score)
    return score
print(parteDos(data)) # 8295

'''
        rock    paper   scissors
    r   draw    paper   rock
    p   paper   draw    scissors
    s   rock    scissors    draw

                A       B       C
    X(loose)    sciss   rock    paper  
    Y(draw)     rock    paper   scissors
    Z(win)      paper   sciss   rock

        65  66  67
    65  0   -1  -2
    66  1   0   -1
    67  2   1   0

    3   1   2
    1   2   3
    2   3   1

    rock = 1
    paper = 2
    scissors = 3
    '''
