#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. Note : Use 'continue' statement.
for i in range(7):
    if i==3 or i==6:
        continue
    print(i)

# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note:
# i = 0,1.., m-1 
# j = 0,1, n-1.
# Hint: Use input(), list comprehension, loops, range()
# Test Data : Rows = 3, Columns = 4 
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

m = int(input("Enter the m  : "))
n = int(input("Enter the n  : "))
arr = [[i * j for j in range(n)]for i in range(m)]
print(arr)

# Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
# Hints:
# Use filter() to filter some elements in a list.
# Use lambda to define anonymous functions.

l = [1,2,3,4,5,6,7,8,9,10]
l1 = list(filter(lambda x : x%2==0,l))
print(l1)

# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.
l2 = [1,2,3,4,5,6,7,8,9,10]
l3 = list(map(lambda x : x**2,l2))
print(l3)


# Write a python function using *args parameters to print name and age from list of students.
# Test data: [{“name”: “abhi”, “age”: 22}, {“name”: “vikas”, “age”: 21}]
#         Expected result: 
#         name abhi
#                age 22
#                name vikas
#                age 

def fun(*args):
    for i in args:
        print('name '+ i['name'])
        print('age '+str(i['age']))

fun({'name': 'abhi', 'age': 22},{'name': 'vikas', 'age': 21})


