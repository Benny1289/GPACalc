Run=True
while Run==True:
    classlist = []  
    n = int(input("Enter number of classes this semster(Exclude GYM):")) 
    print("Please enter grade value for your classes one at a time. \n Press enter when finished with a class(Exclude GYM). \n If the class is a honors/AP class, add .5 to value \n EX: Taking APCSP and have a B, type 3.5. \n EX: Taking Chinese IV and have a C type 2  \n Values: \n A=4 \n B=3 \n C=2 \n D-F=1") 

    for i in range(0, n): 
            ele = float(input()) 
            classlist.append(ele)

    print("What is your current cumulative GPA?")
    cumulative=float(input())
    print("How many semsters have you had in your highschool carrer(exclude current)?")
    sems=int(input())
    print("WIth your current grades, your cumulative would be:")
    print(((cumulative*sems)+(sum(classlist)/n))/(sems+1))
    print("Rerun program?(Y/N)")
    Rerun=input()
    if Rerun=="Y":
        Run=True
    elif Rerun=="N":
        exit()
    
