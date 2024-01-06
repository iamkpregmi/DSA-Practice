#Q1 Write a python program for remove duplicate value from list

def remove_duplicate(inputlist):
    result = []
    for item in inputlist:
        if item not in result:
            result.append(item)
    return result

orginal_list = [12,15,16,12,18,16,12,20]
unique_values = remove_duplicate(orginal_list)
print(unique_values) # Output: [12, 15, 16, 18, 20]

#----------------------------------------------------------------------------------------------------------------------------------
#Q2 Check given number is prime or not

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

print(is_prime(11)) #Output: True

#----------------------------------------------------------------------------------------------------------------------------------
#Q3 Calculate HCF(GCD) using Eucliden Algorithm.
'''
HCF: Highest Common Factor
GCD: Greatest Common Divisor
'''

def calculate_hcf(a,b):
    while b!=0:
        a,b = b, a%b
    return a

print(calculate_hcf(8,15)) #Output: 1

#----------------------------------------------------------------------------------------------------------------------------------
#Q4 Calculate LCM(Lowest Common Multiple) using Euclidean Algorithm
# Formula: LCM(a,b) = (a*b)/GCD(a,b)

def calculate_lcm(a,b):
    return (a*b)//calculate_hcf(a,b)

print(calculate_lcm(12,15)) #Output: 60

#----------------------------------------------------------------------------------------------------------------------------------
#Q5 Count length of the list without using inbuild method

def find_length(number):
    count = 0
    for i in number:
        count += 1
    return count

my_list = [12,15,16,12,18,16,12,20]
print(find_length(my_list)) #Output: 8

#----------------------------------------------------------------------------------------------------------------------------------
#Q6 Write a python program for calulate factorial of n number
'''
Using recursive way
Time Complexity: O(1)
Space Complexity: O(n)
'''
def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
    
print(factorial(5)) #Output: 120

'''
Using recursive Simple way (Best Way to implement)
Time Complexity: O(1)
Space Complexity: O(1)
'''
n = 6
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(fact) #Output: 720

#----------------------------------------------------------------------------------------------------------------------------------
#Q7 Write python program for check given number are odd or even
'''
Even number: 0,2,4,6,8
Odd number: 1,3,5,7,9
'''

def odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(odd_even(6)) #Output: Even


#Using bitwise Operator (Best Way Run fast)
def odd_even1(number):
    if number & 1:
        return "Odd"
    else:
        return "Even"
    
print(odd_even1(7)) #Output: Odd

#----------------------------------------------------------------------------------------------------------------------------------
#Q8 Write a python program for reverse an number

def reverse_number(num):
    sum = 0
    while num > 0:
        remd = num % 10
        sum = (sum * 10) + remd
        num = num // 10
    return sum

print(reverse_number(347)) #Output: 743

#----------------------------------------------------------------------------------------------------------------------------------
#Q9 Write a python program for remove special charactor from string

def remove_special_char(input_list):
    special_chars = "!@#$%^&*()_+1234567890-="
    clean_text = ""
    for char in input_list:
        if char not in special_chars:
            clean_text += char
    return clean_text

my_list = "@2Krishna21"
print(remove_special_char(my_list)) #Output: Krishna

#----------------------------------------------------------------------------------------------------------------------------------
#10 Write a python program for Reverse string

def reverse_string(user_input):
    result = ""
    for char in user_input:
        result = char + result
    return result

name = "Krishna"
print(reverse_string(name)) #Output: anhsirK

#----------------------------------------------------------------------------------------------------------------------------------
#10 Write a python program for Reverse for Reverse a list

def reverse_list(mylist):
    start_index = 0
    end_index = len(mylist)-1

    while start_index < end_index:
        mylist[start_index],mylist[end_index] = mylist[end_index],mylist[start_index]
        start_index += 1
        end_index -= 1

    return mylist

my_list = [12,15,16,1,7]
print(reverse_list(my_list)) #Output: [7, 1, 16, 15, 12]

#----------------------------------------------------------------------------------------------------------------------------------
#Q11 Here's a Python program that prints prime numbers from 1 to 7 (excluding 7 as the last one):
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

for num in range(1, 7):  # Iterate from 1 to 6 (excluding 7)
    if is_prime(num):
        print(num)

#----------------------------------------------------------------------------------------------------------------------------------
# Write a pythn program for fundout occquerance of word in a list

def count_occurrences(words_list):
    word_count = {}
    for word in words_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

mylist = ["krishna", "kushal", "Brijesh", "Brijesh", "Krishna", "Brijesh"]
word_occurrences = count_occurrences(mylist)

print("Occurrences of each word:")
for word, count in word_occurrences.items():
    print(f"'{word}': {count} times")

# ----------------------------------------------------------------------------------
from collections import Counter

mylist = ["krishna", "kushal", "Brijesh", "Brijesh", "Krishna", "Brijesh"]
word_occurrences = Counter(mylist)

print("Occurrences of each word:")
for word, count in word_occurrences.items():
    print(f"'{word}': {count} times")

# ----------------------------------------------------------------------------------
def count_occurrences(words_str):
    words_list = words_str.split()  # Split the string into a list of words
    word_count = {}
    for word in words_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

input_string = "krishna kushal Brijesh Brijesh Krishna Brijesh"
word_occurrences = count_occurrences(input_string)

print("Occurrences of each word:")
for word, count in word_occurrences.items():
    print(f"'{word}': {count} times")

# ----------------------------------------------------------------------------------


