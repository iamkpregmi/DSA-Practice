# Write a python code for short value according to value
mydict = {'A': 30, 'B': 10, 'C': 7}
sorted_values = sorted(mydict.values())
print(sorted_values)
# print(type(sorted_values)) #list


# Write a python program to find index of first acquaintance and last acquaintance of given number
def myAcq(key):
    mylist = [3,12,17,20,3,12,11,2,3,0,1]
    c = []
    for i in range(len(mylist)):
        if key == mylist[i]:
            c.append(i)

    print("First acquaintance",c[0])
    print("Last acquaintance",c[-1])

myAcq(3)


# Write a python program for find logic

def myfunction(fromUnit, toUnit, n):
    mydict = {
        'kmh':{'m':100, 'mm':1000, 'mmm':10000},
        'vlt': {'v1':50, 'v2':100, 'v3':500 },
        'kpr':{'k1':50, 'k2': 100, 'k3':150, 'k4': 200}
    }

    mykey = mydict[fromUnit][toUnit]
    return mykey * n

print(myfunction('vlt','v2',5))


# Anoter method with error handling
def myfunction(fromUnit, toUnit, n):
    mydict = {
        'kmh': {'m': 100, 'mm': 1000, 'mmm': 10000},
        'vlt': {'v1': 50, 'v2': 100, 'v3': 500}
    }

    if fromUnit in mydict and toUnit in mydict[fromUnit]:
        return mydict[fromUnit][toUnit] * n
    else:
        return "Invalid units provided"

result = myfunction('kmh', 'm', 5)
print(result)


