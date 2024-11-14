#gardes.py
grade = []

while True:
    entry = input("Enter Student Grades or type exit to end: ")
    
    if entry.lower() == 'exit':
        if grade:
            break
        else:
            print("No Grades Entered")
            exit()
            
    if entry.isdigit():
        gradess = int(entry)
        if 40 <= gradess <= 100:
            grade.append(gradess)
            x =+ 1
        else:
            print("Sorry Invalid Number. Put A Valid Number Between 40-100")
            exit ()
    else:
          print("Sorry Invalid Number")
          exit()
if grade:          
    average = sum(grade) /len(grade)
    passedgrade = (len(grade)/ len(grade)) * 100
    #resultssss      
    print(f"\nYour Average Grade is {average:.2f} %")
    print(f"Passed Subjects: {passedgrade:.2f} %")
    print(f"The Students who have passed: {len(grade)} ")
    print(f"Grades: {grade}\n")
else:
    print("Invalid Grades Input")