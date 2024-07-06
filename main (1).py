def bmi():
    a=float(input("Enter you weight"))
    b=float(input("Enter you height"))
    c=a/(b**2)
    if c<18.5:
        print("Underweight")
    if 18.5<=c<24.9:
        print("Normalweight")
    if 25<=c<29.9:
        print("Overweight")
    if 30<=c:
        print("Obeisity")
bmi()    

