###REDUCE
##from functools import reduce
##num=[3, 4, 6, 9, 34, 12]
##def c_sum(first,second):
##    return first+second
##result= reduce(c_sum,num)
##print(result)


from functools import reduce


my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
my_names = ["Jeff", "Alex", "Jonathan", "Richelle", "Anna"]
my_numbers = [4, 6, 8, 10, 2]


map_result = list(map(lambda x: round(x ** 2,5), my_floats))
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce( lambda num1, num2: num1 * num2, my_numbers)


print(map_result)
print(filter_result)
print(reduce_result)
