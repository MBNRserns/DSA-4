#Linear Search
ar=[1,2,3,4,5,6,7,8,9,10]
print(ar)
numQ=int(input("Choose a number   "))
found=False
for i in ar:
    if numQ == i:
        print("Number Available")
        found=True
        break
if found==False:
    print("Number Not Available")
print(len(ar))

print(ar[0])
print(ar[4])