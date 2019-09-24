my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_list[2:-1:2])

print(my_list[-2:1:-2])

my_string = 'http://www.google.com'

print(my_string[::-1])

my_list2 = [n * n for n in my_list]
print(my_list2)

my_list3 = map(lambda n: n * n, my_list)
print(list(my_list3))

my_list4 = [n for n in my_list if n % 2 == 0]
print(my_list4)

my_list5 = filter(lambda n: n * n, my_list)
print(list(my_list5))

my_list6 = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list6)

name = ['a', 'b', 'c']
name2 = ['d', 'e', 'f']

print(list(zip(name, name2)))

my_list7 = {name: name2 for name, name2 in zip(name, name2) if name != 'a'}

print(my_list7)
nums = [1, 1, 1, 2, 3, 4, 4, 5]
my_list8 = {n for n in nums}
print(my_list8)

# sorted return sorted list but sort will change original list
# sorted(list,reverse=true)
# li.sort(reverse=true)
# for tuple ->() and dict sorted will work a

li = [-3, -4, -6, 3, 6, 7]
li2 = sorted(li, key=abs)
print(li2)
