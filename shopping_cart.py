#from pprint import pprint
import datetime

x = datetime.datetime.now()
#computer stamp of time
print(str(x))
print("------------------")
print("WELCOME TO WEGMANS")
print("------------------")
print(" ")
print("To checkout, enter the numeric id's of your products and type 'END' when finished")
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017
total_price = 0
grocery_ids = []
valid_inputs = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
#Info Capture/input of the grocery id's, elif statement to check if valid entry from list of permitted entries
while True:
    grocery_id = input("Please input a product identifier id number: ") #This is a string input
    
    if grocery_id == "END":
        break
    elif grocery_id in valid_inputs:
        grocery_ids.append(grocery_id)
    else:
        print("Please enter a valid input.")
#Info display/outpu, displays dates and the individual products selected
print(" ")
print(x.strftime("%Y-%m-%d"))
print("Your Cart: ")
for grocery_id in grocery_ids:
        matching_products = [p for p in products if str(p["id"]) == str(grocery_id)]
        matching_product = matching_products[0]
        total_price = total_price + matching_product["price"]  
        print("Purchased Item: " + matching_product["name"] + " $" + str(matching_product["price"]))

#Gives 10 reward points for every dolar spent
rewards_points = ((round(total_price) * 10))
#receipt below
print(" ")
print("------------------------------------------------")
print("SUBTOTAL: $" + str(round(total_price, 2)))
print("SALES TAX: $" + str(round(total_price * 0.0875, 2)))
print("AMOUNT OWED: $" + str(round(total_price * 1.0875, 2)))
print("You have earned " + str(rewards_points) + " rewards points today.")
print("------------------------------------------------")
print(" ")
print("Thank you for Shopping at Wegmans, we can't wait")
print("to see you again!")
print("For customer service inquiry, please contact us")
print("at our customer support line: 1-800-934-6267")

#print(products)
# pprint(products)
