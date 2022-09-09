# binarySearch.py
# Alise Braick
# CSCI 77800 Fall 2022
# collaborators: 
# consulted:

def binarySearch( list, target):
    
    # lowIndex, highIndex, and midIndex
    low = 0
    high = len(list) -1
    
    
    while low <= high:
        # the // instead of /  because we need an integer output
        mid = (low + high)//2
        print(low, high, mid)
        
        # will use if/elif, so the comoputer does need to go through all of conditions once any of these conditoons is true
        if target == list[mid]:
            return mid
        
        elif target < list[mid]:
            high = mid -1
            
        elif target > list[mid]:
            low = mid + 1
            
    # In case target not found       
    return -1

# test the list and target 
list =[4, 8, 15, 20, 26, 30,31 , 40, 55, 100]
target = 55
print ("our target is", target, "in this", list)

# call BinarySearch function
indexTarget = binarySearch (list, target)
print ( target, " is at index" , indexTarget)
        
    