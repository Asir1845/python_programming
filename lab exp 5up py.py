def is_subset(set_a, set_b):
    return all(elem in set_b for elem in set_a)

set_a = set(input("enter a set1:"))
set_b = set(input("enter a set 2:"))

result = is_subset(set_b, set_a)
print(result)
