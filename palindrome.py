def palindrome(s):
    s = str(s)
    rev = s[::-1]
    if s == rev:
        return True
    else:
        return False



print("Dec\t\tBin")

for i in range(100000):
    if palindrome(i) and palindrome(bin(i)[2:]):
        print("{:5} \t {} são palindromos".format(i, str(bin(i)[2:])))
