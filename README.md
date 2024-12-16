# 📝 To-Do List App

Welcome to the **To-Do List App**, a simple yet powerful application built with Python to help you stay organized and productive! This repository includes both a Command-Line Interface (CLI) and a Graphical User Interface (GUI) version of the app, so you can use it in the way that suits you best. 🚀

---

## 🎯 Features

### CLI Version
- **Add To-Dos**: Easily add new tasks to your list.
- **Show To-Dos**: View your current list of tasks in a neatly formatted way.
- **Edit Tasks**: Modify tasks by their index.
- **Mark as Complete**: Remove tasks from your list when completed.
- **Save Progress**: Automatically saves your tasks to a text file.

### GUI Version
- **User-Friendly Interface**: Manage your tasks using an intuitive and visually appealing design.
- **Real-Time Clock**: Displays the current date and time in the app.
- **Interactive Buttons**: Add, edit, and complete tasks with a single click.
- **Persistent Storage**: Saves tasks to a text file for future use.
- **Standalone EXE**: A pre-compiled executable version is included for convenience.

---

### Repository Structure
```
📂 todolist-app
├── cli.py               # CLI-based To-Do app
├── gui.py               # GUI-based To-Do app
├── functions.py         # Shared functions for handling tasks
├── todos.txt            # Text file to store tasks
├── dist/                # Contains the standalone GUI EXE
├── README.md            # Project documentation
```

## 🚀 How It Works

### CLI Workflow
1. **Add tasks**: Type `add` followed by your task (e.g., `add Buy groceries`).
2. **View tasks**: Type `show` to display your to-do list.
3. **Edit tasks**: Type `edit <task_number>` and provide the updated task.
4. **Complete tasks**: Type `complete <task_number>` to remove a task.
5. **Exit**: Type `exit` to close the app.

### GUI Workflow
1. Enter your task in the input box and click **Add**.
2. Select a task from the list and click **Edit** to modify it.
3. Click **Complete** to mark a task as done and remove it.
4. Click **Exit** to close the app.

---

---

## 📝 Notes
- Ensure that `todos.txt` exists in the project folder. The app will create the file if it doesn't exist.
- The standalone EXE is available in the `dist/` folder for users without Python installed.

---

## 🤝 Acknowledgments
Special thanks to the Python and PySimpleGUI communities for their amazing support and resources! 💖

---

## 📧 Contact
Feel free to reach out via GitHub Issues if you have any questions or feedback! 😄
