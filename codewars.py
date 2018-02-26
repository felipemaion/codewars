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
        return unittest.TestCase().assertEqual(one, two, msg=None)
    def assert_not_equals(one, two, msg=None):
        return unittest.TestCase().assertNotEqual(one, two, msg=None)


test = Test

def xrange(*att):
    return range(*att)

# Todo:
# Implementar metaprogramming para criar as def conforme iniciar o Test.describe(txt) e rodar o
# Test.assert_equals em cima de um def test_*describe*
# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Metaprogramming.html

def comment(desc_program=""):
    print ("###############################################")
    print(desc_program)

###############################################
comment("The Like Function")

# Description:
#
# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
#
# Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:
#
# likes [] // must be "no one likes this"
# likes ["Peter"] // must be "Peter likes this"
# likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
# likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
# likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
# For more than 4 names, the number in and 2 others simply increases.

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    if len(names) == 1:
        return names[0] + " likes this"
    if len(names) == 2:
        return names[0] + " and " + names[1] + " like this"
    if len(names) == 3:
        return  names[0] + ", " + names[1] + " and " + names[2] + " like this"
    if len(names) > 3:
        return  names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"
Test.describe('Basic tests')
Test.assert_equals(likes([]), 'no one likes this')
Test.assert_equals(likes(['Peter']), 'Peter likes this')
Test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
Test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
Test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')

Test.describe("Random tests")
from random import randint, shuffle
sol = lambda n: 'no one likes this' if len(n) == 0 else n[0] + ' likes this' if len(n) == 1 else n[0] + ' and ' + n[
    1] + ' like this' if len(n) == 2 else n[0] + ', ' + n[1] + ' and ' + n[2] + ' like this' if len(n) == 3 else n[
                                                                                                                     0] + ', ' + \
                                                                                                                 n[
                                                                                                                     1] + ' and ' + str(
    len(n) - 2) + ' others like this'
base = ["Sylia Stingray", "Priscilla S. Asagiri", "Linna Yamazaki", "Nene Romanova", "Nigel", "Macky Stingray",
        "Largo", "Brian J. Mason", "Sylvie", "Anri", "Leon McNichol", "Daley Wong", "Galatea", "Quincy Rosenkreutz"]

for _ in range(40):
    shuffle(base)
    names = base[:randint(0, len(base) - 1)]
    Test.it("Testig for %s" % (", ".join(names) if len(names) > 0 else "none"))
    Test.assert_equals(likes(names), sol(names), "It should work for random inputs too")

# Test Cases:
#AssertionError: 'Jacob and Alex like this' != 'Jacob and A lex like this'
# - Jacob and Alex like this
# + Jacob and A lex like this
# ?            +

Test.describe('Basic tests')
Test.assert_equals(likes([]), 'no one likes this')
Test.assert_equals(likes(['Peter']), 'Peter likes this')
Test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
Test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
Test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
#
Test.describe("Random tests")
from random import randint, shuffle
sol=lambda n: 'no one likes this' if len(n)==0 else n[0]+' likes this' if len(n)==1 else n[0]+' and '+n[1]+' like this' if len(n)==2 else n[0]+', '+n[1]+' and '+n[2]+' like this' if len(n)==3 else n[0]+', '+n[1]+' and '+str(len(n)-2)+' others like this'
base=["Sylia Stingray", "Priscilla S. Asagiri", "Linna Yamazaki", "Nene Romanova", "Nigel", "Macky Stingray", "Largo", "Brian J. Mason", "Sylvie", "Anri", "Leon McNichol", "Daley Wong", "Galatea", "Quincy Rosenkreutz"]

for _ in range(40):
    shuffle(base)
    names=base[:randint(0,len(base)-1)]
    Test.it("Testig for %s" %(", ".join(names) if len(names)>0 else "none"))
    Test.assert_equals(likes(names),sol(names),"It should work for random inputs too")

#
# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this',
#         2: '{} and {} like this',
#         3: '{}, {} and {} like this',
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)


comment("The Supermarket Queue")

# # https://www.codewars.com/kata/the-supermarket-queue/train/python
# There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!
#
# The function has two input variables:
#
# customers: an array (list in python) of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
# n: a positive integer, the number of checkout tills.
# The function should return an integer, the total time required.
#
# EDIT: A lot of people have been confused in the comments. To try to prevent any more confusion:
#
# There is only ONE queue, and
# The order of the queue NEVER changes, and
# Assume that the front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.
# The diagram on the wiki page I linked to at the bottom of the description may be useful.
# So, for example:
#
# queue_time([5,3,4], 1)
# # should return 12
# # because when n=1, the total time is just the sum of the times
#
# queue_time([10,2,3,3], 2)
# # should return 10
# # because here n=2 and the 2nd, 3rd, and 4th people in the
# # queue finish before the 1st person has finished.
#
# queue_time([2,3,10], 2)
# # should return 12
# N.B. You should assume that all the test input will be valid, as specified above.
#
# P.S. The situation in this kata can be likened to the more-computer-science-related idea of a thread pool, with relation to running multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool
def grouplen(sequence, chunk_size):
    return list(zip(*[iter(sequence)] * chunk_size))

def allocate_them(customers,n):
    tills = []
    while len(customers) > 0: # Still customer waiting in the line?
        if len(tills) < n: # Is there any till available?
            customer = customers.pop(0) # You sir
            tills.append(customer) # Go to that till
            print("Customer (", customer, ") is at cashier")
        else: # No cashier available, please wait here, sir.
            break
    # print("Allocated:", tills, " Missing customers:", customers)
    return tills, customers

def queue_time(customers, n):
    sum = 0
    tills = []
    while len(customers) > 0: # Do we have customers waiting?
        tills, customers = allocate_them(customers, n)
        tills.sort() # Fasters leave first...
        user_time = tills.pop(0)
        sum += user_time if (user_time > 0) else 0
        # Time has passed for everybody:
        tills = list(map(lambda x: x - user_time, tills))
        # Only curstomers that still paying stay on the cashier:
        tills = [customer for customer in tills if customer > 0]
        print("Sir, We have", (n-len(tills)),  "free cashier here! \nAnd", len(tills), "busy cashiers. \nSo far time elapsed:", sum, "\n")
        for customer in tills: # the customers that haven't finished
            customers.insert(0,customer) # are treated as new customers with less time.
    print("\nNo more customers! Total time elapsed:", sum)
    return sum

# queue_time([4, 50, 24, 14, 3, 45, 14, 25, 36, 25, 46, 50, 34, 24, 6, 16],3) # 144
# # [37, 48, 7, 35, 27, 15, 3, 14, 1, 33, 47, 38] and n = 4: 122 should equal 95
#
# queue_time([1,2,3,4,5], 1)
# queue_time([1,2,3,4,5], 100)
Test.describe("Testing Supermarket Queue")
Test.assert_equals(queue_time([], 1), 0, "wrong answer for case with an empty queue")
Test.assert_equals(queue_time([5], 1), 5, "wrong answer for a single person in the queue")
Test.assert_equals(queue_time([2], 5), 2, "wrong answer for a single person in the queue")
Test.assert_equals(queue_time([1,2,3,4,5], 1), 15, "wrong answer for a single till")
Test.assert_equals(queue_time([1,2,3,4,5], 100), 5, "wrong answer for a case with a large number of tills")
Test.assert_equals(queue_time([2,2,3,3,4,4], 2), 9, "wrong answer for a case with two tills")
########### BRUXARIA!!!
# def queue_time(customers, n):
#     l=[0]*n
#     for i in customers:
#         l[l.index(min(l))]+=i
#     return max(l)


###########################################


# https://www.codewars.com/kata/iq-test/train/python
#
# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.
#
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
#
# ##Examples :
#
# iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even
#
# iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
comment("The iq_test:")



def iq_test(numbers):
    numbers = [int(x) for x in numbers.split(" ")]
    odds = []
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)
    if len(evens) > len(odds):
        return (numbers.index(odds[0]) + 1)
    else:
        return (numbers.index(evens[0]) + 1)

        # your code here
Test.describe("Testing IQ Test")
Test.assert_equals(iq_test("2 4 7 8 10"), 3)
Test.assert_equals(iq_test("1 2 2"), 1)

############################
# https://www.codewars.com/kata/descending-order/train/python
#     Description:
#
# Your task is to make a function that can take any non - negative
# integer as a argument and return it
# with its digits in descending order.Essentially, rearrange the digits to create the highest possible number.
#
# Examples:
#
# Input: 21445
# Output: 54421
#
# Input: 145263
# Output: 654321
#
# Input: 1254859723
# Output: 9875543221
    # array to binary to decimal
comment("The Descending_order:")

def Descending_Order(num):
    numl = list(str(num))
    numl.sort(reverse=True)
    return int("".join(numl))
    # Bust a move right here

Test.describe("Testing Descending Order")
Test.assert_equals(Descending_Order(0), 0)
Test.assert_equals(Descending_Order(1), 1)
Test.assert_equals(Descending_Order(15), 51)
Test.assert_equals(Descending_Order(1021), 2110)
Test.assert_equals(Descending_Order(123456789), 987654321)




#####################################
# https://www.codewars.com/kata/ones-and-zeros/train/python
# Given an array of one's and zero's convert the equivalent binary value to an integer.
#
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1
#
# Examples:
#
# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11

comment("The binary_array_to_number:")

def binary_array_to_number(arr):
  return int("".join(str(bit) for bit in arr),2)

# Test Cases:

import random

Test.describe("Example tests")
Test.assert_equals(binary_array_to_number([0,0,0,1]), 1)
Test.assert_equals(binary_array_to_number([0,0,1,0]), 2)
Test.assert_equals(binary_array_to_number([1,1,1,1]), 15)
Test.assert_equals(binary_array_to_number([0,1,1,0]), 6)

Test.describe("Random tests")
for _ in range(50):
    n = random.randint(0, 1000)
    array = [int(x) for x in bin(n)[2:]]
    Test.it("Tests %s ==> %s" % (array, n))
    Test.assert_equals(binary_array_to_number(array), n,"It should work for random inputs too")

######################################################
#
# n this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
#
# Example:
#
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes:
#
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.
comment("The high and low:")

def high_and_low(numbers):
    # ...
    numbers = [int(x) for x in numbers.split(" ")]
    high = str(max(numbers))
    low = str(min(numbers))
    numbers = " ".join([high, low])
    return numbers
# versão final está mais compacta... fuck off..
Test.describe("Testing High and Low")
Test.assert_equals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");
Test.assert_equals(high_and_low("1 -1"), "1 -1");
Test.assert_equals(high_and_low("1 1"), "1 1");
Test.assert_equals(high_and_low("-1 -1"), "-1 -1");
Test.assert_equals(high_and_low("1 -1 0"), "1 -1");
Test.assert_equals(high_and_low("1 1 0"), "1 0");
Test.assert_equals(high_and_low("-1 -1 0"), "0 -1");
Test.assert_equals(high_and_low("42"), "42 42");


###################################

