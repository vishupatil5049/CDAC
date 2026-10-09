
products=[
    {"id":1, "name":"Laptop", "category":"Elctronics", "price":55000, "quantity": 10},
    {"id":2, "name":"chair", "category":"Furniture", "price":1500, "quantity": 50},   
    {"id":3, "name":"Laptop", "category":"Elctronics", "price":55000, "quantity": 10}
]

idCounter=len(products)

def menu():
    print("*********** Product Inventory Menu ***********")
    menu_text="""    1: Add Products
    2: View All Products
    3: Search Products
    4: Update Products
    5: Delete Products
    6: Exit
"""
    print(menu_text)
    try:
        choice=int(input("Enter the choice: "))
    except ValueError:
        choice=False
    return choice

#-------------------------------------------------------------------------------------------------------------------------------------
def addProduct():
        global idCounter
        try:
            name=input("Enter the name of product: ").strip().capitalize()
            if name == "":
                print("Name cannot be empty string")
                return
            category=input("Enter the category of product: ").strip().capitalize()
            if category == "":
                print("Category cannot be empty string")
                return
            price=int(input("Enter the price of product: "))
            if price <= 0:
                print("Price must be greater than 0")
                return
            quantity=int(input("Enter the quantity of product: "))
            if quantity < 0:
                print("quantity must be >= 0") 
                return           
        except:
            print("Enter the valid value")
        
        pid = idCounter + 1 
        products.append(dict(id=pid, name=name, category=category, price=price, quantity=quantity))
        print("Product added to inventory")
#-------------------------------------------------------------------------------------------------------------------------------------
def viewProducts():
    if len(products)==0:
        print("The inventory is empty")
    elif len(products)==1:
        viewoneProduct(products[0])
    else:
        viewManyProducts(products)

#-------------------------------------------------------------------------------------------------------------------------------------
def viewoneProduct(p):
    for p in products:
        pid, name, category, price, quantity= p.values()
        print(f'"Id"      :{pid}\n"Name"    :{name}\n"Category":{category}\n"Price"   :{price}\n"Quantity":{quantity}\n')
#-------------------------------------------------------------------------------------------------------------------------------------
def viewManyProducts(p_list):
    print("-"*60)
    print(f"{"ID":^5}{"Name":<20}{"Category":<20}{"Price":>10}{"Qty":^5}")
    print("-"*60)
    for p in p_list:
        pid, name, category, price, quantity= p.values()
        print(f'{pid:^5}{name:<20}{category:<20}{price:>10}{quantity:^5}')
    print("-"*60)
#-------------------------------------------------------------------------------------------------------------------------------------
def searchProduct():
    choiceText='''    1: Search By ID
    2: Search By Name
'''
    print(choiceText)
    try:
        a=int(input("Enter the choice: "))
    except:
        print("Enter integer value")
    if a==1:
        searchById()
    elif a==2:
        searchByName()
    else:
        print("try again")

#-------------------------------------------------------------------------------------------------------------------------------------
def searchById():
    global products
    try:
        sid=int(input("Enter the product ID to search: "))
    except:
        print("Enter Integer Value")
    validId=[pid for pid in products if pid['id']==sid ]
    viewoneProduct(validId)

def searchByName():
    global products
    sname=input("Enter the product Name to search: ").capitalize()
    validName=[pname for pname in products if pname['name']==sname]
    viewManyProducts(validName)
#-------------------------------------------------------------------------------------------------------------------------------------
def updateProduct():
    updated=None
    try:
        a=int(input("Enter the product Id to update: "))
        updated= [pid for pid in products if pid['id']==a ]
        if updated==None:
            print("ID not found")
            return
        else:
            try:
                uname=str(input("Enter the new name of product: ")).strip().capitalize()
                if uname == "":
                    print("Name cannot be empty string")
                    return
                ucategory=str(input("Enter the new category of product: ")).strip().capitalize()
                if ucategory == "":
                    print("Category cannot be empty string")
                    return
                uprice=int(input("Enter the new price of product: "))
                if uprice <= 0:
                    print("Price must be greater than 0")
                    return
                uquantity=int(input("Enter the quantity of product: "))
                if uquantity < 0:
                    print("quantity must be >= 0")   
                    return         
            except:
                print("Enter the valid value")
    except:
        print("Enter integer value")
    updated[0]['name']=uname
    updated[0]['category']=ucategory
    updated[0]['price']=uprice
    updated[0]['quantity']=uquantity
#-------------------------------------------------------------------------------------------------------------------------------------
def deleteProduct():
    global products
    updated=None
    try:
        a=int(input("Enter the product Id to delete: "))
        updated= [pid for pid in products if pid['id']==a ]
        if updated==None:
            print("ID not found")
            return
        else:
            c1=input(f"Do you really want to delete product with id {a} (y/n)[No]: ").upper()
            if c1 in['Y','YES']:
                products.remove(updated[0])
                print("Succesfully Deleted")
            else:
                print("Deletion canceled")
                
    except:
        print("Enter integer value")
#-------------------------------------------------------------------------------------------------------------------------------------
def main():
    while True:
        choice=menu()
        match choice:
            case 1:
                addProduct()
            case 2:
                viewProducts()
            case 3:
                searchProduct()
            case 4:
                updateProduct()
            case 5:
                deleteProduct()
            case 6:
                print("Exiting Menu")
                break
            case _:
                print("Invalid Choice. Try again")
main()