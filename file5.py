# Write a generator function to create fibonacci series up to n number. Get input n from the user.

def fib(num_of_terms):
    num1  = 0
    num2  = 1

    while num_of_terms > 0:
        num3 = num1+num2
        yield num3
        num1 = num2
        num2 = num3
        num_of_terms -= 1

num = int(input(("Enter the number of terms upto which you want the fibonacci series : ")))

for i in fib(num):
    print(i,end='  ')



# Create a decorator do_twice which provides any function capability to execute it twice.

def do_twice(func_obj):
    print("This function executes the function object passed as a argument twice using decorators")

    def wrap_it():
        print("inside the wrapper function")
        func_obj()
        func_obj()

    return wrap_it


@do_twice
def fun_to_be_decorated():
    print("Run it")


fun_to_be_decorated()


# Create a sample.txt file with 10-15 lines of text. Find out the most common word in the file

import re
from collections import Counter

with open('file.txt','r') as file:
  passage = file.read()

words = re.findall(r'\w+',passage)
c_o_w = Counter([word for word in words])
c_o_w.most_common()[0]

'''
c_w = Counter(passage.split())
c_w.most_common()[0]
'''


# Have the program find prime numbers until the user chooses to stop asking for the next one.

def prime(ch):

    i = 2
    while ch =='y':
        flag = True

        for j in range(2,i):
            if i %j == 0:
                flag = False
                break
        if flag == True or i == 2:
            yield i

        i += 1

inp = 'y'
p = prime(inp)
while inp == 'y':
    print(next(p))
    inp = input('Do you want next prime y or n : ')


# Converts various units between one another. The user enters the type of unit being entered, the type of
# unit they want to convert to and then the value. The program will then make the conversion

def conver(unit1,unit2,num):
    unit_dic = {'m':1,'cm':0.01,'mm':0.001,'km': 1000}
    return f"{num} {unit1} =  {num * (unit_dic[unit1]/unit_dic[unit2]) } {unit2}"

print(" Use km m cm and mm for various length units")
unit1 = input("Enter the unit you want to use : ")
unit2 = input("Enter the unit you want to convert : ")

digit = float(input("Enter the value to convert : "))
print(conver(unit1,unit2,digit))

# A tool that allows the user to enter a text string and then in a separate control enter a regex pattern.
# It will run the regular expression against the source text and return any matches or flag errors in the regular expression.

import re
pattern = input("Enter the string in which you want to search custom pattern : ")
reg = input("Enter the regex pattern you want to search : ")

re.compile(reg)
search = re.findall(reg,pattern)
print("Searched patterns : ")
print(search)