# https://www.codewars.com/kata/reverse-or-rotate/train/python
# The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).
#
# If a chunk represents an integer such as the sum of the cubes
# of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left
# by one position. Put together these modified chunks and return the result as a string.
#
# If
#
# sz is <= 0 or if str is empty return ""
# sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
# Examples:
# revrot("123456987654", 6) --> "234561876549"
# revrot("123456987653", 6) --> "234561356789"
# revrot("66443875", 4) --> "44668753"
# revrot("66443875", 8) --> "64438756"
# revrot("664438769", 8) --> "67834466"
# revrot("123456779", 8) --> "23456771"
# revrot("", 8) --> ""
# revrot("123456779", 0) --> ""
# revrot("563000655734469485", 4) --> "0365065073456944"

# def revrot(strng, sz):
#     # your code
#
#
#
#
#
# def testing(actual, expected):
#     Test.assert_equals(actual, expected)
#
# 
# Test.describe("revrot")
# Test.it("Basic tests")
# testing(revrot("1234", 0), "")
# testing(revrot("", 0), "")
# testing(revrot("1234", 5), "")
# s = "733049910872815764"
# testing(revrot(s, 5), "330479108928157")


###########################################

# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
# The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
#
# Examples:
#
# "din" => "((("
#
# "recede" => "()()()"
#
# "Success" => ")())())"
#
# "(( @" => "))(("
#

comment("The duplicate_encode:")

def duplicate_encode(word):
    output = []
    word = word.lower()
    for char in word:
        output.append("(" if word.count(char) == 1 else ")")
    return "".join(output)

Test.describe("Testing duplicate encode")
Test.assert_equals(duplicate_encode("din"),"(((")
Test.assert_equals(duplicate_encode("recede"),"()()()")
Test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
Test.assert_equals(duplicate_encode("(( @"),"))((")

Test.describe( "Basic tests:")
Test.assert_equals(duplicate_encode("din"),"(((")
Test.assert_equals(duplicate_encode("recede"),"()()()")
Test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
Test.assert_equals(duplicate_encode("CodeWarrior"),"()(((())())")
Test.assert_equals(duplicate_encode("Supralapsarian"),")()))()))))()(","should ignore case")
Test.assert_equals(duplicate_encode("iiiiii"),"))))))","duplicate-only-string")


Test.describe( "Tests with '(' and ')'")
Test.assert_equals(duplicate_encode("(( @"),"))((")
Test.assert_equals(duplicate_encode(" ( ( )"),")))))(")


Test.describe( "And now... some random tests !")
from random import randint
duplicate_sol = lambda word: "".join(["(" if word.lower().count(x.lower())==1 else ")" for x in word])
for _ in range(40):
    testlen=randint(6,40)
    testword=""
    for i in range(testlen):
        testword+="abcdeFGHIJklmnOPQRSTuvwxyz() @!"[randint(0,30)]
    Test.it("Testing for word: "+testword)
    Test.assert_equals(duplicate_encode(testword),duplicate_sol(testword),"It Should encode '"+duplicate_sol(testword)+"'")




########################################

comment("Count the Digit:")
# https://www.codewars.com/kata/count-the-digit/train/python
# Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.
# Square all numbers k (0 <= k <= n) between 0 and n.
# Count the numbers of digits d used in the writing of all the k**2.
# Call nb_dig (or nbDig or ...) the function taking n and d as parameters and returning this count.
#
# #Examples:
#
# n = 10, d = 1, the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
# We are using the digit 1 in 1, 16, 81, 100. The total count is then 4.
#
# nb_dig(25, 1):
# the numbers of interest are
# 1, 4, 9, 10, 11, 12, 13, 14, 19, 21 which squared are 1, 16, 81, 100, 121, 144, 169, 196, 361, 441
# so there are 11 digits `1` for the squares of numbers between 0 and 25.
# Note that 121 has twice the digit 1.
def nb_dig(n, d):
    countd = 0
    for k in range(n+1):
        countd += str(k*k).count(str(d))
    return countd
# your code

Test.describe("nb_dig")
Test.it("Basic tests")
Test.assert_equals(nb_dig(5750, 0), 4700)
Test.assert_equals(nb_dig(11011, 2), 9481)
Test.assert_equals(nb_dig(12224, 8), 7733)
Test.assert_equals(nb_dig(11549, 1), 11905)
Test.assert_equals(nb_dig(14550, 7), 8014)
Test.assert_equals(nb_dig(8304, 7), 3927)
Test.assert_equals(nb_dig(10576, 9), 7860)
Test.assert_equals(nb_dig(12526, 1), 13558)
Test.assert_equals(nb_dig(7856, 4), 7132)
Test.assert_equals(nb_dig(14956, 1), 17267)
Test.assert_not_equals(nb_dig(14956, 1), -1)

from random import randint


def nbdigSol4532(n, d):
    k = 0
    cnt = 0
    d = str(d)
    while (k <= n):
        a = str(k * k).count(d)
        if (a > 0):
            cnt += a
        k += 1
    return cnt


def randomTests():
    print("Random tests ****************** ")
    for _ in range(0, 100):
        n = randint(2, 15000)
        d = randint(0, 9)
        Test.assert_equals(nb_dig(n, d), nbdigSol4532(n, d))


randomTests()

########################################
comment("Equal Sides Of An Array:")
#https://www.codewars.com/kata/equal-sides-of-an-array/train/python
# You are going to be given an array of integers.
# Your job is to take that array and find an index N where the sum of the integers to the left of N is
# equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.
#
# For example:
#
# Let's say you are given the array {1,2,3,4,3,2,1}:
# Your function will return the index 3, because at the 3rd position of the array,
# the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.
#
# Let's look at another one.
# You are given the array {1,100,50,-51,1,1}:
# Your function will return the index 1, because at the 1st position of the array,
# the sum of left side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.
#
# Last one:
# You are given the array {20,10,-80,10,10,15,35}
# At index 0 the left side is {}
# The right side is {10,-80,10,10,15,35}
# They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
# Index 0 is the place where the left side and right side are equal.
#
# Note: Please remember that in most programming/scripting languages the index of an array starts at 0.
#
# Input:
# An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.
#
# Output:
# The lowest index N where the side to the left of N is equal to the side to the right of N.
# If you do not find an index that fits these rules, then you will return -1.
#
# Note:
# If you are given an array with multiple answers, return the lowest correct index.
# An empty array should be treated like a 0 in this problem.

def find_even_index(arr):
    for index in range(len(arr)):
        if sum(arr[:index]) == sum(arr[(index+1):]):
            return index
        else:
            pass
    return -1
