dummy="Wellcome to the engine room!"
print(dummy)
print(type(dummy))

num1=3
num2=3.0
print(type(num1))
print(type(num2))

val = True
print(type(val))

print(num1)
print(num2)
print(val)

#Strings
#String Basics

test = 'Apple\'s products are beautiful' 
print(test)

test = "Apple's products are beautiful" 
print(test)

text = "Hello World"
print(len(text))

text = "Opportunities don't happen, you create them."
print(text[0])
print(text[8])

print(text[2:13])
print(text[:2])
print(text[2:])

text = "Welcome to Python!"
print(type(text))
print(type(text[2:4]))

#String Functions

text = "heLLo worLD!"
print(text.upper())
print(text.lower())
print(text.title())

text = 'hello world'
print(text.count('l'))

print(text.count('rl'))

print(text.find('o'))

print(text.find('Z'))

print(text)             
print(text.count('H'))  
print(text.find('H'))

text = 'This is a beautiful world'
print(text.find('beautiful'))

print(text.count('beautiful'))   
print(text.count('is'))          

print(text.replace('world', 'planet'))

print(text)

new_text = text.replace('world','planet')
print(new_text)
print(text)

fruit = 'applllllleeeeeee'
print(fruit.replace('e','E'))
print(fruit.replace('z','E'))

msg = '   Hello World    '
print(msg)
print(msg.strip())

print(len(msg))
print(len(msg.strip()))

print(msg.count(' '))
print(msg.strip().count(' '))  


address = '102, Baker St, London'
print(address.split(','))

test = 'how are you doing'
print(test.split(' ')) 

output = test.split(' ')
print(output)
print(type(output))

first = 'Bill'
last = 'Musk'
name = first + last
print(name)

name = first + ' ' + last
print(name)
name = first + '    ' + last
print(name)

name = '{}{}'.format(first, last)
print(name)
name = '{} {}'.format(first, last)
print(name)
name = '  {}     {}  '.format(first, last)
print(name)
name = '  {}     {}  '.format(last, first)
print(name)

name = f'{first}{last}'
print(name)
name = f'{first} {last}'
print(name)
name = f'{first}    {last}'
print(name)

name = f'{first.upper()} {last.lower()}'
print(name)

#Integer & Float

num1 = 3
num2 = 5
print(num1, num2)
print(type(num1), type(num2))

res = num1 + num2
print(res)

print(num1-num2)
print(num1*num2)
print(num2 / num1)
print(num2 // num1)
print(num2 % num1)

print(type(num2/num1))

new1 = 2.1
new2 = 0.3
print(new1 + new2)
print(new1 - new2)

fir = 3
sec = 0.1
print (fir + sec)

#Extra Learning
#Accepting User input

name = input('enter your name:')
print(name)
print(type(name))

text = input('Enter some text: ->')
print(text.upper())
print(text.title())
print(text.find('j'))
print(text.count('p'))
print(text.replace('p','k'))
print(len(text))

#help(), dir() functions

#help(str)
dir(str)
#help(str.upper)

#Opeartors
#Arithmatic Operators
a=10
b=5
print(a,b)
print(type(a),type(b))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

print(9//3)
print(8//3)
print(7//3)
print(6//3)

print(9%3)
print(8%3)
print(7%3)  
print(6%3)

print(5*4+1)
print(1+5*4)
print(5*(4+1))

#Comparison Operators

print(2==2)
print(2==1)
print(3 != 2) 
print(3 > 2)
print(3 < 2)
print(3 >= 3)
print(3 >= 2)
print(3 <= 2)

a=5
print(a)
a+=1
print(a)
a-=1
print(a)
a*=2
print(a)
a/=2
print(a)

