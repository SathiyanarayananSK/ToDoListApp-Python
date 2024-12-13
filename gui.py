import functions
import FreeSimpleGUI as gui

label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo")
add_button = gui.Button("Add")
fb = gui.FileBrowse("choose")
fob = gui.FolderBrowse("choose")

window = gui.Window("My To-Do App", layout=[[label, input_box],[add_button, fb, fob]])
window.read()
window.close()




