import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout= [[label], [input_box, add_button]])
# [] means one single row, [[c],[a,b]] will have c in first row and a & b in 2nd row
window.read()
window.close()