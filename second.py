#Python Calculator v2

def calculate(a, opr, b):
    
    if opr == "+":
        result = a + b
    
    elif opr == "-":
        result = a - b 
    
    elif opr == "*":
        result = a * b 
    
    elif opr == "/":
        if b == 0:
            result = "Math Error! Can't Divide by Zero."
        else:
            result = a / b

    else:
        result = "Insert an operator first!"
    
    return result

try:

    a = float(input("Insert the first number: "))
    opr = input("Insert the operator (+,-,*,/): ")
    b = float(input("Insert the second number: "))

    print(f"Result = {calculate(a, opr, b)}")

except ValueError: print("Invalid Number Input!")
