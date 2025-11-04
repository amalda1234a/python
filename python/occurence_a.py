names=input("enter first names:").split()
count_a=sum(name.lower().count('a') for name in names)
print("total occurences of 'a':",count_a)
