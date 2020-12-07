#declaration of variables
month_input =int(input("What is the month(1-12)?"))

months =['January','February','March', 'April','May', 'June','July','August','September','October','November','Decemeber']

if 1<= month_input <=12:
	print("The month is:", months[month_input - 1])

