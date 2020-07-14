# playing with lists
var_list = list(i for i in range(10))
var_list2 = list(i for i in range(10, 20))
var_list3 = list(i for i in range(20, 30))
var_list4 = ['Kshitish', 'Manas', 'Aniket', 'Akhil', 'Reet']
var_list_combined = [var_list, var_list2, var_list3]  # list of all lists generated

print(var_list, var_list2, var_list3, var_list_combined, var_list4)

print(var_list[0])  # lists are subscriptable
var_list3.append(18)  # appending an object to the end of a list
print(var_list3)
var_list3.sort()  # sorting a list in ascending order
print(var_list3)
var_list2.sort(reverse=True)  # sorting a list in descending order
print(var_list2)
var_list_combined.sort(key=lambda x: x[0], reverse=True)  # you can even specify a key with which to compare
print(var_list_combined)
var_list3.sort(key=lambda x: x % 5)  # the key is basically a function applied to both elements before comparison
print(var_list3)
print(var_list + var_list2)  # adding two lists essentially concatenates them
print(len(var_list + var_list2))  # len() returns the number of elements in a list
var_list4.insert(1, 'Prayagraj')  # you can even insert an object at a specific index
print(var_list4)
print(var_list4 + var_list)  # lists need not be monotype - they can contain objects of multiple types
print(var_list.index(3))  # the index of function returns the index at which a certain object is present in the list
var_list4.sort()  # in case of a list of strings, objects are ordered by their ascii values
print(var_list4)

# playing with tuples
var_tuple = tuple(i for i in range(10))

print(var_tuple)
print(var_tuple.index(3))  # same as list
print(var_tuple.count(3))  # returns number of occurrences of an element in a tuple
# tuples are immutable while lists are mutable


# playing with sets
var_set = {'infosys', 'wipro', 'mann dairy'}
var_set2 = {'tcs', 'tata steel'}

print(var_set, var_set2)

var_set.add('tcs')  # adds an element to the set
print(var_set)
var_set.add('infosys')  # since sets hold unique values, adding a duplicate value does not change the set contents
print(var_set)
print(var_set.union(var_set2))  # returns set with all elements in both sets, after removing duplicate values
print(var_set.intersection(var_set2))  # returns set of all elements present in both sets
print(var_set.difference(var_set2))  # returns set of all elements present in set1 but not in set2
print(var_set.symmetric_difference(var_set2))
print(var_set2.pop(), var_set2)  # pops the first value (acc to ascending order) in the set
var_set2.clear()  # reset!
print(var_set2)
var_set2.add('IBM')
var_set2.update(var_set)  # updates a set by adding all elements in another set
print(var_set2)

# playing with dictionaries
var_dict = {'boo': 'ghost', 'vroom': 'car'}

print(var_dict)

print(var_dict.keys())  # returns iterable with all keys in dict
print(var_dict.values())  # returns iterable with all values in dict
print(var_dict.get('boo'))  # get value for key
print(var_dict['vroom'])  # same effect as above
