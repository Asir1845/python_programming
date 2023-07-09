num_elements = int(input("Enter the number of elements in the list: "))
my_list = []

for i in range(num_elements):
    value = int(input("Enter the value: "))
    my_list.append(value)

print("Original list:", my_list)

ascending = True

for i in range(1, num_elements):
    if my_list[i] < my_list[i-1]:
        ascending = False
        break
if ascending:
    print("Yes, the list is in ascending order.")
else:
    print("No, the list is not in ascending order.")
