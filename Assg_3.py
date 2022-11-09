puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0]
a = [1, 2, 3, 0, 4, 6, 7, 5, 8]
def isSolved(a, puzzle):
 for i in range(9):
    if a[i] != puzzle[i]:
        return False
 return True

def upMove(a, index):
 if(index < 4):
    return a
 else:
    b = a.copy()
    t = b[index-3]
    b[index-3] = b[index]
    b[index] = t
    return b
def downMove(a, index):
 if(index>5):
    return a
 else:
    b = a.copy()
    t = b[index+3]
    b[index+3] = b[index]
    b[index] = t
    return b

def leftMove(a, index):
 if(index % 3 == 0):
    return a
 else:
    b = a.copy()
    t = b[index-1]
    b[index-1] = b[index]
    b[index] = t
    return b

def rightMove(a, index):
 if(index % 3 == 2):
    return a
 else:
    b = a.copy()
    t = b[index+1]
    b[index+1] = b[index]
    b[index] = t
    return b

def calH(a, puzzle):
 count = 0
 for i in range(8):
    if a[i] != puzzle[i]:
        count+=1
 return count
def printBox(a):
 print(f"{a[0]} {a[1]} {a[2]}")
 print(f"{a[3]} {a[4]} {a[5]}")
 print(f"{a[6]} {a[7]} {a[8]}")
 print()

def findSpace(a):
 for i in range(9):
    if a[i] == 0:
        return i
def Astar(a, puzzle):

 if(isSolved(a, puzzle)):
    print("Solved!!!")
    return

 index = findSpace(a)
 b = upMove(a, index)
 c = downMove(a, index)
 d = leftMove(a, index)
 e = rightMove(a, index)

 val = []
 b1 = calH(b, puzzle)
 c1 = calH(c, puzzle)
 d1 = calH(d, puzzle)
 e1 = calH(e, puzzle)
 val.append(b1)
 val.append(c1)
 val.append(d1)
 val.append(e1)
 move = 0
 for i in range(len(val)):
    if(val[i] < val[move]):
        move = i

 dict = { 0 : b,
 1 : c,
 2 : d,
 3 : e}

 if(move == 0):
     print("Up Move")
 elif move == 1:
    print("Down Move")
 elif move == 2:
    print("Left Move")
 elif move == 3:
    print("Right Move")
 printBox(dict[move])


 Astar(dict[move], puzzle)
printBox(a)
Astar(a, puzzle)