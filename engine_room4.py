#Tuple
#Basic Implementations of Tuple
courses = ('ba', 'bcom', 'bsc')
print(courses)
print(type(courses)) 
print(courses[0])
print(courses[1])
print(courses.count('bsc'))
print(courses.index('bcom'))
for item in courses:
    print(item)

for id,item in enumerate(courses):
    print(id, item)

print(len(courses))
nums = (1,2,3,4,5)
print(type(nums))

data=('abc', 123, 45.67, True)
print(data)
print(type(data))
print(data[0])
print(data[2])
print(data[-1])
print(data[-3:-1])

for item in data:
    print(item, type(item))

new=('50')
print(type(new))

new1 = ('50',)
print(type(new1))

print(('a','b','c')+(1,2,3))
new = ('50',)
new1 = ('apple',)
new2 = ('mango','orange')
print(new + new1 + new2)

del new

fruits = ('apple','mango')
print('mango' in fruits)
print('mangoes' in fruits)

print(max(2, 1, 3, 7))
print(min(2, 1, 3, 7))

num=[1,2,3,4,5]
new=tuple(num)
print(new)
print(num)

num = (1, 2, 3, 4, 5, 6, 7)
print(num[-1])
print(num[-2])

print(num[6])


