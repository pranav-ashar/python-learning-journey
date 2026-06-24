#Word Counter
print("ENTER A STATEMENT : ")
Input_Statement = input()
Spaces = Input_Statement.count(" ")
Vowels = Input_Statement.count("a") + Input_Statement.count("e") + Input_Statement.count("i") + Input_Statement.count("o") + Input_Statement.count("u")
Letters = len(Input_Statement) - Spaces
words = Input_Statement.split()
words_count = len(words)
print("The Statement contains :")
print(f"Spaces : {Spaces}")
print(f"Vowels : {Vowels}")
print(f"Letters : {Letters}")
print(f"Total Words : {words_count}")