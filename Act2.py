#Binary Search
ar=[1,2,3,4,5,6,7]
print(ar)
Key=int(input("Pick a number  "))
start=0
end = len(ar)-1
found=False

while start<=end:
    mid=(start+end)//2
    if ar[mid] == Key:
        found=True
        print("Number Found")
        break
    elif ar[mid] < Key:
        start=mid+1
    else:
        end=mid-1

if found==False:
    print("Number Not Found")

    