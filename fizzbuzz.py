# Write a program that prints out numbers from 1 to 100, but for numbers divisible by 3 prints out "Fizz", for numbers divisible by 5 prints out "Buzz" and for numbers divisible by both prints out "FizzBuzz".

for number in range(1,100):
	str = ""
	# To check if number is divisible by both 5 and 3
	if number % 15 == 0:
		str = "fizzbuzz"
	# Check to see if number divisible by 5
	elif number % 5 == 0:
		str += "buzz"
	# Check to see if number divisible by 3
	elif number % 3 == 0:
		str = "fizz"
	# If neither return number
	else: 
		str = number
	print str