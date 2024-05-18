import os
TO_DO_LIST="list.txt"

def load_list():
    list = {}
    if os.path.exists(TO_DO_LIST):
        with open (TO_DO_LIST, 'r') as file:
            for line in file:
                name, time, date = line.strip().split(',')
                list[name] = {'time': time, 'date' : date}
    return list

def save_list(list):
    with open(TO_DO_LIST, 'w') as file:
        for name, info in list.items():
            file.write(f"{name},{info['time']},{info['date']}\n")


def add_task(list):
    name = input("Enter the name of the task")
    time = input("Enter the time of which this task should be started, using an 00:00 format")
    date = input("Enter the date this task is meant to be completed, using a m/d/yyyy")
    list[name] = {'time': time, 'date' : date}
    save_list(list)
    print("Task added successfully")

def remove_task(list):
    name = input("Enter the name of the task to remove")
    if name in list:
        del list[name]
        save_list(list)
        print("Task removed successfully")
    else:
        print("Task not found")

def search_list(list):
    name = input("Enter the name of the task to search")
    if name in list:
        print(f"name: {name}")
        print(f"time: {time}")
        print(f"date: {date}")
    else:
        print("Task not found")

def list_tasks(list):
    if not list:
        print("No tasks found")
    else:
        print("\n--->> > > > > > Tasks < < < < < <<--- \n")
        for name, info in list.items():
            print(f"Name: {name} ---- Time: {time} ---= Date: {date} ")
            print('___________________________________________')
def main():
    list = load_list
    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Search Task")
        print("4. List All Contacts")
        print("5. Exit")
        choice = input("Enter an option: ")
        if choice == "1":
            add_task(list)
        elif choice == "2":
            remove_task(list)
        elif choice == "3":
            search_list(list)
        elif choice == "4":
            list_tasks(list):
        elif choice == "5":
            break
        else:
            print("Invalid Option, try again.")

if __name__=="__main__":
    main()
        
