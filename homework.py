#Handle the exception thrown by the code below by using try and except blocks.
try:
	for i in ['a', 'b', 'c']:
		print(i **2)
except TypeError:
	print("THere was an error. Fix the code")
finally:
	print("Check the documentation")

#############Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'



try:
	x = 5
	y = 0	
	z = x/y
except ZeroDivisionError:
	print('You are trying to divide by zero. Can not do that')
finally:
	print('All done')

###########Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.



