# your code here
Test.describe("Basic tests")
Test.assert_equals(find_even_index([1,2,3,4,3,2,1]),3)
Test.assert_equals(find_even_index([1,100,50,-51,1,1]),1,)
Test.assert_equals(find_even_index([1,2,3,4,5,6]),-1)
Test.assert_equals(find_even_index([20,10,30,10,10,15,35]),3)
Test.assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
Test.assert_equals(find_even_index([10,-80,10,10,15,35,20]),6)
Test.assert_equals(find_even_index(range(1,100)),-1)
Test.assert_equals(find_even_index([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
Test.assert_equals(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
Test.assert_equals(find_even_index(range(-100,-1)),-1)

Test.describe("Random tests")
from random import randint
find_even_sol=lambda arr, l=0, r="null", i=0: (lambda r: -1 if i>=len(arr) else i if r==l else find_even_sol(arr, l+arr[i], r-(0 if i+1>=len(arr) else arr[i+1]), i+1))(r if r!="null" else sum(arr[1:]))
contract=lambda arr: (lambda pos: arr[:pos]+[sum(arr[pos:])])(randint(0,len(arr)-1))

for _ in range(40):
    left=[randint(-20, 20) for qu in range(randint(10,20))]
    right=left[:]
    if randint(0,1): left[randint(0,len(left)-1)]+=randint(-20,20)
    left=sorted(contract(left), key=lambda a: randint(1,1000));right=sorted(contract(right), key=lambda a: randint(1,1000))
    arr=([]+left[:]+[randint(-20,20)]+right[:])[:]
    Test.it("Testing for %s" %arr)
    Test.assert_equals(find_even_index(arr[:]),find_even_sol(arr),"It should work for random inputs too")


##############################################
comment("The highest profit wins!")
# https://www.codewars.com/kata/the-highest-profit-wins/train/python
# Story
#
# Ben has a very simple idea to make some profit: he buys something and sells it again.
# Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price.
#
# Instead, he's going to buy it for the lowest possible price and sell it at the highest.
#
# Task
#
# Write a function that returns both the minimum and maximum number of the given list/array.
#
# Examples
#
# min_max([1,2,3,4,5])   == [1,5]
# min_max([2334454,5])   == [5, 2334454]
# min_max([1])           == [1, 1]
# Remarks
#
# All arrays or lists will always have at least one element,
# so you don't need to check the length. Also, your function will always get an array or a list,
# you don't have to check for null, undefined or similar.
def min_max(lst):
  return[min(lst), max(lst)]

from random import randint, shuffle

def test(lst, res):
  Test.assert_equals(min_max(lst), res, "tested on " + str(lst));

Test.describe("min_max")
Test.it("should work for some examples")
test([1,2,3,4,5], [1,5])
test([2334454,5], [5, 2334454])

for i in range(0,20):
    r = randint(0,100)
    test([r], [r,r])



########################################
comment("Maximum subarray sum:")
# https://www.codewars.com/kata/maximum-subarray-sum/train/python
# The maximum sum subarray problem consists in finding the maximum sum of a
#  contiguous subsequence in an array or list of integers:
#
# maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the
# maximum sum is the sum of the whole array. If the list is made up of only
# negative numbers, return 0 instead.
#
# Empty list is considered to have zero greatest sum. Note that the
# empty list or array is also a valid sublist/subarray.

def maxSequence(arr):
    comb = []
    maxsum = [0,0]
    if len(arr) == 0:
        return 0
    for index1 in range(len(arr)):
        for index2 in range(len(arr)+1):
            comb.append([index1,index2+1])
        for combination in comb:
            thissum = sum(arr[combination[0]:combination[1]])
            maxsum = [thissum, combination] if thissum > maxsum[0] else maxsum
    # print(arr[maxsum[1][0]:maxsum[1][1]])
    return maxsum[0]
	# ...

Test.describe("Tests")
Test.it('should work on an empty array')
Test.assert_equals(maxSequence([]), 0)
Test.it('should work on the example')
Test.assert_equals(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
Test.it('should work on random arrays')
from random import randint
def randomArray(size):
	return [ randint(-30, 30) for i in range(0, size) ]

def maxSequenceSol(arr):
	lowest = ans = total = 0
	for i in arr:
		total += i
		lowest = min(lowest, total)
		ans = max(ans, total - lowest)
	return ans
for i in range(50):
	ary = randomArray(50)
	Test.assert_equals(maxSequence(ary), maxSequenceSol(ary))



###############################################
comment("Reverse words:")
# https://www.codewars.com/kata/reverse-words/train/python
# Write a reverseWords function that accepts a string a parameter,
# and reverses each word in the string. Any spaces in the string should be retained.
#
# Example:
#
# reverse_words("This is an example!") # returns  "sihT si na !elpmaxe"
# reverse_words("double  spaces") # returns  "elbuod  secaps"
def reverse_words(str):
    new_str_list = []
    for word in str.split(" "):
        new_str_list.append(word[::-1])
    return " ".join(new_str_list)


  #go for it
Test.describe("Testing Reverse Words")
Test.assert_equals(reverse_words('This is an example!'),'sihT si na !elpmaxe')
Test.assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'),'ehT kciuq nworb xof spmuj revo eht yzal .god')
Test.assert_equals(reverse_words('apple'),'elppa')
Test.assert_equals(reverse_words('a b c d'),'a b c d')
Test.assert_equals(reverse_words('double  spaced  words'),'elbuod  decaps  sdrow')


##########################################
comment("Array.dif:")
# https://www.codewars.com/kata/array-dot-diff/train/python
# Your goal in this kata is to implement an difference function, which subtracts one list from another.
#
# It should remove all values from list a, which are present in list b.
#
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
#
# array_diff([1,2,2,2,3],[2]) == [1,3]


def array_diff(a, b):
    result = a
    if len(b) > 0:
        for number in b:
            result = [value for value in result if value != number]
    return result

# def array_diff(a, b):
#     return [x for x in a if x not in b]

Test.describe("Basic Tests")
Test.assert_equals(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
Test.assert_equals(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
Test.assert_equals(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
Test.assert_equals(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
Test.assert_equals(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")
Test.describe("Random Tests")
from random import randint
def array_sol(a, b): return [item for item in a if item not in b]
for _ in range(40):
    alen,blen=randint(0,20),randint(0,20)
    a=[randint(0,40)-20 for i in range(alen)]
    b=[randint(0,40)-20 for i in range(blen)]
    Test.it("Testing for array_diff(["+", ".join(map(str,a))+"],["+", ".join(map(str,b))+"])")
    Test.assert_equals(array_diff(a,b), array_sol(a,b), "Should work for random arrays too")



########################################

comment("How Much?")

# https://www.codewars.com/kata/how-much/train/python
#
# I always thought that my old friend John was rather richer than he looked,
# but I never knew exactly how much money he actually had. One day
# (as I was plying him with questions) he said:
# "Imagine I have between m and n Zloty (or did he say Quetzal? I can't remember!)
#
# If I were to buy 9 cars costing c each, I'd only have 1 Zlotty (or was it Meticals?) left.
#
# And if I were to buy 7 boats at b each, I'd only have 2 Ringglets (or was it Zlotty?) left.
#
# Could you tell me in each possible case:
#
# how much money f he could possibly have
# the cost c of a car
# the cost b of a boat?
# So, I will have a better idea about his fortune. Note that if m-n is big enough,
# you might have a lot of possible answers.
#
# Each answer will be given as ["M: f", "B: b", "C: c"] and all the answers as
#  [ ["M: f", "B: b", "C: c"] ... ]. M stands for "Money", B for boats, C for cars.
#
# m and n are positive or null integers with m <= n or m >= n, m and n inclusive.
#
# ##Examples:
#
# howmuch(1, 100) => [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"]]
# howmuch(1000, 1100) => [["M: 1045", "B: 149", "C: 116"]]
# howmuch(10000, 9950) => [["M: 9991", "B: 1427", "C: 1110"]]
# howmuch(0, 200) => [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"], ["M: 163", "B: 23", "C: 18"]]
# Explanation of howmuch(1, 100):
#
# In the first answer his possible fortune is 37 so if he buys 7 boats each worth 5 it remains 37 - 7 * 5 = 2,
# if he buys 9 cars worth 4 each it remains 37 - 9 * 4 = 1.
# The same with f = 100: 100 - 7 * 14 = 2 and 100 - 9 * 11 = 1.
#
# Note
#
# See "Sample Tests" to know the format of the return.


# income - (9 * price of car) = 1
# income - (7 * price of boat) = 2
def howmuch(m, n):
    m, n = min(m,n), max(m,n)
    car =0
    boat =0
    solutions = []
    # print("Getting income from:", m, "to:",n)
    for income in range(m,n+1):
        car = int(-(1-income)/9)
        boat = int(-(2-income)/7)
        if (income - 9*car) == 1 and (income - 7*boat) ==2:
            # print("Found solution: Car:", car, " and Boat:", boat, "for the income:", income)
            solutions.append(["M: " + str(income), "B: " + str(boat), "C: " + str(car)])
    return solutions
    # your code

howmuch(10000, 9950)
howmuch(1,100)
Test.assert_equals(howmuch(2950, 2950), [])
Test.assert_equals(howmuch(20000, 20100), [["M: 20008", "B: 2858", "C: 2223"], ["M: 20071", "B: 2867", "C: 2230"]])

Test.assert_equals(howmuch(1, 100), [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"]])
Test.assert_equals(howmuch(1000, 1100), [["M: 1045", "B: 149", "C: 116"]])
Test.assert_equals(howmuch(10000, 9950), [["M: 9991", "B: 1427", "C: 1110"]])
Test.assert_equals(howmuch(0, 200),
                   [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"], ["M: 163", "B: 23", "C: 18"]])
Test.assert_equals(howmuch(1500, 1600), [["M: 1549", "B: 221", "C: 172"]])
Test.assert_equals(howmuch(2950, 2950), [])
Test.assert_equals(howmuch(20000, 20100), [["M: 20008", "B: 2858", "C: 2223"], ["M: 20071", "B: 2867", "C: 2230"]])


def howmuch1341(m, n):
    i = min(m, n)
    j = max(m, n)
    res = []
    while (i <= j):
        if ((i % 9 == 1) and (i % 7 == 2)):
            res.append(["M: " + str(i), "B: " + str(i // 7), "C: " + str(i // 9)])
        i += 1
    return res


from random import randint


def randomTests():
    Test.describe("50 Random Tests")
    for x in range(0, 50):
        m = randint(60000, 60550) + randint(1, 100)
        n = randint(60551, 60999) + randint(1, 200)
        Test.it("Testing howmuch, Test number : %i" % (x))
        Test.assert_equals(howmuch(m, n), howmuch1341(m, n))


randomTests()


###################################
comment("Build Tower:")
# https://www.codewars.com/kata/build-tower/train/python
#
# Build Tower
#
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
#
# Tower block is represented as *
#
# Python: return a list;
# JavaScript: returns an Array;
# C#: returns a string[];
# PHP: returns an array;
# C++: returns a vector<string>;
# Haskell: returns a [String];
# Have fun!
#
# for example, a tower of 3 floors looks like below
#
# [
#   '  *  ',
#   ' *** ',
#   '*****'
# ]
# and a tower of 6 floors looks like below
#
# [
#   '     *     ',
#   '    ***    ',
#   '   *****   ',
#   '  *******  ',
#   ' ********* ',
#   '***********'
# ]
# Go challenge Build Tower Advanced (https://www.codewars.com/kata/57675f3dedc6f728ee000256)
#  once you have finished this :)
def tower_builder(n_floors):
    chr_size = 2 * n_floors -1
    tower = []
    for nfloor in range(1, n_floors+1):
        floor_chr = int(2*nfloor -1) * "*"
        spaces = " " * int((chr_size - len(floor_chr))/2)
        str_floor = spaces + floor_chr  + spaces
        # print("[", str_floor, "]")
        tower.append(str_floor)
    return tower
    # build here

test = Test
test.describe("Tests")
test.it("Basic Tests")
test.assert_equals(tower_builder(1), ['*', ])
test.assert_equals(tower_builder(2), [' * ', '***'])
test.assert_equals(tower_builder(3), ['  *  ', ' *** ', '*****'])
# Use test.describe (or Test.describe) to describe your test suite
test.describe("Tests")

# Use "it" calls to describe the specific test case
test.it("Blanket Test")

# assert equals will pass if both items equal each other (using ==). If
# the test fails, assert_equals will output a descriptive message indicating
# what the values were expected to be.

def sol(n_floors):
    floors = []
    n = n_floors
    for i in range(n_floors):
        n -= 1
        floors.append(' ' * n + '*' * (i * 2 + 1) + ' ' * n)

    return floors

for i in range(1, 101):
    test.assert_equals(tower_builder(i), sol(i))

    #BRUXARIA!!!!!
# def tower_builder(n):
#     return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

######################################

comment("Data Reverse:")
# https://www.codewars.com/kata/data-reverse/train/python
# A stream of data is received and needs to be reversed. Each segment is 8 bits
# meaning the order of these segments need to be reversed:
#
# 11111111 00000000 00001111 10101010
#
# (byte1) (byte2) (byte3) (byte4)
#
# 10101010 00001111 00000000 11111111
#
# (byte4) (byte3) (byte2) (byte1)
#
# Total number of bits will always be a multiple of 8. The data is given in an array as such:
#
# [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]

def data_reverse(data):
    output = []
    for byte_data in range(0,len(data),8):
        output.insert(0,data[byte_data:(byte_data+8)])
    return [item for sublist in output for item in sublist]


data1 = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
data2 = [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
test.describe("Data Reverse Tests:")
test.assert_equals(data_reverse(data1), data2)

data3 = [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]
data4 = [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0]
test.assert_equals(data_reverse(data3), data4)

# BRUXARIA!!!!
# def data_reverse(data):
#     return [b for a in range(len(data) - 8, -1, -8) for b in data[a:a + 8]]

###########################

comment("Give me a Diamond:")
# https://www.codewars.com/kata/give-me-a-diamond/train/python
#
# This kata is to practice simple string output. Jamie is a programmer,
# and James' girlfriend. She likes diamonds, and wants a diamond string from James.
# Since James doesn't know how to make this happen, he needs your help.
#
# ###Task:
#
# You need to return a string that displays a diamond shape on the screen using asterisk ("*")
# characters. Please see provided test cases for exact output format.
#
# The shape that will be returned from print method resembles a diamond,
# where the number provided as input represents the number of *’s printed on the middle line.
# The line above and below will be centered and will have 2 less *’s than the middle line.
# This reduction by 2 *’s for each line continues until a line with a single * is
# printed at the top and bottom of the figure.
#
# Return null if input is even number or negative (as it is not possible to
# print diamond with even number or negative number).
#
# Please see provided test case(s) for examples.
#
# Python Note
#
# Since print is a reserved word in Python, Python students must implement the diamond(n)
# method instead, and return None for invalid input.
#
# JS Note
#
# JS students, like Python ones, must implement the diamond(n) method, and return null for invalid input.



def diamond(n):
    stone =[]
    if n % 2 == 0 or n < 0:
        return None
    else:
        top = [("*" * (i)).center(n) for i in range(1, n + 1,2)]
        bottom = [("*" * (i)).center(n) for i in range(1, n,2)]
        top = "\n".join([line.rstrip() for line in top])
        bottom = bottom[::-1]
        bottom = "\n".join([line.rstrip() for line in bottom])
        stone.append(top)
        stone.append(bottom)
        return "\n".join(stone) + "\n" ## CRAP CODE!!!



# STUDY CASE:
# def diamond(n):
#     if n > 0 and n % 2 == 1:
#         diamond = ""
#         for i in range(n):
#             diamond += " " * abs((n/2) - i)
#             diamond += "*" * (n - abs((n-1) - 2 * i))
#             diamond += "\n"
#         return diamond
#     else:
#         return None

test.describe("Testing Diamonds:")
test.assert_equals(diamond(3), " *\n***\n *\n")
test.assert_equals(diamond(0), None)
test.assert_equals(diamond(2), None)
test.assert_equals(diamond(-1), None)
test.assert_equals(diamond(-2), None)


def known_diamond(n):
    if n % 2 == 0 or n < 0:
        return None
    result = []

    def append(c, n, nl):
        for _ in range(n):
            result.append(c)
        if nl:
            result.append('\n')

    indent = n // 2
    for i in xrange(indent, 0, -1):
        append(' ', i, False)
        append('*', n - 2 * i, True)
    append('*', n, True)
    for i in xrange(1, indent + 1):
        append(' ', i, False)
        append('*', n - 2 * i, True)
    return "".join(result)


test.assert_equals(diamond(5), known_diamond(5))
test.assert_equals(diamond(7), known_diamond(7))
test.assert_equals(diamond(15), known_diamond(15))


#############################
comment("Mexican Wave:")
# https://www.codewars.com/kata/mexican-wave/train/python
# Task
#
#  	In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up.
# Rules
#
#  	1.  The input string will always be lower case but maybe empty.
#
# 2.  If the character in the string is whitespace then pass over it as if it was an empty seat.
# Example
#
# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

def wave(str):
    output = []
    for pos in range(len(str)):
        output.append(str[:pos] + str[pos].capitalize() + str[(pos + 1):]) if str[pos] != " " else None
    return output

# Code here FIQUEI PERTO DA BRUXARIA!!!
# def wave(str):
#     return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]


result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
test.it("Should return: '[" + ", ".join(result) + "]'")
test.assert_equals(wave("hello"), result)

result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
test.it("Should return: '[" + ", ".join(result) + "]'")
test.assert_equals(wave("codewars"), result)

result = []
test.it("Should return: '[" + ", ".join(result) + "]'")
test.assert_equals(wave(""), result)

result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
test.it("Should return: '[" + ", ".join(result) + "]'")
test.assert_equals(wave("two words"), result)

result = [" Gap ", " gAp ", " gaP "]
test.it("Should return: '[" + ", ".join(result) + "]'")
test.assert_equals(wave(" gap "), result)


#################################

comment("Autocomplete! Yay!")
# https://www.codewars.com/kata/autocomplete-yay/train/python
#
# It's time to create an autocomplete function! Yay!
#
# The autocomplete function will take in an input string and a dictionary array and
# return the values from the dictionary that start with the input string.
#  If there are more than 5 matches, restrict your output to the first 5 results.
#  If there are no matches, return an empty array.
#
# Example:
#
# autocomplete('ai', ['airplane','airport','apple','ball']) = ['airplane','airport']
# For this kata, the dictionary will always be a valid array of strings.
# Please return all results in the order given in the dictionary,
# even if they're not always alphabetical. The search should NOT be case sensitive,
#  but the case of the word should be preserved when it's returned.
#
# For example, "Apple" and "airport" would both return for an input of 'a'.
# However, they should return as "Apple" and "airport" in their original cases.
#
# Important note:
#
# Any input that is NOT a letter should be treated as if it is not there.
# For example, an input of "$%^" should be treated as "" and an input of "ab*&1cd"
# should be treated as "abcd".
#
# (Thanks to wthit56 for the suggestion!)

def autocomplete(input_, dictionary):
    # output = []
    # for word in dictionary:
    #     output.append(word) if word.startswith(input_) else None
    #     if len(output) >= 5:
    #         break
    # return output
    return [word for word in dictionary if word.startswith(input_)][:5]
    # Estou virando bruxo!!! :D 100% meu!

# Ok... fix para caracteres estranhos:
import string
def autocomplete(input_, dictionary):
    input_ = "".join([x for x in input_ if x in string.ascii_letters])
    return [word for word in dictionary if word.lower().startswith(input_)][:5]

    #your code here

dictionary = ['abnormal',
              'arm-wrestling',
              'absolute',
              'airplane',
              'airport',
              'amazing',
              'apple',
              'ball']

Test.assert_equals(autocomplete('ai', dictionary), ['airplane', 'airport'])

#################################
comment("Prime in Numbers")
# https://www.codewars.com/kata/primes-in-numbers/train/python

# primes_under_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# def isprime(n):
#     if n <= 100:
#         return n in primes_under_100
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     for f in range(5, int(n ** .5), 6):
#         if n % f == 0 or n % (f + 2) == 0:
#             return False
#     return True
#
# def primes_under_(n):
#     return [prime for prime in range(n+1) if isprime(prime)]
#
# def display(primes_mult):
#     equation = ""
#     list_primes =
#     for prime in list_primes:
#         equation += "(" + str(prime) + "**" + str(primes_mult.count(prime)) + ")" if primes_mult.count(prime) > 1 else "(" + str(prime) + ")"
#     return equation
#
#
# def primeFactors(n, primes_mult=None, maxprime=100):
#     if primes_mult == None:
#         primes_mult = []
#     primes_list = primes_under_(maxprime)
#     for prime in primes_list:
#         if n % prime == 0:
#             primes_mult.append(prime)
#             n = int(n / prime)
#     if n != 1:
#         maxprime += 100
#         primeFactors(n,primes_mult, maxprime)
#     print(primes_mult)
#     return display(primes_mult)

import numpy as np
def display(primes_mult):
    equation = ""
    for prime in np.unique(primes_mult):
        equation += "(" + str(prime) + "**" + str(primes_mult.count(prime)) + ")" if primes_mult.count(prime) > 1 else "(" + str(prime) + ")"
    return equation

def primeFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return display(factors)


# primeFactors(18195729)
# primeFactors(7919)
# primeFactors(7775460)
# Bruxos fizeram (preciso aprender a usar o format!!!):

def primeFactors(n):
    ret = ''
    for i in xrange(2, n + 1):
        num = 0
        while(n % i == 0):
            num += 1
            n /= i
        if num > 0:
            ret += '({}{})'.format(i, '**%d' % num if num > 1 else '')
        if n == 1:
            return ret


test.assert_equals(primeFactors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
test.assert_equals(primeFactors(7919), "(7919)")
test.assert_equals(primeFactors(17*17*93*677), "(3)(17**2)(31)(677)")
test.assert_equals(primeFactors(933555431), "(7537)(123863)")
test.assert_equals(primeFactors(342217392), "(2**4)(3)(11)(43)(15073)")
test.assert_equals(primeFactors(35791357), "(7)(5113051)", )
test.assert_equals(primeFactors(782611830), "(2)(3**2)(5)(7**2)(11)(13)(17)(73)")
test.assert_equals(primeFactors(775878912), "(2**8)(3**4)(17)(31)(71)")


# I just got this idea - a platform for people to say what they want to eat and their preferences and cook around the area place their quotes for it. The app can be made viral by spreading it in a food festival.  How does it sound?  Example : one person requests that he wants  biryani for 8 people and says he wants food from a person who is pure vegetarian and it shows up to the cooks on that around area,  he may also specify the logistic information. It can also be marketed to bank and student hostels.


#####################################

comment("Moves in squared strings (II):")
# https://www.codewars.com/kata/moves-in-squared-strings-ii/train/python
# You are given a string of n lines, each substring being n characters long: For example:
#
# s = "abcd\nefgh\nijkl\nmnop"
#
# We will study some transformations of this square of strings.
#
# Clock rotation 180 degrees: rot
# rot(s) => "ponm\nlkji\nhgfe\ndcba"
# selfie_and_rot(s) (or selfieAndRot or selfie-and-rot)
# It is initial string + string obtained by clock rotation 180 degrees with dots interspersed in order (hopefully)
#  to better show the rotation when printed.
# s = "abcd\nefgh\nijkl\nmnop" -->
# "abcd....\nefgh....\nijkl....\nmnop....\n....ponm\n....lkji\n....hgfe\n....dcba"
# or printed:
# |rotation        |selfie_and_rot
# |abcd --> ponm   |abcd --> abcd....
# |efgh     lkji   |efgh     efgh....
# |ijkl     hgfe   |ijkl     ijkl....
# |mnop     dcba   |mnop     mnop....
#                            ....ponm
#                            ....lkji
#                            ....hgfe
#                            ....dcba
# #Task:
#
# Write these two functions rotand selfie_and_rot
# and
#
# high-order function oper(fct, s) where
#
# fct is the function of one variable f to apply to the string s (fct will be one of rot, selfie_and_rot)
# #Examples:
#
# s = "abcd\nefgh\nijkl\nmnop"
# oper(rot, s) => "ponm\nlkji\nhgfe\ndcba"
# oper(selfie_and_rot, s) => "abcd....\nefgh....\nijkl....\nmnop....\n....ponm\n....lkji\n....hgfe\n....dcba"
# Notes:
#
# The form of the parameter fct in oper changes according to the language. You can see each form according to
# the language in "Your test cases".
# It could be easier to take these katas from number (I) to number (IV)
# Forthcoming katas will study other tranformations.
#
# Bash Note:
#
# The input strings are separated by , instead of \n. The ouput strings should be separated by \r instead of \n.
# See "Sample Tests".

s = "abcd\nefgh\nijkl\nmnop"

def rot(s):
    return "\n".join([rotation[::-1] for rotation in s.split("\n")[::-1]])
    # your code

def add_dots(s):
    return "\n".join([word + "." * len(word) for word in s.split("\n")])

def selfie_and_rot(s):
    return add_dots(s) + "\n" + rot(add_dots(s))
    # your code

def oper(fct, s):
    return fct(s)
    # your code

def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe("opstrings")

Test.it("Basic tests rot")
testing(oper(rot, "fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL"),
        "LyfUVC\nGUFjWk\nABpfre\nJMmPrD\ntcVYqC\nooujif")
testing(oper(rot, "rkKv\ncofM\nzXkh\nflCB"), "BClf\nhkXz\nMfoc\nvKkr")

Test.it("Basic tests selfie_and_rot")
testing(oper(selfie_and_rot, "xZBV\njsbS\nJcpN\nfVnP"),
        "xZBV....\njsbS....\nJcpN....\nfVnP....\n....PnVf\n....NpcJ\n....Sbsj\n....VBZx")
testing(oper(selfie_and_rot, "uLcq\nJkuL\nYirX\nnwMB"),
        "uLcq....\nJkuL....\nYirX....\nnwMB....\n....BMwn\n....XriY\n....LukJ\n....qcLu")

def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe("opstrings")

Test.it("Basic tests rot")
testing(oper(rot, "fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL"), "LyfUVC\nGUFjWk\nABpfre\nJMmPrD\ntcVYqC\nooujif")
testing(oper(rot, "rkKv\ncofM\nzXkh\nflCB"), "BClf\nhkXz\nMfoc\nvKkr")
testing(oper(rot, "lVHt\nJVhv\nCSbg\nyeCt"), "tCey\ngbSC\nvhVJ\ntHVl")
testing(oper(rot, "QMxo\ntmFe\nWLUG\nowoq"), "qowo\nGULW\neFmt\noxMQ")

Test.it("Basic tests selfie_and_rot")
testing(oper(selfie_and_rot, "xZBV\njsbS\nJcpN\nfVnP"),
    "xZBV....\njsbS....\nJcpN....\nfVnP....\n....PnVf\n....NpcJ\n....Sbsj\n....VBZx")
testing(oper(selfie_and_rot, "uLcq\nJkuL\nYirX\nnwMB"),
    "uLcq....\nJkuL....\nYirX....\nnwMB....\n....BMwn\n....XriY\n....LukJ\n....qcLu")
testing(oper(selfie_and_rot, "lVHt\nJVhv\nCSbg\nyeCt"),
        "lVHt....\nJVhv....\nCSbg....\nyeCt....\n....tCey\n....gbSC\n....vhVJ\n....tHVl")
testing(oper(selfie_and_rot, "QMxo\ntmFe\nWLUG\nowoq"),
        "QMxo....\ntmFe....\nWLUG....\nowoq....\n....qowo\n....GULW\n....eFmt\n....oxMQ")

from random import randint

def do_ex(k):
    if (k % 2 == 1): k += 1
    j , res = 0, []
    while (j < k):
        s, i = "", 0
        while (i < k):
            if (randint(0, 100) % 2 == 0): s += chr(randint(97, 122))
            else: s += chr(randint(65, 90))
            i += 1
        res.append(s)
        j += 1
    return "\n".join(res)

def vert_mirror213(strng):
    return "\n".join(map (lambda x: x[::-1], strng.split("\n")))
def hor_mirror213(strng):
    return "\n".join(strng.split("\n")[::-1])
def rot213(strng):
    return vert_mirror213(hor_mirror213(strng))
def selfie_and_rot213(strng):
    newstr1 = "\n".join(map (lambda x: x + '.' * len(x), strng.split("\n")))
    newstr2 = "\n".join(map(lambda x: '.' * len(x) + x, rot213(strng).split("\n")))
    return newstr1 + "\n" + newstr2

def tests_code1():
    print("Random tests rot")
    i = 0
    while (i < 100):
        s = do_ex(randint(8,20))
        testing(oper(rot, s), rot213(s))
        i += 1
tests_code1()
def tests_code2():
    print("Random tests selfie_and_rot")
    i = 0
    while (i < 100):
        s = do_ex(randint(8,20))
        testing(oper(selfie_and_rot, s), selfie_and_rot213(s))
        i += 1
tests_code2()

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

testar(sol_equa)



############################################
comment("Write out Numbers:")
# https://www.codewars.com/kata/write-out-numbers/train/python

# Create a function that transforms any positive number to a string representing the number in words.
#  The function should work for all numbers between 0 and 999999.

def number2words(n):
    words = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
                 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
                 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
                 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', \
                 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', \
                 90: 'ninety', 100: 'hundred', 1000: 'thousand'}
    if n in words.keys():
        if n == 100 or n == 1000:
            return words[1] + " " + words[n]
        return words[n]
    else:
        digits = len(str(n))
        if digits == 2:
            e0 = words[n%10] if n%10 != 0 else ""
            e1 = words[(n//10)*10] if (n//10)*10 != 0 else ""
            return  "-".join([e1, e0])
        if digits == 3:
            e2 = " ".join([number2words(n // 100), words[100]])
            e = number2words(n - n//100*100) if n - n//100*100 != 0 else ""
            return " ".join([e2,e]) if e != "" else e2
        if digits >= 4 and digits <= 6:
            e3 = " ".join([number2words(n//1000), words[1000]])
            e = number2words(n - n//1000*1000) if n - n//1000*1000 != 0 else ""
            return " ".join([e3, e]) if e != "" else e3
        # if digits == 5:
        #     number2words(n//10000)



# https://www.codewars.com/kata/52724507b149fa120600031d/solutions/python

test.assert_equals(number2words(0), "zero")
test.assert_equals(number2words(1), "one")
test.assert_equals(number2words(8), "eight")
test.assert_equals(number2words(10), "ten")
test.assert_equals(number2words(19), "nineteen")
test.assert_equals(number2words(20), "twenty")
test.assert_equals(number2words(22), "twenty-two")
test.assert_equals(number2words(54), "fifty-four")
test.assert_equals(number2words(80), "eighty")
test.assert_equals(number2words(98), "ninety-eight")
test.assert_equals(number2words(100), "one hundred")
test.assert_equals(number2words(301), "three hundred one")
test.assert_equals(number2words(793), "seven hundred ninety-three")
test.assert_equals(number2words(800), "eight hundred")
test.assert_equals(number2words(650), "six hundred fifty")
test.assert_equals(number2words(1000), "one thousand")
test.assert_equals(number2words(1003), "one thousand three")
test.assert_equals(number2words(950),"nine hundred fifty")
test.assert_equals(number2words(1000),"one thousand")
test.assert_equals(number2words(1002),"one thousand two")
test.assert_equals(number2words(3051),"three thousand fifty-one")
test.assert_equals(number2words(7200),"seven thousand two hundred")
test.assert_equals(number2words(7219),"seven thousand two hundred nineteen")
test.assert_equals(number2words(8330),"eight thousand three hundred thirty")
test.assert_equals(number2words(99999),"ninety-nine thousand nine hundred ninety-nine")
test.assert_equals(number2words(888888),"eight hundred eighty-eight thousand eight hundred eighty-eight")


############################################
comment("Take a Ten Minute Walk:")
# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python
#
# You live in the city of Cartesia where all roads are laid out in a perfect grid.
# You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.
# The city provides its citizens with a Walk Generating App on their phones --
# everytime you press the button it sends you an array of one-letter strings representing directions to walk
# (eg. ['n', 's', 'w', 'e']). You know it takes you one minute to traverse one city block,
# so create a function that will return true if the walk the app gives you will take you exactly ten minutes
#  (you don't want to be early or late!) and will, of course, return you to your starting point.
# Return false otherwise.
#
# Note: you will always receive a valid array containing a random assortment of direction letters
# ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

def isValidWalk(walk):
    if len(walk) == 40:
        if walk.count('n') == walk.count('s'):
            if walk.count('e') == walk.count('w'):
                return True
        return False
    else:
        return False

# test.describe("Take a Ten Minutes Walk Testing...")
# for i in range(2): # test as many times as you want, just change the number
#     test1 = create_tests(random.randint(0,20))
#     test.assert_equals(isValidWalk(test1[0]),test1[1])

#########################
comment("Playing with digits")
# https://www.codewars.com/kata/playing-with-digits/train/python
# Some numbers have funny properties. For example:
#
# 89 --> 8¹ + 9² = 89 * 1
#
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
#
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n. In other words:
#
# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
# If it is the case we will return k, if not return -1.
#
# Note: n, p will always be given as strictly positive integers.
#
# dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
# dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
# dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
# dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
def dig_pow(n, p):
    num_list = [int(d) for d in str(n)]
    pow = [ps for ps in range(p,len(num_list)+p)]
    sum_pow = sum(num_list[i]**pow[i] for i in range(len(num_list)))
    return (sum_pow // n) if sum_pow % n == 0 else -1


    # your code
test.describe("Testing Playing with Digits")
test.assert_equals(dig_pow(89, 1), 1)
test.assert_equals(dig_pow(92, 1), -1)
test.assert_equals(dig_pow(46288, 3), 51)
test.assert_equals(dig_pow(114, 3), 9)
test.assert_equals(dig_pow(46288, 5), -1)
test.assert_equals(dig_pow(135, 1), 1)
test.assert_equals(dig_pow(175, 1), 1)
test.assert_equals(dig_pow(518, 1), 1)
test.assert_equals(dig_pow(598, 1), 1)
test.assert_equals(dig_pow(1306, 1), 1)
test.assert_equals(dig_pow(2427, 1), 1)
test.assert_equals(dig_pow(2646798, 1), 1)
test.assert_equals(dig_pow(3456789, 1), -1)
test.assert_equals(dig_pow(3456789, 5), -1)
test.assert_equals(dig_pow(198, 1), 3)
test.assert_equals(dig_pow(249, 1), 3)
test.assert_equals(dig_pow(1377, 1), 2)
test.assert_equals(dig_pow(1676, 1), 1)
test.assert_equals(dig_pow(695, 2), 2)
test.assert_equals(dig_pow(1878, 2), 19)
test.assert_equals(dig_pow(7388, 2), 5)
test.assert_equals(dig_pow(47016, 2), 1)
test.assert_equals(dig_pow(542186, 2), 1)
test.assert_equals(dig_pow(261, 3), 5)
test.assert_equals(dig_pow(1385, 3), 35)
test.assert_equals(dig_pow(2697, 3), 66)
test.assert_equals(dig_pow(6376, 3), 10)
test.assert_equals(dig_pow(6714, 3), 1)
test.assert_equals(dig_pow(63760, 3), 1)
test.assert_equals(dig_pow(63761, 3), 1)
test.assert_equals(dig_pow(132921, 3), 4)
test.assert_equals(dig_pow(10383, 6), 12933)


##################################################
comment("The Enigma Machine - Part 1: The Plugboard")
# https://www.codewars.com/kata/the-enigma-machine-part-1-the-plugboard/train/python

# In this series of Kata, we will be implementing a software version of the Enigma Machine.
#
# The Enigma Machine was a message enciphering/deciphering machine used during the Second World War for
# disguising the content of military communications. Alan Turing - the father of computing -
# formulated and developed concepts that are the basis of all computers in use today, he did this in response
# to the vital need to break those military communications. Turing and his colleagues at Bletchley Park are
# generally recognised as being responsible for shortening WWII by two years and saving an estimated 22 Million lives.
#
# The Enigma Machine consisted of a number of parts: Keyboard for input, rotors and plugboard for enciphering,
# and lampboard for output.
#
# We will simulate input and output with strings, and build the rotors, plugboard and mechanism that used them
#  in software. As we progress the code will become more complex, so you are advised to attempt them in order.
#
# Step 1: The plugboard
#
# In this Kata, you must implement the plugboard.
#
# Physical Description
#
# The plugboard crosswired the 26 letters of the latin alphabet togther, so that an input into one letter
# could generate output as another letter. If a wire was not present, then the input letter was unchanged.
# Each plugboard came with a maximum of 10 wires, so at least six letters were not cross-wired.
#
# For example:
#
# If a wire connects A to B, then an A input will generate a B output and a B input will generate an A output.
# If no wire connects to C, then only a C input will generate a C output.
# Note
#
# In the actual usage of the original Enigma Machine, punctuation was encoded as words transmitted in the stream,
# in our code, anything that is not in the range A-Z will be returned unchanged.
#
# Kata
#
# The Plugboard class you will implement, will:
#
# Take a list of wire pairs at construction in the form of a string, with a default behaviour of no wires configured.
# E.g. "ABCD" would wire A <-> B and C <-> D.
# Validate that the wire pairings are legitimate. Raise an exception if not.
# Implement the process method to translate a single character input into an output.
# Haskell remarks
#
# Since Haskell doesn't have classes, plugboard is a function that either returns a
# Char -> Char function for processing, or an error message.
#
# Examples
#
# plugboard = Plugboard("ABCDEFGHIJKLMNOPQRST")
# print plugboard.process("A")
# print plugboard.process("B")
# print plugboard.process("X")
# print plugboard.process(".")
# Expected output:
#
# B
# A
# X
# .

class Plugboard(object):
    def __init__(self, wires = ""):
        if len(wires) > 20:
            raise Exception("Should not have accepted too many wires defined")
        if len(wires) % 2 != 0:
            raise Exception("Should not have accepted a partial wire definition")
        for chr in wires:
            if wires.count(chr) > 1:
                raise Exception("Should not have accepted a second definition for a wire end")
        self.wires = wires.upper()
    def process(self, c):
        c = c.capitalize()
        output =  "".join([pair for pair in map(''.join, zip(*[iter(self.wires)]*2))
                        if c in pair]).strip(c)
        return output if output != "" else c




# p = Plugboard("ABCD")
# p.process("C")


### Todo:  Escrever a expect_error
# test.it("Too many wires defined")
# test.expect_error(
#     "Should not have accepted too many wires defined",
#     lambda: Plugboard("ABCDEFGHIJKLMNOPQRSTUV"))
# https://www.codewars.com/kata/5523b97ac8f5025c45000900/solutions/python
test.it("Character processing")
plugboard = Plugboard("AB")
test.assert_equals(plugboard.process('A'), 'B')
test.assert_equals(plugboard.process('B'), 'A')
test.assert_equals(plugboard.process('C'), 'C')

##########################################


comment("Linked List Alternating Split")
# https://www.codewars.com/kata/linked-lists-alternating-split/train/python
#
# Linked Lists - Alternating Split
#
# Write an AlternatingSplit() function that takes one list and divides up its nodes to make two smaller lists.
#
# The sublists should be made from alternating elements in the original list.
# So if the original list is a -> b -> a -> b -> a -> null then one sublist
# should be a -> a -> a -> null and the other should be b -> b -> null.

# ###Python
# 
# list = 1 -> 2 -> 3 -> 4 -> 5 -> None
# alternating_split(list).first == 1 -> 3 -> 5 -> None
# alternating_split(list).second == 2 -> 4 -> None

# For simplicity, we use a Context object to store and return the state of the two linked lists.
# A Context object containing the two mutated lists should be returned by AlternatingSplit().
#
# If the passed in head node is null/None/nil or a single node, throw an error.
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext
    def setPrev(self,newprev):
        self.prev = newprev
    def getPrev(self):
        return self.prev

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise "Error, just don't"

    node = head
    node_1_prev, node_2_prev = None, None

    is_node_1 = True
    while node:
        if is_node_1:
            node_1 = Node(node.data)
            if node_1_prev:
                node_1_prev.next = node_1
            else:
                #Clone the object
                node_1_new = node_1
            node_1_prev = node_1
            is_node_1 = False
        else:
            node_2 = Node(node.data)
            if node_2_prev:
                node_2_prev.next = node_2
            else:
                node_2_new = node_2
            node_2_prev = node_2
            is_node_1 = True
        node = node.next

    return Context(node_1_new, node_2_new)

# Bruxaria!!!
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError('Bad input')

    orig_a, orig_b = a, b = Node(), Node()

    while head:
        a.next = Node(head.data)
        a = a.next
        a, b = b, a
        head = head.next

    return Context(orig_a.next, orig_b.next)

#Eu fazendo por String:
# def alternating_split(head):
#     if not head:
#         raise ValueError
#     if not head.next:
#         raise ValueError
#     mylist = head.split(" -> ")
#     first_list = [item for item in mylist if mylist.index(item) % 2 == 0 ]
#     second_list = [item for item in mylist if mylist.index(item) % 2 == 1]
#     context = Context(first_list,second_list)

# Your code goes here.
# Remember to return the context.

# test.it("should be able to handle an empty list.")
# test.expect_error("splitting a None list should throw an error.", lambda : alternating_split(None))
#
# test.it("should be able to handle a list of length 1.")
# test.expect_error("splitting a single node list should throw an error.", lambda : alternating_split(Node(23)))

test.it("should be able to handle a list of length 2.")
# test.assert_equals(alternating_split(build_one_two()).first.data, 1, "First index of first linked list should have value of 1.")
# test.assert_equals(alternating_split(build_one_two()).first.next, None, "Second index of first linked list should be None.")
# test.assert_equals(alternating_split(build_one_two()).second.data, 2, "First index of second linked list should have value of 2.")
# test.assert_equals(alternating_split(build_one_two()).second.next, None, "Second index of second linked list should be None.")

test.it("should be able to handle a list of length 3")
# test.assert_equals(alternating_split(build_one_two_three()).first.data, 1, "First index of first linked list should have value of 1.")
# test.assert_equals(alternating_split(build_one_two_three()).first.next.data, 3, "Second index of first linked list should have value 3.")
# test.assert_equals(alternating_split(build_one_two_three()).first.next.next, None, "Third index of first linked list should be None.")
# test.assert_equals(alternating_split(build_one_two_three()).second.data, 2, "First index of second linked list should have value of 2.")
# test.assert_equals(alternating_split(build_one_two_three()).second.next, None, "Second index of second linked list should be None.")

test.it("should be able to handle a list of length 6")
# assert_linked_list_equals(alternating_split(build_one_two_three_four_five_six()).first, build_list([1, 3, 5]), "First list of alternating_split(1 -> 2 -> 3 -> ... 6 -> None) should be 1 -> 3 -> 5 -> None")
# assert_linked_list_equals(alternating_split(build_one_two_three_four_five_six()).second, build_list([2, 4, 6]), "Second list of alternating_split(1 -> 2 -> 3 -> ... 6 -> None) should be 2 -> 4 -> 6 -> None")
# test.assert_equals(alternating_split(build_one_two_three_four_five_six()).first.next.next.next, None, "Fourth index of first linked list should be None.")
# test.assert_equals(alternating_split(build_one_two_three_four_five_six()).second.next.next.next, None, "Fourth index of second linked list should be None.")

test.it("should be able to handle a list of length 11")
# assert_linked_list_equals(alternating_split(build_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])).first, build_list([1, 3, 5, 7, 9, 11]), "First list of alternating_split(1 -> 2 -> 3 -> ... 11 -> None) should be 1 -> 3 -> 5 -> 7 -> 9 -> 11 -> None")
# assert_linked_list_equals(alternating_split(build_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])).second, build_list([2, 4, 6, 8, 10]), "Second list of alternating_split(1 -> 2 -> 3 -> ... 11 -> None) should be 2 -> 4 -> 6 -> 8 -> 10 -> None")
# assert_linked_list_equals(alternating_split(build_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])).first.next.next.next.next.next.next, None, "Seventh index of first linked list should be None.")
# assert_linked_list_equals(alternating_split(build_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])).second.next.next.next.next.next, None, "Sixth index of second linked list should be None.")

test.it("should be able to handle are large unordered list.")
# assert_linked_list_equals(alternating_split(build_list([5, 6, 1, 2, 3, 3, 3, 4, 8, 5, 4, 1])).first, build_list([5, 1, 3, 3, 8, 4]), "First list of alternating_split(5 -> 6 -> 1 -> 2 -> 3 -> 3 -> 3 -> 4 -> 8 -> 5 -> 4 -> 1 -> None) should be 5 -> 1 -> 3 -> 3 -> 8 -> 4 -> None")
# assert_linked_list_equals(alternating_split(build_list([5, 6, 1, 2, 3, 3, 3, 4, 8, 5, 4, 1])).second, build_list([6, 2, 3, 4, 5, 1]), "Second list of alternating_split(5 -> 6 -> 1 -> 2 -> 3 -> 3 -> 3 -> 4 -> 8 -> 5 -> 4 -> 1 -> None) should be 6 -> 2 -> 3 -> 4 -> 5 -> -> 1 -> None")
# assert_linked_list_equals(alternating_split(build_list([5, 6, 1, 2, 3, 3, 3, 4, 8, 5, 4, 1])).first.next.next.next.next.next.next, None, "Seventh index of first linked list should be None.")
# assert_linked_list_equals(alternating_split(build_list([5, 6, 1, 2, 3, 3, 3, 4, 8, 5, 4, 1])).second.next.next.next.next.next.next, None, "Seventh index of second linked list should be None.")


##############################################


comment("Phone Directory")
# https://www.codewars.com/kata/56baeae7022c16dd7400086e/train/python
#
# John keeps a backup of his old personal phone book as a text file.
# On each line of the file he can find the phone number (formated as +X-abc-def-ghij
# where X stands for one or two digits), the corresponding name between < and > and the address.
#
# Unfortunately everything is mixed, things are not always in the same order,
# lines are cluttered with non-alpha-numeric characters.
#
# Examples of John's phone book lines:
#
# "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n"
#
# " 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"
#
# "<Anastasia> +48-421-674-8974 Via Quirinal Roma\n"
#
# Could you help John with a program that, given the lines of his phone book and
# a phone number returns a string for this number : "Phone => num, Name => name, Address => adress"
#
# Examples:
#
# s = "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"
#
# phone(s, "1-541-754-3010") should return "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St."
# It can happen that, for a few phone numbers, there are many people for a phone number -say nb- , then
#
# return : "Error => Too many people: nb"
#
# or it can happen that the number nb is not in the phone book, in that case
#
# return: "Error => Not found: nb"
#
# You can see other examples in the test cases.
#
# JavaScript random tests completed by @matt c
#
# Note
# Codewars stdout doesn't print part of a string when between < and >

# Todo:
# 1- break by line (from beginning to \n)

# 2- regex phone, regex name, rest is address.

# phone:    \+([1-99])\D*([2-9]\d{2})(\D*)([2-9]\d{2})(\D*)(\d{4})\D*
#           \+([1-9]*[1-9])-([0-9]\d{2})-([0-9]\d{2})-([0-9]\d{3})
import re

class Phonebook(object):
    def __init__(self):
        self.people = []


    def add_person(self, person):
        self.people.append(person)

    def __iter__(self):
        for elem in self.people:
            yield elem

    def find_phone(self, phone ):
        found = []
        for person in self.people:
            if str(person.phone) == str(phone):
                found.append(person)
        return found



class Person(object):
    def __init__(self, name, phone=None, address=None):
        self.name = name
        self.phone = phone
        self.address = address

    def add_phone(self, number):
        self.phone = number

    def add_address(self, address):
        self.address = address

    def show(self):
        print("Data:")
        s = 'name: %s \n' % self.name
        if self.phone is not None:
            s += 'general phone:   %s\n' % self.phone
        if self.address is not None:
            s += 'address address:  %s\n' % self.address
        print (s)




def phone(strng, num):
# Working with the given data:
    phonebook = Phonebook()
    datas = strng.split("\n")
    datas = [data for data in datas if data]

    for data in datas:
        tel = re.findall("([1-9]*[1-9]-[0-9]\d{2}-[0-9]\d{2}-[0-9]\d{3})", data)[0]
        name = re.findall("(?<=\<)(.*?)(?=\>)", data)[0]
        address = data.replace(tel,"")
        address = address.replace("<" + name + ">", "")
        address = re.sub('[^A-Za-z0-9-" ."]+', ' ', address)
        address = " ".join(address.split())
    # Now with the data clean, add it to a person:
        person = Person(name=name, phone=tel, address=address)
    # And add the person to phonebook
        phonebook.add_person(person)
    # Find the person by the Phone:
    results = phonebook.find_phone(num)
    if len(results) == 1:
        return ("Phone => {}, Name => {}, Address => {}".format(results[0].phone, results[0].name, results[0].address))
    if len(results) > 1:
        return "Error => Too many people: {}".format(num)
    if len(results) == 0:
        return "Error => Not found: {}".format(num)


# strip the information that I already have...

dr = ("/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;\n"
"+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209\n"
"+1-741-984-3090 <Peter Reedgrave> _Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209\n"
"+1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209\n"
"<Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222!\n"
"<Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,\n"
"<Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209\n"
"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver\n"
"<C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado\n"
"+1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071\n"
"<P Salinge> Main Street, +1-098-512-2222, Denve\n")

def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe("phone")
Test.it("Basic tests")
testing(phone(dr, "48-421-674-8974"), "Phone => 48-421-674-8974, Name => Anastasia, Address => Via Quirinal Roma")
testing(phone(dr, "1-921-512-2222"), "Phone => 1-921-512-2222, Name => Wilfrid Stevens, Address => Wild Street AA-67209")
testing(phone(dr, "1-908-512-2222"), "Phone => 1-908-512-2222, Name => Peter O'Brien, Address => High Street CC-47209")
testing(phone(dr, "1-541-754-3010"), "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St.")
testing(phone(dr, "1-121-504-8974"), "Phone => 1-121-504-8974, Name => Arthur Clarke, Address => San Antonio TT-45120")
testing(phone(dr, "1-498-512-2222"), "Phone => 1-498-512-2222, Name => Bernard Deltheil, Address => Mount Av. Eldorado")
testing(phone(dr, "1-098-512-2222"), "Error => Too many people: 1-098-512-2222")
testing(phone(dr, "5-555-555-5555"), "Error => Not found: 5-555-555-5555")


### BRUXARIA !!! REGEX:
from re import sub


def phone2(dir, num):
    if dir.count("+" + num) == 0:
        return "Error => Not found: " + num

    if dir.count("+" + num) > 1:
        return "Error => Too many people: " + num

    for line in dir.splitlines():
        if "+" + num in line:
            name = sub(".*<(.*)>.*", "\g<1>", line)
            line = sub("<" + name + ">|\+" + num, "", line)
            address = " ".join(sub("[^a-zA-Z0-9\.-]", " ", line).split())
            return "Phone => %s, Name => %s, Address => %s" % (num, name, address)


###############################

comment("#9 Matrices: Adding diagonal products")
# https://www.codewars.com/kata/number-9-matrices-adding-diagonal-products/train/python
#
# We have a square matrix M of dimension n x n that has positive and negative numbers in the ranges [-9,-1] and [0,9],
# ( the value 0 is excluded).
#
# We want to add up all the products of the elements of the diagonals UP-LEFT to DOWN-BOTTOM, that is the value ofsum1;
# and the elements of the diagonals UP-RIGHT to LEFT-DOWN and that is sum2. Then, as a final result,
#  the value of sum1 - sum2.
#
# E.g.
#
# M = [[ 1,  4, 7,  6,  5],
#      [-3,  2, 8,  1,  3],
#      [ 6,  2, 9,  7, -4],
#      [ 1, -2, 4, -2,  6],
#      [ 3,  2, 2, -4,  7]]
# Let's see how to get this result in the image below:
#
# source: http://i.imgur.com/MHfydrP.jpg?1
#
# So the value of sum1 - sum2 is equal to:
#
# 1164 - 66 = 1098
# Create the code to do this calculation.
#
# Features of the random tests:
#
# Numbers of tests = 150
# 10 < dimension < 25 (python and ruby)
# 10 < dimension < 20 (javascript)
# -10 < M[i,j] < 0 and 0 < M[i,j] < 10
# This kata is available in Python2, Ruby and Javascript by the moment. Translations into another languages will be released soon. Enjoy it!
import numpy as np
def sum_prod_diags(matrix):
    fliped = np.fliplr(matrix)
    spread = list(range(-len(matrix)+1,len(matrix)))
    diag1, diag2 = [], []
    for i in spread:
        diag1.append(np.diag(matrix,i))
        diag2.append(np.diag(fliped,i))
    prod1,prod2 = [], []
    for diagonal in diag1:
        prod1.append(np.prod(diagonal))
    for diagonal in diag2:
        prod2.append(np.prod(diagonal))
    return sum(prod1) - sum(prod2)
    # diag0 = (0,0)
    # diag1 = (0,1), (1,0)
    # diag2 = (0,2), (1,1), (2,0)
    # diag3 = (0,3), (1,2), (2,1), (3,0)
    # diag4 = (1,3), (2,2), (3,1)
    # diag5 = (2,3), (3,2)
    # diag6 = (3,3)
    #
    # diag13 = (0, 3)
    # diag12 = (0, 2), (1, 3)
    # diag11 = (0, 1), (1, 2), (2, 3)
    # diag10 = (0, 0), (1,1), (2,2), (3,3)
    # diag9  = (1, 0), (2, 1), (3, 2)
    # diag8  = (2, 0), (3, 1)
    # diag7  = (3, 0)

    # 5 x 5 = 25 -> 18 diag
    # 4 x 4 = 16 -> 14 diag

    # sum1 = current index + (len(line) + 1)
    # sum2 = current index + (len(line) - 1)
    # your code here
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    #



M = [[(0,0), (0,1), (0,2), (0,3)],
     [(1,0), (1,1), (1,2), (1,3)],
     [(2,0), (2,1), (2,2), (2,3)],
     [(3,0), (3,1), (3,2), (3,3)]]


MT = [[1,   2,   3,  4],
      [5,   6,   7,  8],
      [9,  10,  11, 12],
      [13, 14,  15, 16]]
test.describe("Basic Tests")

M1 = [[1,  4, 7,  6,  5],
      [-3, 2, 8,  1,  3],
      [6,  2, 9,  7, -4],
      [1, -2, 4, -2,  6],
      [3,  2, 2, -4,  7]]

test.assert_equals(sum_prod_diags(M1), 1098)

M2 = [[1, 4, 7, 6],
      [-3, 2, 8, 1],
      [6, 2, 9, 7],
      [1, -2, 4, -2]]

test.assert_equals(sum_prod_diags(M2), -11)

M3 = [[1, 2, 3, 2, 1],
      [2, 3, 4, 3, 2],
      [3, 4, 5, 4, 3],
      [4, 5, 6, 5, 4],
      [5, 6, 7, 6, 5]]

test.assert_equals(sum_prod_diags(M3), 0)


matrix = [[8, -4, -4, 2, 8, 9, -6, 7, 5, 3, 3, -4, 1, -6, 6, 7, 6, 9, -1, 1, 8, -9, 7, -1, 7],
          [9, 9, -8, -1, -5, 8, -2, -7, 9, -3, 7, -3, -1, 1, 5, 1, -7, 1, -8, -9, 4, 5, -8, -7, -5],
          [4, 7, -1, -2, -5, 2, 9, 3, 7, 9, -8, 5, -5, 4, -1, 1, 8, 1, -8, 7, 2, -6, 6, 5, 5],
          [8, 6, -2, -7, 3, 4, -5, -6, -5, 5, -6, 7, -6, 3, 4, 4, 7, 4, -8, -7, -2, -5, -2, -9, 3],
          [3, -3, 5, 6, -8, 7, -1, 1, 3, 4, -6, 8, 8, 1, 6, -6, -2, -9, -8, 5, -8, 4, 3, -2, -6],
          [7, -3, 8, 3, -8, 3, 2, -3, 8, 6, 5, 7, 4, -3, -1, 7, 3, -3, 2, 2, -8, 2, 6, -7, 6],
          [-4, 5, 3, -8, -5, 2, -7, 5, 9, 1, -3, 9, -1, 9, 3, -1, 3, 1, -8, 2, -5, -5, 9, -5, -5],
          [-2, 1, -7, 6, 7, 6, -3, 8, -4, -8, 1, -8, -3, -6, -4, 6, -2, -6, -6, -9, -4, -4, -1, -2, -8],
          [1, 2, 6, 5, 8, -8, -1, -9, 8, -4, -9, -3, 2, -6, 4, -6, 3, 9, -6, -1, 4, 7, 9, 4, 6],
          [-5, 8, -5, 9, -5, -1, -4, -3, -4, 6, -5, 1, -1, -6, 9, -5, -7, 5, -1, -1, -8, 3, 1, -2, 8],
          [9, 9, -6, 5, 8, -9, -4, -1, 5, -4, -7, -2, 5, 4, 9, -6, -8, -1, -5, -1, -9, 6, 1, -3, 3],
          [-9, -4, 8, 6, -5, -2, -2, -6, -9, -5, -6, -6, 6, -8, 2, 4, -8, -2, -1, 2, -2, 2, 9, 2, 6],
          [-3, -3, 3, 7, -1, -8, -8, -8, 4, -6, -6, -4, -9, -1, -5, 5, 8, 6, 8, 2, 8, 9, 1, -9, -7],
          [-7, 4, 8, 4, 8, 2, -5, 2, 9, 3, 9, 6, -8, -7, 9, 8, 2, 5, -7, -1, 3, -3, 7, -1, -3],
          [-3, 8, -6, 8, -7, -1, -9, -7, -7, -6, -9, -2, 3, -1, 7, 3, 8, 6, 6, 9, 1, -7, -2, 8, -1],
          [2, 2, 8, -8, 2, -4, -3, 7, 6, 3, 8, -5, -1, -5, 2, 9, -8, 4, -4, 1, 1, 5, -1, 5, 5],
          [-8, -7, -8, 7, -7, -5, 8, -2, 2, -1, 3, -4, 2, 4, 1, 7, -5, 9, 2, -4, -9, -4, -1, 2, 6],
          [-1, -7, -1, -3, -2, -5, 5, -3, -7, -4, 3, 2, 7, 3, -6, -3, -5, 7, 3, 4, -5, 4, 4, -3, 8],
          [-4, -2, 3, 2, 4, -5, -4, -5, -6, -1, -6, -8, 4, 6, -2, -8, 7, -1, -9, -4, -5, -1, -4, 9, 3],
          [-9, 9, -9, -5, 5, 9, -8, -9, -3, -9, -8, -5, 7, 6, -5, 5, -4, -8, 2, -1, 8, 3, -7, -7, 1],
          [-9, 7, -9, -9, -7, 9, -4, -8, -4, 4, -8, -3, 5, -1, -8, -4, -8, 1, -9, 9, 8, -5, 4, -6, 7],
          [-5, 9, 7, -1, 5, -8, 4, -6, 8, 3, -5, -6, -1, 9, -2, -4, -3, 8, -7, -2, 8, 3, -3, 7, 4],
          [1, -3, 1, -5, -3, -7, 1, 1, -7, 8, 4, -1, 4, 2, 8, 8, 3, -2, -1, -9, 8, 6, -8, -9, 2],
          [-2, 1, -6, -9, 9, 7, 2, -9, -7, -6, -6, -9, 5, 5, -9, 1, -7, -6, 5, 6, -5, 4, -9, -8, 9],
          [-6, -4, -3, -9, 2, -8, -8, 9, 1, -7, 4, 1, 9, -2, -9, 1, 7, -5, -5, 7, -3, -2, -4, 4, 7]]



#################################
comment("ROT13")
# https://www.codewars.com/kata/rot13-1/train/python
#
# ROT13 is a simple letter substitution cipher that replaces a letter with
# the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
#
# Create a function that takes a string and returns the string ciphered with Rot13.
# If there are numbers or special characters included in the string, they should be returned as they are.
# Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
#
# Please note that using "encode" in Python is considered cheating.


import string
# from codecs import encode as _dont_use_this_

def rot13(message):
    lowletters1 = string.ascii_lowercase[:13]
    lowletters2 = string.ascii_lowercase[13:]
    upperletters1 = string.ascii_uppercase[:13]
    upperletters2 = string.ascii_uppercase[13:]
    dictlow1 = dict(zip(lowletters1, lowletters2))
    dictlow2 = dict(zip(lowletters2, lowletters1))
    dictupper1 = dict(zip(upperletters1, upperletters2))
    dictupper2 = dict(zip(upperletters2, upperletters1))
    mydict = {**dictlow1, **dictupper1, **dictlow2, **dictupper2}
    # To simplify....
    #     input = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    #     output = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    #     mydict = dict(zip(input,output))
    cripted = ""
    for chr in message:
        if chr in mydict.keys():
            cripted += mydict[chr]
        else:
            cripted += chr
    return cripted


test.assert_equals(rot13("test"),"grfg")
test.assert_equals(rot13("Test"),"Grfg")




####################
comment("Closest and Smallest")
# https://www.codewars.com/kata/closest-and-smallest/train/python
#
# Input
#
# a string strng of n positive numbers (n = 0 or n >= 2)
# Let us call weight of a number the sum of its digits. For example 99
# will have "weight" 18, 100 will have "weight" 1.
#
# Two numbers are "close" if the difference of their weights is small.
#
# Task:
# For each number in strng calculate its "weight" and then find two numbers of strng that have:
#
# the smallest difference of weights ie that are the closest
# with the smallest weights
# and with the smallest indices (or ranks, numbered from 0) in strng
# Output:
#
# an array of two arrays, each subarray in the following format:
# [number-weight, index in strng of the corresponding number, original corresponding number instrng]
#
# or a pair of two subarrays (Haskell, Clojure, FSharp) or an array of tuples (Elixir, C++)
#
# or a (char*) in C mimicking an array of two subarrays
#
# or a matrix in R (2 rows, 3 columns, no columns names)
#
# The two subarrays are sorted in ascending order by their number weights
# if these weights are different, by their indexes in the string if they have the same weights.
#
# Examples:
# Let us call that function closest
#
# strng = "103 123 4444 99 2000"
# the weights are 4, 6, 16, 18, 2 (ie 2, 4, 6, 16, 18)
#
# closest should return [[2, 4, 2000], [4, 0, 103]] (or ([2, 4, 2000], [4, 0, 103])
# or [{2, 4, 2000}, {4, 0, 103}] or ... depending on the language)
# because 2000 and 103 have for weight 2 and 4, ther indexes in strng are 4 and 0.
# The smallest difference is 2.
# 4 (for 103) and 6 (for 123) have a difference of 2 too but they are not
# the smallest ones with a difference of 2 between their weights.
# ....................
#
# strng = "80 71 62 53"
# All the weights are 8.
# closest should return [[8, 0, 80], [8, 1, 71]]
# 71 and 62 have also:
# - the smallest weights (which is 8 for all)
# - the smallest difference of weights (which is 0 for all pairs)
# - but not the smallest indices in strng.
# ....................
#
# strng = "444 2000 445 544"
# the weights are 12, 2, 13, 13 (ie 2, 12, 13, 13)
#
# closest should return [[13, 2, 445], [13, 3, 544]] or ([13, 2, 445], [13, 3, 544])
# or [{13, 2, 445}, {13, 3, 544}] or ...
# 444 and 2000 have the smallest weights (12 and 2) but not the smallest difference of weights;
# they are not the closest.
# Here the smallest difference is 0 and in the result the indexes are in ascending order.
# ...................
#
# closest("444 2000 445 644 2001 1002") --> [[3, 4, 2001], [3, 5, 1002]] or ([3, 4, 2001],
# [3, 5, 1002]]) or [{3, 4, 2001}, {3, 5, 1002}] or ...
# Here the smallest difference is 0 and in the result the indexes are in ascending order.
# ...................
#
# closest("239382 162 254765 182 485944 468751 49780 108 54")
# The weights are: 27, 9, 29, 11, 34, 31, 28, 9, 9.
# closest should return  [[9, 1, 162], [9, 7, 108]] or ([9, 1, 162], [9, 7, 108])
# or [{9, 1, 162}, {9, 7, 108}] or ...
# 108 and 54 have the smallest difference of weights too, they also have
# the smallest weights but they don't have the smallest ranks in the original string.
# ..................
#
# closest("54 239382 162 254765 182 485944 468751 49780 108")
# closest should return  [[9, 0, 54], [9, 2, 162]] or ([9, 0, 54], [9, 2, 162])
# or [{9, 0, 54}, {9, 2, 162}] or ...
# Notes :
# If n == 0, `closest("") should return [] or ([], []) in Haskell, Clojure, FSharp or [{}, {}]
# in Elixir or {{0,0,0},{0,0,0}} in C++, "{{0,0,0},{0,0,0}}" in C, NULL in R.
# See Example tests for the format of the results in your language.

def closest(strng):
    #print("Input:", strng)
    all_weight = []
    splitted = [num for num in strng.split(" ") if num]
    if strng == "":
        return []
    for i, number in enumerate(splitted):
        my_sum = 0
        for chr in number:
            my_sum += int(chr)
        all_weight.append([my_sum, i, int(number)])
    all_weight.sort()
    all_diff = []
    for i in range(len(all_weight) - 1):
        difference = all_weight[i+1][0] - all_weight[i][0]
        all_diff.append([difference, all_weight[i], all_weight[i+1]])
    # # Help Debug: Find Weight
    # print("\nWeight \tIndex \tNumber")
    # for t in all_weight:
    #     print("{} \t{} \t{}".format(t[0],t[1],t[2]))
    # # Help Debug: Find Differences:
    # print("\nDiff \tWeight \tIndex \tNumber")
    # for t in all_diff:
    #     print("{} \t{} \t{} \t{}".format(t[0],t[1][0],t[1][1], t[1][2]))
    return [min(all_diff)[1], min(all_diff)[2]]



def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe("closest")
Test.it("Basic tests")
testing(closest(""), [])
testing(closest("456899 50 11992 176 272293 163 389128 96 290193 85 52"), [[13, 9, 85], [14, 3, 176]])
testing(closest("239382 162 254765 182 485944 134 468751 62 49780 108 54"), [[8, 5, 134], [8, 7, 62]])
testing(closest("241259 154 155206 194 180502 147 300751 200 406683 37 57"), [[10, 1, 154], [10, 9, 37]])
testing(closest("89998 187 126159 175 338292 89 39962 145 394230 167 1"), [[13, 3, 175], [14, 9, 167]])
testing(closest("462835 148 467467 128 183193 139 220167 116 263183 41 52"), [[13, 1, 148], [13, 5, 139]])

testing(closest("403749 18 278325 97 304194 119 58359 165 144403 128 38"), [[11, 5, 119], [11, 9, 128]])
testing(closest("28706 196 419018 130 49183 124 421208 174 404307 60 24"), [[6, 9, 60], [6, 10, 24]])
testing(closest("189437 110 263080 175 55764 13 257647 53 486111 27 66"), [[8, 7, 53], [9, 9, 27]])
testing(closest("79257 160 44641 146 386224 147 313622 117 259947 155 58"), [[11, 3, 146], [11, 9, 155]])
testing(closest("315411 165 53195 87 318638 107 416122 121 375312 193 59"), [[15, 0, 315411], [15, 3, 87]])

### Bruxarias:
def closest(s):
    wght = sorted([ [sum(int(c) for c in n), i, int(n)] for i, n in enumerate(s.split()) ], key=lambda k: (k[0], k[1]))
    diff = [ abs(a[0] - b[0]) for a, b in zip(wght, wght[1:]) ]
    return  [ wght [diff.index(min(diff)) ], wght [diff.index(min(diff)) + 1] ] if wght else []

######################################

comment("Give The Biggest Prime Factor And The Biggest Divisor Of A Number")
# https://www.codewars.com/kata/give-the-biggest-prime-factor-and-the-biggest-divisor-of-a-number/train/python
#
# Given a certain integer n, we need a function big_primefac_div(),
# that give an array with the highest prime factor and the highest divisor (not equal to n).
#
# Let's see some cases:
#
# big_primefac_div(100) == [5, 50]
# big_primefac_div(1969) == [179, 179]
# If n is a prime number the function will output an empty list:
#
# big_primefac_div(997) == []
# If n is an negative integer number, it should be considered the division with tha absolute number of the value.
#
# big_primefac_div(-1800) == [5, 900]
# If n is a float type, will be rejected if it has a decimal part with some digits different than 0.
#  The output "The number has a decimal part. No Results".
# But n will be converted automatically to an integer if all the digits of the decimal part are 0.
#
# big_primefac_div(-1800.00) == [5, 900]
# big_primefac_div(-1800.1) == "The number has a decimal part. No Results"
# Optimization and fast algorithms are a key factor to solve this kata. Happy coding and enjoy it!


def big_primefac_div(n)
    # your code here
    return [biggest_primefactor, biggest_divisor]



test.describe("Example Tests")
test.assert_equals(big_primefac_div(100), [5, 50])
test.assert_equals(big_primefac_div(1969), [179, 179])
test.assert_equals(big_primefac_div(997), [])
test.assert_equals(big_primefac_div(-1800), [5, 900])
test.assert_equals(big_primefac_div(-1800.00), [5, 900])
test.assert_equals(big_primefac_div(-1800.1), "The number has a decimal part. No Results")



# https://www.codewars.com/kata/tracking-hits-for-different-sum-values-for-different-kinds-of-dice


comment("Find All the Possible Numbers Multiple of 3 with the Digits of a Positive Integer. ")
# https://www.codewars.com/kata/find-all-the-possible-numbers-multiple-of-3-with-the-digits-of-a-positive-integer/train/python
from itertools import permutations, combinations

def find_mult_3(number):
    number = list(str(number))
    candidates, output = [], []
    # Find all combinations mult. of 3.
    for i in range(1, len(number) + 1):
        candidates.append(["".join(a) for a in combinations(number, i)
                           if int("".join(list(a))) % 3 == 0 and int("".join(list(a))) != 0])
    # Remove subitems [[], [[],[],[],[]],[]] -> Flatten:
    candidates = [item for sublist in candidates for item in sublist]
    # Now permute those numbers to get all numbers.
    for candidate in candidates:
        c = str(candidate)
        output.append(["".join(list(a)) for a in permutations(c, len(c))])
    # Flatten list:
    output = [int(item) for sublist in output for item in sublist]
    # Remove Duplicates:
    output = list(set(output))
    return [len(output), max(output)]

test.describe("Basic Test")

test.assert_equals(find_mult_3(362), [4, 63])
test.assert_equals(find_mult_3(6063), [25, 6630])
test.assert_equals(find_mult_3(7766553322), [55510, 766553322])


#########################################


