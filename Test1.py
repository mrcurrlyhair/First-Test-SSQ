print('hello world')
x = 2 
y = 4
print(x * y) ## personal test ##



num = 6
if num > 0:
    print(num, 'is a positive number')
    print('the statement evealulates to True.')

temperature = 30
if temperature >25: 
    print('its a hot day!')

fruits = ['Apple', 'Bannana', 'Cherry'] 
for fruit in fruits:
    print(fruit)


for i in range(5):
     print(i)

count = 0 
while count < 5:  ## while loop stops counting after 5, stops at it would just continue on for infinity ##
    print(count)
    count += 1

for i in range(10):
    if i == 5 :
        break #stops the loop when i = 5
    print(i)

for i in range (5):
    if i ==2:
        continue #skips 2
    print(i)

def opinion():
    print('virtual machines are terrible')

opinion() # output the definition 

name = input('please enter your name.') # eneter name varaible 

def greet(name):
    print(f'hello,{name}!')    #definition for greeting 

greet(name)  #print greet def and name 


def greet2 (name2='Stranger'):
    print(f'HELLO, {name2}!')

greet2()

