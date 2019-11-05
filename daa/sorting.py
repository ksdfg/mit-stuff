l = list(map(float, input("Enter numbers : ").split()))

if input("bubble or selection? ") == 'bubble':
    print("Bubble sort :")
    for _ in range(len(l)):
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
else:
    print("Selection sort :")
    for i in range(len(l)):
        index = l.index(min(l[i:]))
        l[i], l[index] = l[index], l[i]

print(*l)
