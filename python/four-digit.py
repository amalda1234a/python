import math
even_square_numbers=[]
for num in range(1000,10000):
    digits=str(num)
    if all(int(d)%2==0 for d in digits):
       root=int(math.sqrt(num))
       if root*root==num:
          even_square_numbers.append(num)
          print("four digit numbers with all even digits and perfect square:")
          print(even_square_numbers)
