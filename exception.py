def add(a1,a2):
	print(a1 + a2)

add(10,20)
number1 = 10
number2 = input("Please provide a number ")  # This gives back a string. 
print("This will never run because of the type error")

try:
	#You you want to attempt to try. 
	result= 10 + 10

except:
	print("It looks like you are not adding correctly")

else:
	print("NO ERRORS!")
	print(result)


