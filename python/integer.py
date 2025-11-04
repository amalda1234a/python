numbers =list(map(int,input("enter integers separated by space:").split()))
result =['over' if num > 100 else num for num in numbers]
print("Modified list:",result)
