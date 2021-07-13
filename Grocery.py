
shopping_lists = [] #global array

class List:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.items = []


class Item:
    def __init__(self, title, price, quantity) -> None:
        self.title = title
        self.price = price
        self.quantity = quantity


while True:

    print("-----Shopping Lists-----")
    print("1 - Create a new list")
    print("2 - Show all lists")
    print("3 - Add item to list")
    print("4 - Delete a list")
    print("5 - Delete an item from a list")
    print("6 - Quit")

    choice = input("Please enter the number of your selection. ")

    if choice == "6":
        break

    if choice == "1":
        name = input("What store? ")
        address = input("What is the address? ")
        store = List(name, address)
        shopping_lists.append(store)


    if choice == "2":
        for store in shopping_lists:
            print(f"{store.name} - {store.address}")
            for index in range(0, len(store.items)):
                full_list = store.items[index].title
                print(full_list)


    if choice == "3":
        for i in range(0, len(shopping_lists)):
           print(f"{i +1}--{shopping_lists[i].name}")
           store = shopping_lists[i]
           
        store_location = int(input("Which store? "))
        title = input("What item would you like to add to your list? ")
        price = input("How much does it cost? ")
        quantity = input("How many would you like? ")
        item = Item(title, price, quantity)
        shopping_list = shopping_lists[store_location -1]
        shopping_list.items.append(item)


    if choice == "4":
        for i in range(0, len(shopping_lists)):
            print(f"{i +1}--{shopping_lists[i].name}")
            choice2 = int(input("Select the number of the store. "))
            del shopping_lists[choice2 - 1]
            print("List has been deleted.")


    if choice == "5":
        for i in range(0, len(shopping_lists)):
           print(f"{i +1}--{shopping_lists[i].name}")
           store = shopping_lists[i]
        choice3 = int(input("Enter store choice: "))
        store = shopping_lists[choice3 - 1]
        for i in range(0, len(store.items)):
            print(f"{i + 1} {store.items[i].title}")
        itemToDeleteIndex = int(input("Enter item to delete: "))
        del store.items[itemToDeleteIndex]
        print("Item deleted.")
           
        

    

