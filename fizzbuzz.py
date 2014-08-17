# Write a program that prints out numbers from 1 to 100, but for numbers divisible by 3 prints out "Fizz", for numbers divisible by 5 prints out "Buzz" and for numbers divisible by both prints out "FizzBuzz".

for number in range(0,100):
	# Case for when number is 0
	if number == 0:
		print number
	#Check for division by 3
	elif number%3 ==0:
		#Check for division by 5 if division by 3 works
		if number%5==0:
			print "FizzBuzz"
		print "Fizz"
	# Check for division by 5
	elif number%5==0:
		print "Buzz"
	#Print number if not divisible by 3 or 5
	print number