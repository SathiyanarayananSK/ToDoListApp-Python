import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[label, input_box],[add_button]])

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_td = values["todo"] + "\n"
            todos.append(new_td)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break


window.close()




