import unittest
import datetime


class Test(unittest.TestCase):
    def __init__(self):
        self.data = []

    def describe(test_desc, *arg):
        print (test_desc, *arg)
    def it(desc):
        print(desc)
    def assert_equals(one, two, msg=None):
        #print(one, ' == ', two)
        unittest.TestCase().assertEqual(one, two, msg=None)
    def assert_not_equals(one, two, msg=None):
        unittest.TestCase().assertNotEqual(one, two, msg=None)

test = Test

def xrange(*att):
    return range(*att)


def comment(desc_program=""):
    print ("###############################################")
    print(desc_program)

def testar(fnc,*arg):
    comment(fnc)
    starttime = datetime.datetime.now()
    test.describe("Diophantine Testing:", fnc)
    test.assert_equals(fnc(12), [[4, 1]])
    test.assert_equals(fnc(13), [[7, 3]])
    test.assert_equals(fnc(16), [[4, 0]])
    test.assert_equals(fnc(17), [[9, 4]])
    test.assert_equals(fnc(20), [[6, 2]])
    test.assert_equals(fnc(9001), [[4501, 2250]])
    test.assert_equals(fnc(9004), [[2252, 1125]])
    test.assert_equals(fnc(9005), [[4503, 2251], [903, 449]])
    test.assert_equals(fnc(90005), [[45003, 22501], [9003, 4499], [981, 467], [309, 37]])
    test.assert_equals(fnc(90009), [[45005, 22502], [15003, 7500], [5005, 2498], [653, 290], [397, 130], [315, 48]])
    test.assert_equals(fnc(900000),[[112502, 56249], [56254, 28123], [37506, 18747], [22510, 11245], [18762, 9369], [12518, 6241], [11270, 5615],
     [7530, 3735], [6286, 3107], [4550, 2225], [3810, 1845], [2590, 1205], [2350, 1075], [1650, 675], [1430, 535],
     [1150, 325], [1050, 225], [950, 25]])
    test.assert_equals(fnc(900001),[[450001, 225000]])
    test.assert_equals(fnc(900004),[[225002, 112500], [32150, 16068]])
    test.assert_equals(fnc(900005),[[450003, 225001], [90003, 44999]])
    test.assert_equals(fnc(9000001),[[4500001, 2250000], [73801, 36870]])
    test.assert_equals(fnc(9000004),[[2250002, 1125000], [173090, 86532], [132370, 66168], [10402, 4980]])
    test.assert_equals(fnc(9000005),[[4500003, 2250001], [900003, 449999], [642861, 321427], [155187, 77579], [128589, 64277], [31107, 15481],
     [22269, 11033], [4941, 1963]])
    test.assert_equals(fnc(90000001),[[45000001, 22500000], [6428575, 3214284], [3461545, 1730766], [494551, 247230]])
    test.assert_equals(fnc(90000004),[[22500002, 11250000], [252898, 126360], [93602, 46560], [22498, 10200]])
    test.assert_equals(fnc(900000009),[[450000005, 225000002], [150000003, 75000000], [50000005, 24999998], [26470597, 13235290], [8823555, 4411752],
 [2941253, 1470550]])
    test.assert_equals(fnc(900000012),[[225000004, 112500001], [75000004, 37499999], [3358276, 1679071], [1119604, 559601]])
    test.assert_equals(fnc(9000000041),[[4500000021, 2250000010], [155172429, 77586200]])

    print("Elapsed time:", datetime.datetime.now() - starttime)
    print("###############################################\n")

##########################################
comment("Diophantine Equation:")
# https://www.codewars.com/kata/diophantine-equation/train/python
#
# In mathematics, a Diophantine equation is a polynomial equation, usually in two or
# more unknowns, such that only the integer solutions are sought or studied.
#
# In this kata we want to find all integers x, y (x >= 0, y >= 0) solutions of a diophantine equation of the form
#
#  x ^ 2 - 4 * y ^ 2 = n
# where the unknowns are x and y and n is a given positive number.
# Solutions x, y will be given as an array of arrays (Ruby, Python, Clojure, JS, CS, TS)
#
#  [[x1, y1], [x2, y2] ....]
# as an array of tuples (Haskell, C++, Elixir)
#
#  [(x1, y1), (x2, y2) ....] or { {x1, y1}, {x2, y2} ....} or [{x1, y1}, {x2, y2} ....]
# as an array of pairs (C, see example tests)
#
# {{x1, y1}{x2, y2} ....}
# and as a string (Java, C#)
#
#  "[[x1, y1], [x2, y2] ....]"
# in decreasing order of the positive xi. If there is no solution returns [] or "[]".
#
# Examples:
#
# sol_equa(90005) -->  [[45003, 22501], [9003, 4499], [981, 467], [309, 37]]
#
# sol_equa(90002) --> []
#
# (Java, C#)
#
# solEquaStr(90005) --> "[[45003, 22501], [9003, 4499], [981, 467], [309, 37]]"
#
# solEquaStr(90002) --> "[]"
# Hint:
# Problem: x ^ 2 - 4 y ^ 2 = (x - 2y) (x + 2y) = n or (x - y) (x +y) = n.

