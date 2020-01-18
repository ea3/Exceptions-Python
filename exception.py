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


try:
	f = open('testfile', 'w')
	f.write('Write a test line')
except TypeError:
	print('There was a type error')
except :
	print('Hey, you have an OS Error')
finally:
	print('I always run')


def ask_for_int():

	while True:

		try:
			result = int(input("Pleae provide a number: "))
		except:
			print("Whoops!That is not a number")
			continue
		else:
			print("Yes, thank you for the number")
			break
		finally:
			print("End of try/except/finally")
			print("I will always run at the end")



	


ask_for_int()




















