# Python Assignment 2

## Question 1

### Question
Write a program to demonstrate Python Packages
- Create a package with methods
    - Find the area of Square / Rectangle => rec_area( w,h)
    - Find the area of Circle => circle_area(r)
- Import the package and write the code which displays the menu.
    - Area of square / rectangle ( note that square is special case of
rectangle having width = height )
    - Area of Circle
- Accept the input and call appropriate method to calculate area and display the
result

### Solution
In `./area/__init__.py`
```python
from math import pi


def rec_area(w: int, h: int):
    return w * h


def circle_area(r: int):
    return pi * r * r
```
In `./assignment.py`
```python
from area import rec_area, circle_area

w = int(input("Enter width of rectangle : "))
h = int(input("Enter height of rectangle : "))
print("Area of rectangle is =", rec_area(w, h))

s = int(input("Enter side of square : "))
print("Area of square is =", rec_area(s, s))

r = int(input("Enter radius of circle : "))
print("Area of circle is =", circle_area(r))
```

### Output
```
from area import rec_area, circle_area

w = int(input("Enter width of rectangle : "))
h = int(input("Enter height of rectangle : "))
print("Area of rectangle is =", rec_area(w, h))

s = int(input("Enter side of square : "))
print("Area of square is =", rec_area(s, s))

r = int(input("Enter radius of circle : "))
print("Area of circle is =", circle_area(r))
```

## Question 2

### Question
Write a Python program to count the number of even and odd numbers from a
series of numbers.

### Solution
```python
sequence = input("Enter a sequence : ")
print("Number of even digits = ", len([c for c in sequence if c.isnumeric() and int(c) % 2 == 0]))
print("Number of odd digits = ", len([c for c in sequence if c.isnumeric() and int(c) % 2 != 0]))
```

### Output
```
Enter a sequence : 21234567890-
Number of even digits =  6
Number of odd digits =  5
```

## Question 3

### Question
Write a program that keeps student's name and his marks in a dictionary as key-
value pairs. The program should store records of 10 students and display students
name and marks of five students in decreasing order of marks obtained.

### Solution
```python
student_data = {}

for i in range(10):
    print(f'\nPlease enter details for student {i}')
    student_data[input('Enter name : ')] = float(input('Enter marks : '))

print('\nTop 5 students: ')
print('Name\tMarks')
sorted_data = sorted(student_data.items(), key=lambda item: item[1])
sorted_data.reverse()

for i in range(5):
    print(sorted_data[i][0] + '\t' + str(sorted_data[i][1]))
```

### Output
```

Please enter details for student 0
Enter marks : 10
Enter name : random a

Please enter details for student 1
Enter marks : 20
Enter name : random b

Please enter details for student 2
Enter marks : 30
Enter name : random c

Please enter details for student 3
Enter marks : 40
Enter name : random d

Please enter details for student 4
Enter marks : 50
Enter name : random e

Please enter details for student 5
Enter marks : 60
Enter name : random f

Please enter details for student 6
Enter marks : 70
Enter name : random g

Please enter details for student 7
Enter marks : 80
Enter name : random h

Please enter details for student 8
Enter marks : 90
Enter name : random i

Please enter details for student 9
Enter marks : 100
Enter name : random j

Top 5 students: 
Name	Marks
random j	100.0
random i	90.0
random h	80.0
random g	70.0
random f	60.0
```