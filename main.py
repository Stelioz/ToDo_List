
import os
# username = input("Write your username: ")
username = "Stelios"
print(f"Hello {username} to your ToDo List!")

if os.path.isfile("tasks.txt"):
   with open("tasks.txt", "r") as file:
      tasks = file.read().splitlines()
else:
   tasks = []

while True:
    print("- To add new task type: 'Add'")
    print("- To delete a task type: 'Delete'")
    print("- To save the list type: 'Save'")
    print("- To view the list type: 'View'")
    print("- To exit the program type: 'Exit'")
    select = input()
    
    if select == "Add":
      task = input("Give your next task: ")
      tasks.append(task)
    #   time = input(f"{task} starts at: ")
    #   tasks.append(time)
      print("Task added to the list.")
    elif select == "Delete":
       print("\nYour ToDo List")
       print("-------------------------------------")
       i = 1
       for task in tasks:
          print(f"{i}. {task}")
          i = i + 1
       print("-------------------------------------")
       task_index = int(input("Type the number of the task you want to delete: "))
       if task_index <= len(tasks):
          tasks.pop(task_index - 1)
          print("Task deleted from the list.")
       else:
          print("The task is not in the list.")
    elif select == "Save":
        with open("tasks.txt", "w") as file:
          file.write("\n".join(tasks))
        print("List saved!")
    elif select == "View":
       print("\nYour ToDo List")
       print("-------------------------------------")
       i = 1
       for task in tasks:
          print(f"{i}. {task}")
          i = i + 1
       print("-------------------------------------\n")
    elif select == "Exit":
       break
    else:
       print("Command not found!")
print(f"\nGoodbye, {username}")