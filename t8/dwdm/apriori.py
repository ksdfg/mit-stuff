from collections import defaultdict

dataset = [[1, 2, 5], [2, 4], [2, 3], [1, 2, 4], [1, 3], [2, 3], [1, 3], [1, 2, 3, 5], [1, 2, 3]]
minsupport = 2

print("for sets of 1")

c1 = defaultdict(lambda: 0)
for transaction in dataset:
    for item in transaction:
        c1[frozenset([item])] += 1
print(c1.items())

for key in c1.keys():
    if c1[key] < minsupport:
        c1.pop(key)
print(c1.items(), "\n")

print("for sets of 2")

c2 = defaultdict(lambda: 0)
c1keys = list(c1.keys())
for i in range(len(c1keys)):
    for j in range(i + 1, len(c1keys)):
        c2[c1keys[i].union(c1keys[j])] = 0

for transaction in dataset:
    for key in c2.keys():
        if key.issubset(transaction):
            c2[key] += 1

print(c2.items())

keys = list(c2.keys())
for key in keys:
    if c2[key] < minsupport:
        c2.pop(key)
print(c2.items(), "\n")

print("for sets of 3")

c3 = defaultdict(lambda: 0)
for transaction in dataset:
    for i in range(len(transaction)):
        for j in range(i + 1, len(transaction)):
            for k in range(j + 1, len(transaction)):
                c3[frozenset([transaction[i], transaction[j], transaction[k]])] += 1
print(c3.items())

keys = list(c3.keys())
for key in keys:
    if c3[key] < minsupport:
        c3.pop(key)
print(c3.items(), "\n")
