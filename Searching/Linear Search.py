#Linear Search Using Python
#Time Complexity    O(n)
#Space Complexity   O(1)

def linear_Search(inputlist,key):
    for i in range(len(inputlist)):
        if key == inputlist[i]:
            return i
    return -1

key = 16
mylist = [12,15,18,17,16,10]
print(linear_Search(mylist,key))

