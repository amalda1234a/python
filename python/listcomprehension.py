numbers = list(map(int,input("enter a list of integers:").split()))
word = input("enter a word:")
positive_list = [num for num in numbers if num > 0]
print("a.positive numbers:",positive_list)
square_list = [num  ** 2 for num in numbers]
print("b. squares of numbers:" ,square_list)
vowels = [ch for ch in word if ch.lower() in 'aeiou']
print("c.vowels in the word:",vowels)
ordinal_values = [ord(ch) for ch in word]
print("d. ordinal values:",ordinal_values)
