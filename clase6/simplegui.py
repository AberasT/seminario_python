import PySimpleGUI as sg


layout = [[sg.Input('Ingresa algo')],
[sg.Listbox(values=('Item 1', 'Item 2', 'Item 3'))],
[sg.OK()]]
window = sg.Window("Elementos básicos", layout, margins=(200, 150))
event, values = window.read()

sg.Popup(event, values, line_width=200)
sg.ChangeLookAndFeel('DarkAmber')
layout = [[sg.Listbox(values=('Item 1', 'Item 2', 'Item 3'),background_color='yellow', size=(30,10)),
[sg.Input('Last input')],
[sg.ColorChooserButton(" Elegi color")],
[sg.OK()]]]