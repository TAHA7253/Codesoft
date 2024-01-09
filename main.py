import PySimpleGUI as sg
import random
import pyperclip

# Define the layout of the form
layout = [
    [sg.Text('Name:'), sg.InputText(key='-NAME-')],
    [sg.Text('Password Length:'), sg.InputText(key='-LENGTH-')],
    [sg.Button('Generate Password')],
    [sg.Text('Generated Password:'), sg.InputText(key='-PASSWORD-')],
    [sg.Button('Accept'), sg.Button('Reset')]
]

# Create the window
window = sg.Window('Password Generator', layout)

# Define the password generator function
def password_generator(n):
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special_char = "!@#$%^&*()_+"
    all_asci = upper_case + lower_case + digits + special_char
    password = ""
    for i in range(n):
        password += random.choice(all_asci)
    return password

# Event loop to process "events" and generate the password
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Generate Password':
        name = values['-NAME-']
        length = int(values['-LENGTH-'])
        password = password_generator(length)
        window['-PASSWORD-'].update(password)
    if event == 'Accept':
        pyperclip.copy(password)
    if event == 'Reset':
        window['-PASSWORD-'].update('')

# Close the window
window.close()
