"""
Write a program that prints out numbers from 1 to 100, 
but for numbers divisible by 3 prints out "Fizz", 
for numbers divisible by 5 prints out "Buzz" 
and for numbers divisible by both prints out "FizzBuzz".
**PYTHON 3 IMPLEMENTATION**
**RECURSIVE DEFINITION**
"""

def fizzbuzz (start, end):
  str = ""
  if start % 3 == 0:
    str =  'fizz'
  if start % 5 == 0:
    str += 'buzz'
  else:
    str = start
  print (str)

  if start < end:
    fizzbuzz(start+1, end)
  
fizzbuzz(1, 100) 