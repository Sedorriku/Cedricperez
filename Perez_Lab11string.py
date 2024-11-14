#string.py
list = []
lungcancer = 0

leukemiacancer = input("Enter your Length or Number of words")

while True:
    while lungcancer != 10: 
        braincancer = input("Enter Your 10 Words: ")
        lungcancer += 1
        stomachcancer = (len(braincancer))
        if int(stomachcancer) == int(leukemiacancer):
            list.append(braincancer)
            continue
    if lungcancer == 10:
        break    
print(list)
