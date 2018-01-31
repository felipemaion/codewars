# import time
# import timeit
import numpy
import unittest
import datetime


class Test:
    # def __init__(self):
    #     self.data = []

    def describe(test_desc, arg):
        print (test_desc, " ", arg)
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

### Teste padrão para testar as funções criadas por nós...
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


def sol_equa(n):
    solutions = []
    candidates = [number for number in range(1, int(n ** 0.5 + 1)) if n % number == 0]
    for z in candidates:
        # (x+2y)(x-2y) = n
        # zw = n

        w = n / z

        # (x+2y) = w
        # +(x-2y) = z
        # 2x = (z+w)
        ## x = (z + w)/2

        x = int((z + w) / 2)

        # 2y = (w - x)
        ## y = (w - x)/2

        y = int((w - x) / 2)
        if z == (x - 2 * y) and w == (x + 2 * y) and x >= 0 and y >= 0:
            solutions.append([x, y])
    return solutions




def sol_equa_du(n):
    ##--------------solucao padrao------------
    # (x+2y)(x-y2)=z(z-4y)=n
    Lbound = int(n ** .5)
    Ubound = n
    solutions = []
    z = Lbound
    while z <= Ubound:
        y = int((z * z - n) / (z * 4));
        if z * (z - 4 * y) == n:
            solutions.append([z - 2 * y, y])
        z += 1
    return solutions[::-1]


def sol_equa_du_np(n):
    ##--------------solucao padrao com numpy ------------
    ## (deve dar pau para numeros muito grandes)
    # (x+2y)(x-y2)=z(z-4y)=n
    Lbound = int(n ** .5)
    Ubound = n
    z = Lbound
    Z = numpy.arange(Lbound, Ubound + 1)
    Y = ((Z * Z - n) / (Z * 4));
    positions = numpy.where(Z * (Z - 4 * Y) - n == 0)[0]
    return [[Z[i] - 2 * Y[i], Y[i]] for i in positions]


##--------------solucao por fatorizacao em primos ------------
def PrimeFactor(N):
    primes = []
    multiplicity = []
    i = 2
    firstTime = True
    while i <= N:
        if N % i == 0:
            N = N / i
            if firstTime:
                primes.append(i)
                multiplicity.append(1)
                firstTime = False
            else:
                multiplicity[-1] += 1
        else:
            i += 1
            firstTime = True
    return [numpy.array(primes), numpy.array(multiplicity)]


def Divisors(N):
    p, m = PrimeFactor(N)
    m = m + 1
    nfactors = numpy.prod(m)
    #	factors = [ numpy.prod(p**[ i%numpy.prod(m[:im+1]+1) / numpy.prod(m[:im]+1)  for im in  range(len(m))  ] )  for i in range(1,nfactors)]
    factors = []
    for i in range(1, nfactors):
        ii = i
        factors.append(1)
        for j in range(len(p)):
            factors[-1] *= p[j] ** (ii % (m[j]))
            ii = ii / (m[j])
    return numpy.array(factors)


def sol_equa_du_primes(n):
    Z = Divisors(n)
    Z = Z[numpy.where(Z >= n ** .5)]  # parece que afeta mto pouco a performance
    Y = ((Z * Z - n) / (Z * 4));
    positions = numpy.where(numpy.logical_and((Z * (Z - 4 * Y) - n == 0), (Y >= 0)))[0]
    return [[Z[i] - 2 * Y[i], Y[i]] for i in positions]


def sol_equa_coco(n):
    ##------ solucao do maion que por algum motivo nao esta funcionando aqui---
    solutions = []
    candidates = [number for number in range(1, n + 1) if n % number == 0]
    # print (len(candidates))
    pairs = [[plus, minus] for plus in candidates for minus in candidates if (plus * minus) == n if plus >= minus]
    for pair in pairs:
        x = int((1 / 2) * (pair[0] + pair[1]))
        y = int((1 / 2) * (pair[0] - x))
        if x ** 2 - 4 * y ** 2 == n:
            solutions.append([x, y])
    return solutions[::-1]



# Target = 9005
# Target = 987 ** 2 - 50 ** 2 * 4
# print("Target ", Target)
#
# t = time.time()
# solutions = sol_equa_coco(Target)
# print("Elapsed Time Coco    ", time.time() - t, " N Solutions", len(solutions))  # , solutions
#
# t = time.time()
# solutions = sol_equa_du(Target)
# print("Elapsed Time Du      ", time.time() - t, " N Solutions", len(solutions))  # , solutions
#
# t = time.time()
# solutions = sol_equa_du_np(Target)
# print("Elapsed Time Du numpy", time.time() - t, " N Solutions", len(solutions))  # , solutions
#
# t = time.time()
# solutions = sol_equa_du_primes(Target)
# print("Elapsed Time Du primes", time.time() - t, " N Solutions", len(solutions))  # , solutions
#
# print("\n\nDebug...")
# t = time.time()
# solutions = Divisors(Target)
# print("Elapsed Time Du primes (Divisors findding)", time.time() - t, " N Divisors ", len(solutions))
#
# t = time.time()
# solutions = PrimeFactor(Target)
# print("Elapsed Time Du primes (PrimeFactoring)", time.time() - t, " N Divisors ", len(solutions[0]), solutions)
# print(solutions)
#
# solutions = PrimeFactor(90005)
# print(solutions)
# t =timeit.timeit(lambda : (sol_equation(n = (85560)**2-48555**2)), number=1)
# print "Elapsed Time",  t

testar(sol_equa)
testar(sol_equa_coco)
testar(sol_equa_du)
# testar(sol_equa_du_np)
# testar(sol_equa_du_primes)

if __name__ == '__main__':
    print("Running Main Tests")
    unittest.main()