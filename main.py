from actions import show_product_list, insert_product, update_product, delete_product

title = "**** CRUD with MongoDB and Python ****\n"
menu = """
 ~ Select an action

    1 - Show product list
    2 - Insert product
    3 - Update product
    4 - Delete product 
    5 - Exit
"""

print(title + menu)

action = 0

while action != 5:
    if action == 1:
        show_product_list()

    elif action == 2:
        name = raw_input("Name: ")
        price = input("Price: ")
        quantity = input("Quantity: ")
        insert_product(name, price, quantity)

    elif action == 3:
        name = raw_input("Old name: ")
        new_name = raw_input("New name: ")
        new_price = input("New price: ")
        new_quantity = input("Quantity: ")
        update_product(name, new_name, new_price, new_quantity)

    elif action == 4:
        name = raw_input("Name: ")
        delete_product(name)
