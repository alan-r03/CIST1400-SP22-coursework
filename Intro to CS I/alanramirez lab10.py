item_list = []
price_list = []
quantity_list = []

def isFloat(number):
    #found this on the internet to check if a value is a float or not, for integers, isdigit() works
    try:
        float(number)
        return True
    except ValueError:
        return False

def add_update_items(selection):
    #all of the while loops in this function are just checking user inputs to ensure the user doesn't input a value the program cannot work with
    if selection == "update" and len(item_list) == 0:
        print("There are currently no items stored in your shopping cart.")
        return()
    item = input(f'Enter the name of the item to {selection}: ')
    while selection == "add" and item in item_list:
        item = input("That item is already in your shopping cart, please enter a new item to add: ")
    while selection == "update" and item not in item_list: 
        item = input(f'The item was not found in your shopping cart, please enter another item to update: ')
    price = input('Enter the{} price of the item: '.format(" updated" if selection == "update" else ""))
    while isFloat(price) != True:
        price = input('Error, please enter the{} numeric price of the item: '.format(" updated" if selection == "update" else ""))
    quantity = input('Enter the{} quantity of the item: '.format(" updated" if selection == "update" else ""))
    while quantity.isdigit() != True:
        quantity = input('Error, please enter the{} integer quantity of the item: '.format(" updated" if selection == "update" else ""))
    if selection == "add":
        item_list.append(item)
        price_list.append(float(price))
        quantity_list.append(int(quantity))
    elif selection == "update":
        item_index = item_list.index(item)
        price_list[item_index] = float(price)
        quantity_list[item_index] = int(quantity)

def remove_items():
    if len(item_list) == 0:
        print("There are currently no items stored in your shopping cart.")
        return()
    item = input("Enter the name of an item you wish to remove from your shopping cart: ")
    while item not in item_list:
        item = input("The item was not found in your shopping cart, please enter the name of an item you wish to remove: ")
    item_index = item_list.index(item)
    print(f'\n{item} was removed from your shopping cart.')
    item_list.pop(item_index)
    price_list.pop(item_index)
    quantity_list.pop(item_index)

def display_items(method):
    total_price = 0
    sorted_list = []
    if len(item_list) == 0:
        print("There are currently no items stored in your shopping cart.")
        return()
    if method == "abc":
        for item in item_list:
            sorted_list.append(item)
        sorted_list.sort()
    elif method == "price":
        for index, item in enumerate(price_list):
            sorted_list.append([item, round(item*quantity_list[index],2), item_list[index]])
        sorted_list.sort(key=lambda x:x[1]) #also found this on the internet for sorting lists of lists
    for item in sorted_list:
        item_index = item_list.index(item) if method == "abc" else item_list.index(item[2])
        print(f'{item_list[item_index]} ({quantity_list[item_index]} at ${price_list[item_index]}/item) : ${round(quantity_list[item_index] * price_list[item_index], 2)}')
        total_price += round(quantity_list[item_index] * price_list[item_index], 2)
    print(f'\nTotal price of all items in your cart: ${total_price}')

print("Welcome to the Generic eCommerce Store!")
while True:
    choice = input("\nWhich of the following would you like to do?:\n1. Add Item\n2. Update Item\n3. Delete Item\n4. Display Items by Name\n5. Display Items by Total Price\n6. Quit\nEnter the number of your choice: ")
    print()
    while choice not in ("1", "2", "3", "4", "5", "6"):
        choice = input("Incorrect input. Enter the number of your choice: ")
    if choice in ("1", "2"):
        if choice == "1":
            add_update_items("add")
        elif choice == "2":
            add_update_items("update")
    elif choice == "3":
        remove_items()
    elif choice in ("4", "5"):
        if choice == "4":
            display_items("abc")
        elif choice == "5":
            display_items("price")
    elif choice == "6":
        break