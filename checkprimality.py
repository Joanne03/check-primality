

while True:
	user_input = int(input('Please enter a number: '))
	list_divisor = range(1,(user_input+1)) #checked
	list_result = []

	if user_input == 'q':
		print('program ended')
	else:
		for ele in list_divisor:
			if str(user_input % ele) == '0':
				list_result.append(ele)

		if len(list_result) == 2:
			print('Divisors: ' + str(list_result))
			print('This number is prime')
		else:
			print('Divisors: ' + str(list_result))
			print('This number is not prime')


