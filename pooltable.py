from tblclass import Pooltable


pool_tables_arr = []

    
for i in range(1, 13):
    table = Pooltable(i)
    pool_tables_arr.append(table)


def display_occupied_tables():
    for table in pool_tables_arr:
        if table.is_occupied == True:
             print(f"Table number: {table.tblnumber}")



def display_open_tables():
    for table in pool_tables_arr:
        if table.is_occupied == False:
            print(f"Table number: {table.tblnumber}")


def save_to_file():
        with open("pool_tabels.txt", "a")as file:
            for table in pool_tables_arr: 
                file.write(f"\nTable number: {table.tblnumber} --- Start time: {table.start_time} --- Total time: {table.total_time} \n")




while True:
    print("/////Welcome to PoolTable Pro!/////")
    print("1 ------- Check out a table ")
    print("2 ------- Check in a table ")
    print("3 ------- Display all OPEN tables ")
    print("4 ------- Close PoolTable Pro ")

    choice = input("Please select an action by entering a number: ")

    if choice == "1":
        display_open_tables()
        choice = int(input("Which table would you like to check out? "))
        chosen_table = pool_tables_arr[choice -1]
        if pool_tables_arr[choice -1].is_occupied == True:
            print(f"Oops! Table number {choice} is not available right now. Please, select another table. ")

        elif chosen_table.is_occupied == False:
            chosen_table.checking_out()
        print(f"Table {chosen_table.tblnumber} is now occupied. ")
        print(f"Start time: {chosen_table.start_time}")
        
            
    if choice == "2":
        display_occupied_tables()
        choice = int(input("Which table would you like to check in? "))
        chosen_table = pool_tables_arr[choice -1]
        chosen_table.checking_in() 
        print(f"Total time checked out: {chosen_table.total_time.total_seconds()/60}")
        print(f"Table {chosen_table.tblnumber} is now available. ")
        save_to_file()


    

    if choice == "3":
        display_open_tables()
        
    if choice == "4":
        break
        print("Thank you for using PoolTable Pro!")
        
    