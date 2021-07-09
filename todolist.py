#Todo list

tasks = []

while True:
    print("----Todo List----")
    print("1 - Add Task")
    print("2 - Delete Task")
    print("3 - View All Tasks")
    print("4 - Quit")

    choice = int(input("Select an action by entering a number. "))

    if choice == 4:
        break

    if choice == 1:
        title = input("Enter the title of your task here. ")
        priority = input ("Enter the priority of your task here. (High, Medium or Low) ")
        task = {"title": title, "priority": priority}
        tasks.append(task)
       
        print(title + " - " + priority)
    

    if choice == 3:
        print("----Tasks----")
        for i in range(0, len(tasks)):
            print(tasks[i])
        

    
         






