# groceries.py

#from pprint import pprint

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


# print(products)

# TODO: write some Python code here to produce the desired output

#actual implementation of project code

#definition of local variables
y=0

#definition of local functions
def product_name(products):
    return products["name"]

def department_name(products):
    return products["department"]

#alphabetically sort the list
products2 = sorted(products, key=product_name)
    

#initiate the first printed output
print("")
print("--------------")
print("THERE ARE", len(products), "PRODUCTS:")
print("--------------")
while y < len(products2):
    answer = round(products2[y]['price'],2)
    print("+", products2[y]['name'], f"(${format(answer, '.2f')})")
    y+=1


#initiate the second printed output

#define new list
department_list = []
#add in the departments to the list
for p in products:
    department_list.append(p["department"])

#sort alphabetically
department_list.sort()

#create a list to use for output
department_list_sorted = list(set(department_list))
department_list_sorted.sort()

print("--------------")
print("THERE ARE", len(department_list_sorted), "DEPARTMENTS:")
print("--------------")


#demonstrate use of for loop to output the departments
for i in range(len(department_list_sorted)):
    
    department1 = department_list_sorted[i]
    count = 0

    for x in range(len(department_list)):
        if department_list[x] == department1:
            count += 1
            

    if count > 1:
        print("+", department_list_sorted[i].title(), f"({count} products)")
    else:
        print("+", department_list_sorted[i].title(), f"({count} product)")
