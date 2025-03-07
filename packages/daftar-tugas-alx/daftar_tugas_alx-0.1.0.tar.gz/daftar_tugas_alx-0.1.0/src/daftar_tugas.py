class TaskManager:
    def __init__(self):
        self.tasks = []  # List untuk menyimpan tugas

    def add_task(self, task):
        self.tasks.append(task)
        print(f"✅ Tugas '{task}' ditambahkan!")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"❌ Tugas '{task}' dihapus!")
        else:
            print(f"⚠️ Tugas '{task}' tidak ditemukan.")

    def show_tasks(self):
        if not self.tasks:
            print("📭 Tidak ada tugas.")
        else:
            print("\n📌 Daftar Tugas:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")


manager = TaskManager()
manager.add_task("Belajar Python")
manager.add_task("Makan Siang")
manager.show_tasks()
manager.remove_task("Makan Siang")
manager.show_tasks()
