import logging


def show():
    List = [1,2,3,4,5,6,7,8,9]
    print("Original List: \n", List)
    print("\nSliced List: \n")
    print(List[1:9:2])
    print(List[::2])

show()

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.debug("Original Cities: %s",cities)

cities.append('Boston')

del cities[2]
print(cities)


print(cities.index('Houston'))

cities.sort()
logger.debug('Sorted Series : %s', cities)

cities.reverse()
print(*cities)

cities.sort(reverse=True)
print(*cities, sep = '\n')

