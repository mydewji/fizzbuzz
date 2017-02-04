"""
Write a program that prints out numbers from 1 to 100, 
but for numbers divisible by 3 prints out "Fizz", 
for numbers divisible by 5 prints out "Buzz" 
and for numbers divisible by both prints out "FizzBuzz".
**PYTHON 3 IMPLEMENTATION**
"""

for number in range(1,100):
	str = ""
	if number % 3 == 0:
		str = "fizz"
	if number % 5 == 0:
		# adds "buzz" only if divisible by both 3 and 5
		str += "buzz"
	else: 
		str = number
	print (str)