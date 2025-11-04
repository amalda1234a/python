numbers=input("enter numbers: ")
num_list=[int(num) for num in numbers.split()]
total=sum(num_list)
print("sum of all items in the list:",total)
