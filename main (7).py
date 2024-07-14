#AKASH
student={}


while True:
    name=input("If you are done with entering your name aand mark type done Enetr your name: ")
    if name=="done":
        break
    grade=float(input("enter your grade"))
    student[name]=grade
    
    
if student:
    avg=sum(student.values())/len(student.values())
    high=max(student.values())
    low=min(student.values())
    
    print(f"Average mark is:{avg}")
    print(f"Max mark:{high}")
    print(f"Lowest mark is:{low}")
    
    
    for name,grade in student.items():
        print(f"{name};{grade}")
        
else:
    print("No students data found")
    
        
