# Python Assignment 1

## Question 1

### Question
Write a program which will find all such numbers which are divisible by 7
but are not multiple of 5, between 2000 and 3200.

### Solution
```python
print(*[x for x in range(2000, 3201) if x % 7 == 0 and x % 5 != 0])
```

### Output
```
2002 2009 2016 2023 2037 2044 2051 2058 2072 2079 2086 2093 2107 2114 2121 2128 2142 2149 2156 2163 2177 2184 2191 2198 2212 2219 2226 2233 2247 2254 2261 2268 2282 2289 2296 2303 2317 2324 2331 2338 2352 2359 2366 2373 2387 2394 2401 2408 2422 2429 2436 2443 2457 2464 2471 2478 2492 2499 2506 2513 2527 2534 2541 2548 2562 2569 2576 2583 2597 2604 2611 2618 2632 2639 2646 2653 2667 2674 2681 2688 2702 2709 2716 2723 2737 2744 2751 2758 2772 2779 2786 2793 2807 2814 2821 2828 2842 2849 2856 2863 2877 2884 2891 2898 2912 2919 2926 2933 2947 2954 2961 2968 2982 2989 2996 3003 3017 3024 3031 3038 3052 3059 3066 3073 3087 3094 3101 3108 3122 3129 3136 3143 3157 3164 3171 3178 3192 3199
```

## Question 2

### Question
Write a program which can compute the factorial of a given numbers.

### Solution
```python
num = int(input("Enter a number : "))
fact = 1
for i in range(num, 0, -1):
    fact = fact * i
print("Factorial =", fact)
```

### Output
```
Enter a number : 5
Factorial = 120
```

## Question 3

### Question
Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 

Note : Use 'continue' statement.

### Solution
```python
for i in range(0, 7):
    if i == 3 or i == 6:
        continue
    print(i)
```

### Output
```
0
1
2
4
5
```

## Question 4

### Question
Write a program that accepts a string and calculates number of letters and
digit.

### Solution
```python
phrase = input("Enter phrase : ")
l = d = 0
for c in phrase:
    if c in ascii_letters:
        l += 1
    elif c in digits:
        d += 1
print("Number of letters =", l)
print("Number of digits =", d)
```

### Output
```
Enter phrase : hello 123
Number of letters = 5
Number of digits = 3
```

