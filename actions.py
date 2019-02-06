from pymongo import MongoClient

# connect to MongoDB and select 'product' collection from 'SHOP' database
db = MongoClient("mongodb://localhost:27017")["SHOP"]
collection = db.products

def show_product_list():
    for product in collection.find():
        print(product)

def insert_product(name, price, quantity):
    collection.insert_one({
        "name": name,
        "price": price,
        "quantity": quantity
    }).inserted_id

def update_product(name, new_name, new_price, new_quantity):
    collection.find_one_and_replace(
        {
            'name': name
        },
        {
            'name': new_name,
            'price': new_price,
            'quantity': new_quantity
        })

def delete_product(name): 
    collection.find_one_and_delete({
        "name": name
    })
