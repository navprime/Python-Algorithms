import random
lst = [random.randint(0,200) for i in range(100)]
print("Unsorted list=",lst)
for i in range(len(lst)-1):
    for j in range(i,len(lst)-1):
        if lst[j] > lst[j+1]:
            temp = lst[j]
            lst[j],lst[j+1] = lst[j+1],temp
            
print("Sorted lst=",lst)