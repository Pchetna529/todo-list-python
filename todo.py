import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\nKoi task nahi hai!\n")
        return
    print("\n--- Tumhari Task List ---")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['title']} [{status}]")
    print()

def add_task(tasks):
    title = input("Task ka naam likho: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task add ho gaya!\n")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Kaunsa task complete hua? Number daalo: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Task complete mark ho gaya!\n")
    except (ValueError, IndexError):
        print("Galat number daala!\n")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Kaunsa task delete karna hai? Number daalo: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"'{removed['title']}' delete ho gaya!\n")
    except (ValueError, IndexError):
        print("Galat number daala!\n")

def main():
    tasks = load_tasks()
    while True:
        print("1. Task dekho")
        print("2. Naya task add karo")
        print("3. Task complete mark karo")
        print("4. Task delete karo")
        print("5. Exit")
        choice = input("Option chuno (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Sahi option chuno!\n")

if __name__ == "__main__":
    main()
