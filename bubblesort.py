# 5) Write a program or algorithm to implement bubble sort. [5 marks]


def bubblesort(elements):
    swapped = False
    
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i+1]:
                swapped = True
                elements[i], elements[i+1] = elements[i+1], elements[i]
        if not swapped:
            return
elements = [20, 60, 43, 56 , 21, 89,2]
        
print("Unsorted list is,")
print(elements)
bubblesort(elements)
print("Sorted Array is,")
print(elements)