Marks = {}
print("Enter Your Marks : ")
Marks["Physics"] = int(input("Physics : "))
Marks["Chemistry"] = int(input("Chemistry : "))
Marks["Maths"] = int(input("Maths : "))
Marks["English"] = int(input("English : "))
Marks["Computer"] = int(input("Computer : "))

#Total
Total = Marks["Physics"] + Marks["Chemistry"] + Marks["Maths"] + Marks["English"] + Marks["Computer"]

print(f"Total Score = {Total}/500")

Percentage = ((Total)/500)*100
print(f"Percentage Scored : {Percentage} %")

if(Percentage > 33):
    
    if(Marks["Physics"]>33 and Marks["Chemistry"]>33 and Marks["Maths"]>33 and Marks["English"]>33 and Marks["Computer"]>33):
        print("Congrats !")
        print("Result : Passed")
    else:
        print("You have not cleared subject cutoff")
        print("Result : Failed")
        
    
else:
    print("Result : Failed")

if(Percentage > 90):
    print("Grade : A")
elif(Percentage > 80):
    print("Grade : B")
elif(Percentage > 70):
    print("Grade : C")
elif(Percentage > 60):
    print("Grade : D")
elif(Percentage > 40):
    print("Grade : E")
else:
    print("Grade : F")
    
