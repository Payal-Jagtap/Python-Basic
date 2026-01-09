#List
#Basic List Programs
courses = ['ba', 'bcom', 'bsc', 'ma', 'mcom', 'msc']
print(courses)
print(type(courses))
print(courses[0])
print(courses[2])
print(courses[0:2])
print(courses[1:5])
print(courses[-1])
print(courses[-2])
print(courses[-3:-1])
print(courses[-3:])

#List functions
help(list)
help(list.append)
help(courses.append)
courses.append('BE')
print(courses)

courses.insert(3, 'ME')           
print(courses)
c = 'B.Pharm'
courses.append(c)
print(courses)

new=['IMCA', 'MCA']
courses.append(new)
print(courses)
help(courses.extend)
courses.extend(new)
print(courses)
courses.pop()
print(courses)
courses.remove('ME')
print(courses)
courses.sort()
print(courses)

fruits = ['mango', 'apple', 'orange', 'kiwi', 'pineapple', 'papaya']
print(fruits)
fruits.sort()
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

nums=[5, 3, 8, 1, 4, 7, 2, 6]
print(nums)
nums.sort() 
print(nums)

#General functions that can be used with List
countries = ['Russia', 'India', 'US', 'Japan', 'Germany', 'Italy', 'Zambia']
print(len(countries))
print(len('HELLO WORLD'))

nums = [10, 20, 30, 40, 50]
print(sum(nums))
print(max(nums))    
print(min(nums))
print(max(countries))
print(min(countries))

#Iterating a list
countries = ['Russia', 'India', 'US', 'Japan', 'Germany', 'Italy', 'Zambia']

for item in countries:             
  print(item)

for x in countries:             # x can be changed to any other word
  print(x)

for x in countries:
  print(x)
print('Now I am outside the for loop')

print('-------------')

for x in countries:
  print(x)
  print('Now I am inside the for loop')

for item in countries:
  print(item, len(item))  

for item in countries:
  print(item, item.upper(), len(item)) 

for item in countries:
  print(f'{item}, {item.upper()}, {len(item)}') 

for item in countries:
  print(f'{item} --- {item.upper()} --- {len(item)}')

for id, item in enumerate(countries):   # enumerate returns index along with the actual item, hence we need to catch it explicitly. 
  print(id, item)

for index, item in enumerate(countries):   # id can be changed to anyother thing
  print(index, item)

cubes = []    
for i in range(5):       
  cubes.append(i ** 3)
print(cubes)

cubes = []    
for i in range(5):       
  print("i = ", i)
  cubes.append(i ** 3)
  print("Number appended (i ** 3) = ", i ** 3)
  print("Current status of cubes list = ", cubes)
print()
print('Outside for loop')
print(cubes)


#Nested list
fruits = [['mango','apple','pineapple'], ['sitafal', 'orange']]
print(fruits)
print(len(fruits))
print(fruits[0])
print(fruits[1])

print(fruits[0], type(fruits[0]))
print(fruits[1], type(fruits[1]))
print(fruits[0][0])
print(fruits[1][0])
print(fruits[0][2])



