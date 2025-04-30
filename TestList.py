import itertools
import numpy as np


def show():
    List = [1,2,3,4,5,6,7,8,9]
    print("Original List: \n", List)
    print("\nSliced List: \n")
    print(List[1:9:2])
    print(List[::2])

show()

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

print(cities)
cities.append('Boston')

del cities[2]
print(cities)

print(cities.count('New York'))
print(cities.index('Houston'))

cities.sort()
print(*cities)

cities.reverse()
print(*cities)

cities.sort(reverse=True)
print(*cities, sep = '\n')

