# creating an empty list
lst = []
 
# number of elements as input
n = int(input("\n\n\n\n\nEnter number of elements : "))
count = 0
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    lst.append(ele) # adding the element
     
print(lst)

k = int(input("enter a k value : "))
print(k)
for num in lst:
    diff = k-num
    if diff in lst:
        print(num,diff)
        lst.pop(count)
        count+=1
print(lst)