password = input("Enter a Password : ")
pass_stregth = 0
#Length Check
if(len(password)<8):
    pass_stregth = pass_stregth + 0
    print("Length \u2717 ")
else:
    pass_stregth = pass_stregth + 1
    print("Length \u2713 ")

#Uppercase Check 
uppercase_count = sum(1 for char in password if char.isupper())

if(uppercase_count >= 1):
    pass_stregth = pass_stregth + 1
    print("Uppercase \u2713 ")
else:
    pass_stregth = pass_stregth + 0
    print("Uppercase \u2717 ")

#Lowercase Check
lowercase_count = sum(1 for char in password if char.islower())

if(lowercase_count>=1):
    pass_stregth = pass_stregth + 1
    print("Lowercase \u2713 ")
else:
    pass_stregth = pass_stregth + 0
    print("Lowercase \u2717 ")

#Digitcheck
num_count = sum(1 for char in password if char.isnumeric())

if(num_count >= 1):
    pass_stregth = pass_stregth + 1
    print("Number \u2713 ")
else:
    pass_stregth = pass_stregth + 0
    print("Number \u2717 ")

#Special Character Check
specialchar_check = len(password) - lowercase_count - uppercase_count -num_count - password.count(" ")

if(specialchar_check >=1):
    pass_stregth = pass_stregth + 1
    print("Special Characters \u2713 ")
else:
    pass_stregth = pass_stregth + 0
    print("Special Characters \u2717 ")
    
print(f"Password Strength Rating : {pass_stregth}")
if(pass_stregth == 0):
    print("Rating : Very Poor")
elif(pass_stregth == 1):
    print("Rating : Poor")
elif(pass_stregth == 2):
    print("Rating : Weak")
elif(pass_stregth == 3):
    print("Rating : Medium")
elif(pass_stregth == 4):
    print("Rating : Strong")
elif(pass_stregth == 5):
    print("Rating : Very Strong")