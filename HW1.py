letters=["a","b","c","d","e","f","g","h"]
print(letters)
letQ=input("Choose a Letter:  ")
found = False
for i in letters:
    if letQ == i:
        print("Letter Available")
        found = True
        break
if found == False:
    print("Letter Not Available")
print(len(letters))