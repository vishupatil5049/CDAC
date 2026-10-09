def menu():
    print("*********** Book Menu ***********")
    menu_text="""      1: Add Book
      2: View Catalog
      3: Search Books
      4: Update Details
      5: Delete Book
      6: Save to File
      7: Load From File
      8: Exit
  """
    print(menu_text)
    try:
        choice=int(input("Enter the choice: "))
    except ValueError:
        choice=False
    return choice
#------------------------------------------------------------------------------------------
    
def add_book_entry(catalog: list[dict], next_id: int):
    try:
        title=input("Enter the Book Title: ").strip().capitalize()
        if title == "" or title.isnumeric():
            print("The title is invalid")
            return
        author=input("Enter the Book Author: ").strip().capitalize()
        if author == "" or author.isnumeric():
            print("The author name is invalid")
            return
        genre=input("Enter the Book Genre: ").strip().capitalize()
        if genre == "" or genre.isnumeric():
            print("The genre is invalid")
            return
        try:
            price=float(input("Enter the Book price: "))
        except ValueError:
            print("Price should be an integer value")
            return
        if price <= 0.0:
            print("Price cannot be negative value")
            return
        try:
            copies=int(input("Enter the Book copies: "))
        except ValueError:
            print("Copies should be an integer value")
            return
        if copies < 0:
            print("Price cannot be negative value")
            return
    except:
        print("Enter valid value")  
        return  
    newBook={
    "id":next_id,
    "title":title,
    "author":author,
    "genre":genre,
    "price":price,
    "copies":copies
}

    catalog.append(dict(newBook))
    next_id += 1
    return next_id
#------------------------------------------------------------------------------------------

def render_catalog(catalog: list[dict]):
    if len(catalog)==0:
        print("The list is empty")
    elif len(catalog)==1:
        printValue(catalog[0])
    else:
        printValues(catalog)

#------------------------------------------------------------------------------------------
def printValue(c):
        next_id, title, author, genre, price, copies = c.values()
        print(f" id     = {next_id}\n title  = {title}\n author = {author}\n genre  = {genre}\n price  = {price}\n copies = {copies}")
        
#------------------------------------------------------------------------------------------

def printValues(p_list):
    print("-"*79)
    print(f"{"ID":^5}{"Title":<20}{"Author":<20}{"Genre":<20}{"Price":<7}{"copies":>7}")
    print("-"*79)
    for p in p_list:
        next_id, title, author, genre, price, copies= p.values()
        print(f'{next_id:^5}{title:<20}{author:<20}{genre:<20}{price:<7}{copies:>7}')
    print("-"*79)
#------------------------------------------------------------------------------------------
   
def query_books(catalog: list[dict], search_term: str):
    if search_term.strip() == "" or search_term.strip() == "0":
        print("Search term cannot be empty")
        return
    
    elif search_term.isnumeric():
        tlist=[pid for pid in catalog if pid["id"]==int(search_term)]
        if len(tlist)==0:
            print(f"No dictionary found for ID {search_term}")
        else:
            printValue(tlist[0])

    elif search_term.isalpha():
        tlist=[ptitle for ptitle in catalog if ptitle["title"].lower()==search_term.lower() or ptitle["author"].lower()==search_term.lower() ]
        if len(tlist)==0:
            print(f"No dictionary found for title {search_term}")
        else:
            printValues(tlist)
    else:
        print(f"No matching value found for {search_term}")

#------------------------------------------------------------------------------------------

def modify_book_details(catalog: list[dict], book_id: int):
    result=[pid for pid in catalog if pid["id"]==book_id]
    if len(result) == 0:
        print("The ID not found")
    else:
        try:
                ntitle=input("Enter the Book Title: ").strip().capitalize()
                if ntitle == "" or ntitle.isnumeric():
                    print("The title is invalid")
                    return
                nauthor=input("Enter the Book Author: ").strip().capitalize()
                if nauthor == "" or nauthor.isnumeric():
                    print("The author name is invalid")
                    return
                ngenre=input("Enter the Book Genre: ").strip().capitalize()
                if ngenre == "" or ngenre.isnumeric():
                    print("The genre is invalid")
                    return
                try:
                    nprice=float(input("Enter the Book price: "))
                except ValueError:
                    print("Price should be an integer value")
                    return
                if nprice <= 0.0:
                    print("Price cannot be negative value")
                    return
                try:
                    ncopies=int(input("Enter the Book copies: "))
                except ValueError:
                    print("Copies should be an integer value")
                    return
                if ncopies < 0:
                    print("Price cannot be negative value")
                    return
        except:
            print("Enter valid value")  
            return  
        result[0]["id"]=book_id
        result[0]["title"]=ntitle
        result[0]["author"]=nauthor
        result[0]["genre"]=ngenre
        result[0]["price"]=nprice
        result[0]["copies"]=ncopies

#------------------------------------------------------------------------------------------

def sync_catalog_to_file(filepath: str, catalog: list[dict]):
    with open(filepath, "w") as file:
        for book in catalog:
            line="|".join(str(value) for value in book.values())
            file.write(line+ "\n")
        print("Successfully Saved")
#------------------------------------------------------------------------------------------

def load_catalog_from_file(filepath: str):
    catalog = [] 
    with open(filepath, "r") as file: 
       for line in file: 
            if not line.strip():
                continue
            values = line.strip().split("|") 
            book = { "id": int(values[0]),
                     "title": values[1],
                    "author": values[2],
                      "genre": values[3], 
                      "price": float(values[4]),
                    "copies": int(values[5]) } 
            catalog.append(book)
            print("Successfully file content loaded ")
            return catalog
    
#------------------------------------------------------------------------------------------

def main():
    catalog=[]
    next_id= 1
    while True:
        choice=menu()
        match choice:
            case 1:
                next_id = add_book_entry(catalog, next_id)
            case 2:
                render_catalog(catalog)            
            case 3:
                name=input("Enter value to search: ")
                query_books(catalog, name)                          
            case 4:
                try:
                    pid=int(input("Enter the ID to update: "))
                except:
                    print("ID should be integer value ")
                modify_book_details(catalog, pid)                        
            case 5:
                updated=None
                try:
                    a=int(input("Enter the product Id to delete: "))
                except:
                    print("Enter integer value")
                updated= [pid for pid in catalog if pid['id']==a ]
                if updated==None:
                    print("ID not found")
                    return
                else:
                    c1=input(f"Do you really want to delete product with id {a} (y/n)[No]: ").upper()
                    if c1 in['Y','YES']:
                        catalog.remove(updated[0])
                        print("Succesfully Deleted")
                    else:
                        print("Deletion canceled")
                                    
                
            case 6:
                sync_catalog_to_file("D:\\Vishu\\ALL Documents\\CDAC\\Python\\Assesment Practice\\book.txt", catalog )                              
            case 7:
                load_catalog_from_file("D:\\Vishu\\ALL Documents\\CDAC\\Python\\Assesment Practice\\book.txt")                        
            case 8:
                try:
                    load_catalog_from_file()
                except FileNotFoundError:
                    print("The file is not found")
                break                           
            case _:
                print("Invalid choice. Try again")
main()
