number = list(range(10))
print(number)

for i in range(5):
    print(i)
print('---------------------')
for i in range(1, 10, 2):
    print(i)
print('---------------------')
for i in range(0, 36, 5):
    print(i)
print('---------------------')
for i in range(36, 0, -5):
    print(i)
print('---------------------')
#Comprehension list
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even  = [ num * 2 for num in number]
print(even)

new_even = [ num for num in number if num % 2 == 0]
print(new_even)
