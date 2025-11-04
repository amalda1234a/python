list1 = list(map(int,input("enter first list of integers:").split()))
list2 = list(map(int,input("enter the second list of integers:").split()))
same_length = len(list1) ==len(list2)
print("both list have same length:",same_length)
same_sum = sum(list1) == sum(list2)
print("both lists have same sum:",same_sum)
common_values = set(list1)&set(list2)
if common_values:
    print("common values in both lists:",comon_values)
else:
    print("no common values")
