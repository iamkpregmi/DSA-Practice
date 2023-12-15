#Binary Search Using Python
#Time Complexity    O(log n)
#Space Complexity   O(1)

def binary_Search(inputlist,key):
    start = 0
    end = len(inputlist)
    
    while start < end:
        mid = start + (end - start)//2  # Or mid = (start+end)//2
        if key == inputlist[mid]:
            return mid
        elif key > inputlist[mid]:
            start = mid + 1
        else:
            end = mid -1

    return -1

key = 30
mylist = [12,15,18,20,26,30]
print(binary_Search(mylist,key))