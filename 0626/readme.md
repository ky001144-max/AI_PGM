digit
string

variable=expression
literal or constant	a=1
vaiable			a=b
operator			a=1+b
function			a=sum(1,2)


%d "%(1,2)

%{} ".format(1,2)

a=1
b=2
f"{a}{b}

print("I eat %d apples and %d oranges."%(3, 5))
print("I eat {0} apples and {1} oranges.".format(3, 5))
print(f"i eat {3} apples and {5} oranges.")
print(f"i eat 3 apples and 5 oranges.")

결과값
list 		[ ]
tuple 	( )
set		{ }
dictinary	{ : }

두개의 정수를 입력받아 사칙연산의 결과를 출력하세요
5개의 정수값을 입력받아 리스트에 저장하고 그 리스트의 합, 평균, 최소값, 최대값을 출력하세요
과일명이 잇는 리스트를 정의하고 그 리스트의 첫번째와 마지막 문자열을 출력하세요

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"you entered: {a} and {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))
number = [num1, num2, num3, num4, num5]
print(f"sum ={sum(number)}")
print(f"average ={sum(number)/len(number)}")
print(f"max ={max(number)}")
print(f"min ={min(number)}")

fruits = []
fruit = input("Enter a fruit: ")
fruits.append(fruit)
fruit = input("Enter a fruit: ")
fruits.append(fruit)
fruit = input("Enter a fruit: ")
fruits.append(fruit)
fruit = input("Enter a fruit: ")
fruits.append(fruit)
fruit = input("Enter a fruit: ")
fruits.append(fruit)
fruit = input("Enter a fruit: ")
fruits.append(fruit)
print(fruits)
print(fruits[0])
print(fruits[-1])