def sol_equa1(n):
    solutions = []
    for x in range(int(n**0.5),int((n+1)/2)+1):
        for y2 in range(0,x,2):
            solutions.insert(0,[x, int(y2/2)]) if (x - y2)*(x + y2) == n else None
    return solutions
# Local Time:
# 0:00:03.811249 (x starting at 0)
# 0:00:02.786547 (x starting n**0.5)

def sol_equa2(n):
    return [[x, int(y / 2)] for x in range(int(n**0.5), int((n + 1) / 2) + 1) for y in range(0, x, 2) if (x + y) * (x - y) == n][::-1]
# Local Time:
# 0:00:04.300569 (x starting at 0)
# 0:00:02.680080 (x starting n**0.5)

def sol_equa3(n):
    solutions = []
    candidates = [number for number in range(1,n+1) if n % number == 0]
    pairs = [[plus,minus] for plus in candidates for minus in candidates if (plus * minus) == n if plus >= minus]
    for pair in pairs:
        # Solving:
        # x + 2y = pair[0]
        # x - 2y = pair[1]
        # where:
        # (x+2*y)*(x-2*y) = n
        x = int((1/2)*(pair[0] + pair[1]))
        y = int((1/2)*(pair[0] - x))
        if x**2 - 4*y**2==n:
            # print("Pairs:", pair, " x:", x, "y:", y, "(x+2y)(x-2y)=", (x+2*y)*(x-2*y))
            solutions.append([x,y])
    return solutions[::-1]
# Local Time:
# 0:00:00.002898

import math
def sol_equation(n):
	maxIter = 1e6;
	solutions = [] ;
	i=0;
	x=math.floor(n**.5)
	y=0
	while i<maxIter:
	#		print i
		i = i+1;
		if x**2-4*y**2 == n :
			solutions.append( [x,y]);
		if x**2-4*y**2 >n :
			y=y+1;
		else:
			x=x+1;
	# print  "Solution found\n","\n".join([str(sol) for sol in solutions])
	return solutions[::-1]



def sol_equa(n):
    solutions = []
    candidates = [number for number in range(1,int(n**0.5 + 1)) if n % number == 0]
    for z in candidates:
    # (x+2y)(x-2y) = n
    # zw = n

        w = n / z

    # (x+2y) = w
    #+(x-2y) = z
    # 2x = (z+w)
    ## x = (z + w)/2

        x = int((z + w)/2)

    # 2y = (w - x)
    ## y = (w - x)/2

        y = int((w - x)/2)
        if z == (x - 2*y) and w == (x + 2*y) and x >= 0 and y >= 0:
            solutions.append([x,y])
    return solutions

# import numpy as np
# def sol_equa4(n,memory={}):
#     for x in range(int(n**0.5),int((n+1)/2)+1):
#         for y in range(x):
#             if [x,y] not in memory.values():
#                 nn = (x-2*y)*(x+2*y)
#                 if nn > 0:
#                     memory.setdefault(nn, []).append([x,y])
#                     # print(nn, ":", x, ",", y)
#     return [np.unique(memory[n]).tolist()[::-1]]

def sol_equa5(n):
    """
    x - 2y = first_num
    x + 2y = second_num
    """

    result = []

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i != 0:
            continue
    # ij = n --> (x - 2y)(x + 2y) = n --> x**2 - 4y**2 = n
        j = n / i
    #    (x + 2y) = j
    #   (-x + 2y) = -i
    #         4y = j - i
        y = int((j - i) / 4)
    # x - 2y = i
        x = int(i + 2 * y)
        if x >= 0 and y >= 0 and (j == x + 2 * y) and (i == x - 2 * y):
            result.append([x, y])

    return sorted(result, reverse=True)

# testar(sol_equa1)
# testar(sol_equa)
#
#
testar(sol_equa3)
testar(sol_equa5)
