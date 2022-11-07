# 3) Write a program to find the second largest number in an array. [2.5 marks]

l1 = [10,20,30,40,50,60,55,34,22,101,20,10]
# Remove any duplicates from list
l2 = list(set(l1))
# sort the list
l2.sort()

print("second largest element is:", l2[-2])