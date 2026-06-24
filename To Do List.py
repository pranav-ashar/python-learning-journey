List = []
print("Enter Your Tasks ")
List.append(input())
Boolean = True

while Boolean == True:
    userinput = str(input())
    if not userinput:
        Boolean = False 
    else:
        List.append(userinput)
        Boolean = True 
i = 0

print("TO - DO List !")
while(i < len(List)):
    print(f"{i+1}) {List[i]}")
    i = i + 1
    
print("")
print("What Would You Like to do ?")
print("Count Number of Tasks : Num")
print("Add Tasks : Add")
print("Remove Task : Remove")
print("Mark Task : Mark")
Boolean = True
UserInputData = str(input("User Input : "))
if UserInputData.startswith("Add"):
    while Boolean == True:
        userinput = str(input())
        if not userinput:
            Boolean = False 
        else:
            List.append(userinput)
            Boolean = True
     
elif UserInputData.startswith("Num"):
    print(f"Total Number of Tasks : {len(List)}")

elif UserInputData.startswith("Remove"):
    print("Removing")
elif UserInputData.startswith("Mark"):
    print("Mark")

print("Welcome You are out of the Loop")
print("TO - DO List !")

i = 0
while(i < len(List)):
    print(f"{i+1}) {List[i]}")
    i = i + 1
