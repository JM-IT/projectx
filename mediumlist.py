menu_item = 0
#here  were are initializing a list
name_list =[]
user=input(" Enter your name  to access the program:")

while menu_item !=10:
	print("------Welcome to list implementation--------")
	print("1. View the list.")
	print("2. Add a name to the list.")
	print("3. Remove a name from the list.")
	print("4. Change an item in the list.")
	print("10. Quit")

	menu_item = int(input("Pick an option from the menu:"))
	if menu_item ==1:
		current = 0
		if len(name_list) > 0:
			while current <len(name_list):
				print(current, ".", name_list[current])
				current +=1
		else:
			print("The list is empty.")
	elif menu_item == 2:
		name = input("Type a name to add in the list:")
		name_list.append(name)
		print("Name successfully added")
	elif menu_item == 3:
		del_name = input("What name would you like to delete?:")
		if del_name in name_list:
			item_number = name_list.index(del_name)
			del name_list[item_number]
		else:
			print("Name no in the list.")
	elif menu_item ==4:
		old_name = input("Enter name to change:")
		if old_name in name_list:
			item_number = name_list.index(old_name)
			new_name = input("Enter the new name:")
			name_list[item_number] =new_name
		else:
			print(old_name, "was not found.")
print(user, "It has been nice to be with you? ")

		
