size1 = int(input("Enter size of first list: "))
list1 = []

print("Enter elements of first list:")
for i in range(size1):
    number = int(input())
    list1.append(number)

size2 = int(input("Enter size of second list: "))
list2 = []

print("Enter elements of second list:")
for i in range(size2):
    number = int(input())
    list2.append(number)

common_count = 0

for number in list1:
    if number in list2:
        common_count += 1

print("Number of common elements:", common_count)