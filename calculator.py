import math


def add(x, y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x , y):
    return x / y
def power(x,y):
    return x ** y
square_root = math.sqrt


print("Select Operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Square Root")
print("7.All Of Above")

while True:
    choice = input("enter choice(1/2/3/4/5/6/7)  ")
    if choice in ('1','2','3','4','5'):
        num1 = float(input("enter your first number"))
        num2 = float(input("enter your second number"))
        if choice =='1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice == '2':
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif choice == '3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice == '4':
            print(num1,"/",num2,"=",divide(num1, num2))
        elif choice == '5':
            print(num1,"^",num2,"=",power(num1, num2))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    elif choice in ('6'):
        num1 = float(input("enter your number"))
        if choice =='6':
            print("^/",num1,"=",square_root(num1))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    elif choice in ('7'):
        num1 = float(input("enter your first number"))
        num2 = float(input("enter your second number"))
        if choice == '7':

            print(num1, "+", num2, "=", add(num1, num2))
            print(num1,"-",num2,"=",subtract(num1,num2))
            print(num1,"*",num2,"=",multiply(num1,num2))
            print(num1,"/",num2,"=",divide(num1, num2))
            print(num1,"^",num2,"=",power(num1, num2))
            print("^/",num1,"=",square_root(num1))
            print("^/",num2,"=",square_root(num2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break




    else:
             print("invailed input")

