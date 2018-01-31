# Here we will define our function

# this prints the main menu and prompts for a choice

def menu ():
    print ("welecome to my calculator!!!")
    print ("Your options are :-")
    print ("")
    print ("1) Addition","\n2) Subtraction","\n3) Division","\n4) Multiplication","\n5) Quit Calculator")
    print ("")
    return int(input("choose your option: "))


# this add two number given
def add(a,b):
    print (a, "+" ,b, "=", a+b)


# this substract two number given
def sub(a,b):
    print (b, "-", a,"=", b-a)


# this mutilply two number given
def mul(a,b):
    print (a, "*", b, "=", a*b)


# this divides two number given

def div(a,b):
    print (a, "/", b, "=", a/b)

#code start from here

loop = 1

choice = 0

while loop == 1:
    choice = menu()
    if choice == 1:
        add(float(input("add this: ")), float(input("to this: ")))
    elif choice == 2:
        sub(float(input("subtract this: ")), float(input("from this: ")))
    elif choice == 3:
        mul(float(input("multiply this: ")), float(input("by this: ")))
    elif choice == 4:
        div(float(input("divide this: ")), float(input("by this:")))
    elif choice == 5:
        loop = 0


print ("Thank you for using my calculator")

# programme finished
