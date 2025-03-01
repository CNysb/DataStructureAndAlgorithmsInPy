import timeit
import array
import sys


original_data = list(range(1000))

my_list = original_data
my_array = array.array("i", original_data)

# print(sys.getsizeof(my_list))
# print(sys.getsizeof(my_array))

print(timeit.timeit(lambda: my_list[2], number=1000))
print(timeit.timeit(lambda: my_array[2], number=1000))
