tasks = []

def show_menu():
    print("\n📋 Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter new task: ")
        tasks.append(task)
        print("✅ Task added.")

    elif choice == '2':
        if not tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(tasks):
                print(f"{idx + 1}. {task}")

    elif choice == '3':
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Enter updated task: ")
            tasks[index] = new_task
            print("🔁 Task updated.")
        else:
            print("❌ Invalid task number.")

    elif choice == '4':
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("🗑️ Task deleted.")
        else:
            print("❌ Invalid task number.")

    elif choice == '5':
        print("👋 Exiting. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please select 1–5.")
