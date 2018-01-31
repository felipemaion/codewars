# class Node:
#     def __init__(self,initdata):
#         self.data = initdata
#         self.next = None
#     def getData(self):
#         return self.data
#     def getNext(self):
#         return self.next
#     def setData(self,newdata):
#         self.data = newdata
#     def setNext(self,newnext):
#         self.next = newnext
#
#
# node = list("1234567890")
# firstrun = False
# for i in range(len(node)):
#     if firstrun:
#         node.append("a")
#         print(node)
#     else:
#         node_1_new = node # Obj are iquals!
#         firstrun = True

# def decimalparahexa(n):
#     numeros = list("0123456789ABCDEF")
#     hexa = ""
#     while(True):
#         hexa = hexa + numeros[n%16]
#         n = n//16
#         if n == 0:
#             break
#     hexa = hexa[::-1]
#     hexa = str(hexa )
#     print('EM HEXADECIMAL: {}'.format(hexa))
#     return hexa

from itertools import combinations
possibilities = [1, 3, 5, 7, 9, 11, 13, 15]
decimals = [0, 0.1, 0.3, 0.5, 0.7, 0.9, 0.11, 0.13, 0.15]
all_combinations = combinations(possibilities, 3)
solutions = []
for combination in all_combinations:
    for dec1 in decimals:
        for dec2 in decimals:
            for dec3 in decimals:
                combo = [combination[0] + dec1, combination[1] + dec2, combination[2] + dec3]
                if sum(combo) == 30:
                    print("Solved: ", combo, "sum = ", sum(combo))
                    solutions.append(combo)

print("Found: ", len(solutions), "solutions")