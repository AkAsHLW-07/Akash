def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
    
def calculator():
    a=float(input("Enetr a first  number"))
    b=float(input("Enetr a second number"))
    print("Select operation")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    choice=input("Enter your choice:")
    if choice=="1":
        print(f"The result is{add(a,b)}")
    elif choice=="2":
        print(f"The result is{subtract(a,b)}")
    elif choice=="3":
        print(f"The result is{multiply(a,b)}")
    elif choice=="4":
        print(f"The result is{divide(a,b)}")
    else:
        print("invalid")
        
        
calculator()        
