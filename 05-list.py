my_num = ['hello', "english", 1]

print(len(my_num))

print(my_num[0])

print(my_num[-1])

print(my_num[1:2])

print(my_num[2:])

my_num.insert(1, 'hindi')

print(my_num)

my_num2 = [1, 2, 3, 4]

my_num.extend(my_num2)

print(my_num)

my_num.remove('english')

print(my_num)

my_num2.reverse()

print(my_num2)

print(my_num2.pop())

my_num2.sort()
print(my_num2)

sorted_list = sorted(my_num2)
print((sorted_list))

num = [4, 6, 8, 3, 6]

print(max(num))
print(sum(num))
print(num.index(8))
print(8 in num)

for index, item in enumerate(num, start=3):
    print(index, item)

numstr = ['2', '4', '5']

num_str = ', '.join(numstr)

print(num_str)

num_arr = num_str.split(',')
print(num_arr)

tuple1 = (1, 2, 3, 4)

print(tuple1)

# tuple1[0]=1

dict1 = {'eng', 'hin', 'mat', 'eng'}
dict2 = {'phy', 'hin', 'mat', 'sci'}

print(dict1)

print(dict1.intersection(dict2))

print(dict1.union(dict2))

# empty list [] / list()
# empty set set() / not valid ()<- dictionary
# empty tuple ()/tuple()

student = {'name': 'john', 'age': 34}
# student['name1']='ut'

print(student.get('name1', 'Not Found'))

student.update({'name': 'jon', 'age1': 34})

print((student))

# del student['name']

age1 = student.pop('age1')

print(student)

print(len(student))

print(student.values())

print(student.items())

for key, value in student.items():
    print(key, value)
