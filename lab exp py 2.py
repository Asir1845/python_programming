def is_obtained_by_deletion(first_string, second_string):
    first_set = set(first_string)
    second_set = set(second_string)
    return second_set.issubset(first_set)

first_string=input("enter a string1:")
second_string = input("enter a string2:")
result = is_obtained_by_deletion(first_string, second_string)

if result:
    print("YES")
else:
    print("NO")



