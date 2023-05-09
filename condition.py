# Write a Python program that takes a list of strings as input and outputs the number of times
#  each string appears in the list, using a dictionary and conditional statements.


# Write a Python program that takes a list of numbers as input and outputs the median of the numbers 
def median_nums(nums):
    nums.sort()
    length=len(nums)
    count=0
    if(length%2==0):
           middle=length/2
        return length

        print(median_nums([2,3,4,58,9]))       

# Write a Python program that takes a list of numbers as input and outputs the second largest
numbers=[5,6,7,3,8,9]
numbers.sort()
print(numbers[-2])

# Write a Python program that takes a year as input and determines if it is a leap year.
year = 2023
if(year %4 == 0) and (year %100 ==0):
    print(" is a leap year")
elif(year%4!=0)and(year %100!=0):
    print("is not a leap year")

# Write a Python program that takes a string as input and checks if it is a palindrome
#  (reads the same forwards and backwards), ignoring spaces and punctuation.
def palindrome(word):
    if word==word[::-1]:
        return True
    else:
        return False
print(palindrome("madam"))            
