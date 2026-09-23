import os
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"✅ Added: '{task}'")

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            print(f"✔️ Marked as done: '{self.tasks[index]['task']}'")
        else:
            print("❌ Invalid task index.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"🗑️ Removed: '{removed['task']}'")
        else:
            print("❌ Invalid task index.")

    def show_tasks(self):
        if not self.tasks:
            print("📭 No tasks yet.")
            return
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(self.tasks):
            status = "✔️" if task["done"] else "⏳"
            print(f"  {i}. {status} {task['task']}")
        print()


def main():
    todo = ToDoList()

    while True:
        print("Options: [1] Add  [2] Done  [3] Remove  [4] Show  [5] Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.show_tasks()
            try:
                idx = int(input("Enter task number to mark done: "))
                todo.mark_done(idx)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "3":
            todo.show_tasks()
            try:
                idx = int(input("Enter task number to remove: "))
                todo.remove_task(idx)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "4":
            todo.show_tasks()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port, debug=False)
