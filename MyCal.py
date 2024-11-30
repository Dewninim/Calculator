#Simple Calculator
import math

def Add (x,y):
    return x+y

def Subtract(x,y):
    return x-y

def Multiply (x,y):
    return x*y

def Devide (x,y):
    if y==0:
        return "Error!! Devision by 0"
    else:
        return x/y

def Power (x,y):
    return x**y

def sqrt (x):
    if x<0:
        return "Error! Square root of negative number"
    else :
        return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    if (x % 180 == 90):
        return "Error! Tangent undifined at 90 degrees."
    else:
        return math.tan(math.radians(x))


def calculator():
    print ("Welcome")
    print ("Operations: + , - , * , / , sqrt , sin , cos , tan")

    while True:
        choice = input ("\nEnter operation (or 'exit' to quit): ").strip()

        if choice == 'exit':
            print("Goodbye")
            break

        if choice in ('+', '-', '*', '/'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '+':
                print(f"Result: {Add(num1,num2)}")
            elif choice == '-':
                print(f"Result: {Subtract(num1,num2)}")
            elif choice == '*':
                print(f"Result: {Multiply(num1,num2)}")
            elif choice == '/':
                print(f"Result: {Devide(num1,num2)}")

        elif choice == 'pow':
            num1 = float(input("Enter base: "))
            num2 = float(input("Enter exponent: "))
            print(f"Result: {Power(num1,num2)}")

        elif choice == 'sqrt':
            num = float(input("Enter number: "))
            print(f"Result: {sqrt(num)}")

        elif choice == 'sin':
            angle = float(input("Enter angle in degrees: "))
            print(f"Result: {sin(angle)}")

        elif choice == 'cos':
            angle = float(input("Enter angle in degrees: "))
            print(f"Result: {cos(angle)}")

        elif choice == 'tan':
            angle = float(input("Enter angle in degrees: "))
            print(f"Result: {tan(angle)}")

        else:
            print("Invalid operation! Please try again.")

if __name__ == "__main__":
    calculator()

        
                    
            
