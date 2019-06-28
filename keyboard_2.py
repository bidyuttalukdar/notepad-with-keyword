from tkinter import *
import tkinter
import tkinter.scrolledtext as ScrolledText
import webbrowser
from tkinter import filedialog
from virtual_keyboard import *
import os
########################################################################################################################
# the main keyboard window

Keyboard_App = tkinter.Tk()
Keyboard_App.title("Keyboard")
Keyboard_App.resizable(1,3)

########################################################################################################################
## for the menu of the keyboard

menu=Menu(Keyboard_App)
Keyboard_App.config(menu=menu)

filename = "untitled"
filepath = None

def donothing():
    print("idyut")


def newfile():
    global filename
    filename="Untitled"
    text_box.delete(0.0,END)


def savefile():
    global filename
    if(filename=="untitled"):
        filename = filedialog.asksaveasfilename(filetypes=(('Text Files', '*.txt'), ('All files', '*.*'))) #defaultextension='.txt'
        with open(filename, 'wb') as f:
            t = text_box.get(1.0, "end-1c")
            f.write(bytes(t, 'UTF-16'))
            return "saved"
    elif(filename!="untitled"):
        with open(filename, 'wb') as f:
            t = text_box.get(1.0, "end-1c")
            f.write(bytes(t, 'UTF-16'))
            return "saved"

def savefileas():
    global f
    f=filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    file=open(f,"wb")
    t=text_box.get(1.0, "end-1c")
    file.write(t)
    file.close()
    #print(t)

def openfile():
    global filepath
    filepath = filedialog.askopenfilename()
    if filepath != None and filepath != '':
        with open(filepath, encoding="utf-16") as f:
            fileContents = f.read()
        text_box.delete(1.0, "end")
        text_box.insert(1.0, fileContents)

def renamefile():
    global filename
    refile=filedialog.asksaveasfile(initialdir="/", title="Select file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    os.rename(filename,refile)
def backspacefun():
    #file = open(filename, "wb")
    t = text_box.get(1.0, "end-1c")
    t=t[:-1]
    #file.close()
    keyboard_2.text_box.delete('1.0', END)
    keyboard_2.text_box.insert(tkinter.END, t)
def printfile():
    os.startfile("filepath","print")


newform=2
url="http://google.com"


def feedback_form():
    webbrowser.open(url,new=newform)


submenu=Menu(menu)
editmenu=Menu(menu)
windowsmenu=Menu(menu)
viewmenu=Menu(menu)
formatmenu=Menu(menu)

menu.add_cascade(label="File ",menu=submenu)
submenu.add_command(label="New                        Ctrl+N",command=newfile)
submenu.add_command(label="Open                      Ctrl+O",command=openfile)
submenu.add_command(label="Save                        Ctrl+S",command=savefile)
submenu.add_command(label="Save As",command=savefileas)
submenu.add_command(label="Rename",command=renamefile)
submenu.add_separator()
submenu.add_command(label="Print",command=printfile)
submenu.add_command(label="Exit",command=Keyboard_App.quit)


menu.add_cascade(label="Edit ",menu=editmenu)
editmenu.add_command(label="Copy                         Ctrl+C",command=donothing)
editmenu.add_command(label="Cut                            Ctrl+X",command=donothing)
editmenu.add_command(label="Paste                         Ctrl+V",command=donothing)


menu.add_cascade(label="View ",menu=viewmenu)
viewmenu.add_command(label="Status Bar",command=donothing)

menu.add_cascade(label="Formate ",menu=formatmenu)
formatmenu.add_command(label="Status Bar",command=donothing)


menu.add_cascade(label="Windows",menu=windowsmenu)
windowsmenu.add_command(label="Virtual Keyboard          ",command=virtual_keyboard)
windowsmenu.add_command(label="Feedback us               ",command=feedback_form)

########################################################################################################################
# frames for textbox, numbers, predicted word select buttons, letter buttons, spacebar

#text_box_frame = Frame(Keyboard_App)
#text_box_frame.pack(fill=BOTH)

'''predicted_word_frame = Frame(Keyboard_App)
predicted_word_frame .pack()

number_buttons_frame = Frame(Keyboard_App)
number_buttons_frame.pack()

letter_buttons_frame = Frame(Keyboard_App)
letter_buttons_frame.pack()

spacebar_frame = Frame(Keyboard_App)
spacebar_frame.pack()'''

# the row and column
varRow = 0
varColumn = 0

########################################################################################################################
# the textbox

# text_box = Text(text_box_frame, width=135, height=15, font=('arial'))

text_box = ScrolledText.ScrolledText(Keyboard_App,height=1000, font=('arial'))
text_box.pack(fill=BOTH)
#text_box.focus()
#text_box.update()
#text_box.text.focus()
#text_box.text.update()
#text_box.grid(row = varRow, columnspan = 40,)
#text_box.focus()

varRow += 1

########################################################################################################################
# predicted words

'''predicted_button_list = []

for i in range(0, 5):
    predicted_button_list.append(tkinter.Button(predicted_word_frame, text=i, font='Lohit-Assamese',width=23))
    predicted_button_list[i].grid(row=varRow, column=varColumn)

    varColumn += 1

varRow += 1

########################################################################################################################
# numbers

numrber_list = [
    '১',	 '২', '৩', '৪', '৫', '৬', '৭', ' ৮', '৯', '০'
]

varColumn = 0
for assamese_number in numrber_list:
    command = lambda x= assamese_number: text_box.insert(tkinter.END, x)
    tkinter.Button(number_buttons_frame, text=assamese_number, width=10, command=command).grid(row=varRow, column=varColumn)

    varColumn += 1
varRow += 1

########################################################################################################################
# letter buttons

buttons = [
    'ক', 'খ', 'গ', 'ঘ', 'ঙ',
    'চ', 'ছ', 'জ', 'ঝ', 'ঞ',
    'ট', 'ঠ', 'ড', 'ঢ', 'ণ',
    'ত', 'থ', 'দ', 'ধ', 'ন',
    'প', 'ফ', 'ব', 'ভ', 'ম',
    'য', 'ৰ', 'ল', 'ৱ',
    'শ', 'ষ', 'স', 'হ',
    'ক্ষ', 'ড়', 'ঢ়', 'য়',
    'অ', 'আ', 'ই', 'ঈ',
    'উ', 'ঊ', 'ঋ',
    'এ', 'ঐ', 'ও', 'ঔ',
    'া', 'ি', 'ী',
    'ু', 'ূ', 'ৃ',
    'ে', 'ৈ', 'ো', 'ৌ',
    'ৎ', 'ং', 'ঃ', 'ঁ',
    '।', '্'
]

varColumn = 0
for button in buttons:
    command = lambda x= button: text_box.insert(tkinter.END, x)
    tkinter.Button(letter_buttons_frame, text=button,font='Lohit-Assamese',width=5, command=command).grid(row=varRow, column=varColumn)

    varColumn += 1
    if varColumn > 15:
        varColumn = 0
        varRow += 1

########################################################################################################################
# spacebar

command = lambda x= 'Space': text_box.insert(tkinter.END, ' ')
tkinter.Button(spacebar_frame, text="Space", width = 118, command=command).grid(row=varRow, columnspan=16)
varRow += 1




########################################################################################################################

def buttonCommand(text_box_data):
    text_box.delete('1.0', END)
    text_box.insert(tkinter.END, text_box_data)


def keypress(key):
    text_box_data = text_box.get('1.0', 'end-1c')
    flag = 0
    words = []

    if text_box_data.endswith(' ') or text_box_data == '':
        flag = 0
    else:
        last_word = text_box_data.split()[-1]
        print(last_word)
        words = select_word_from_db.selectWordFromDb(last_word, flag)
        flag = 1
        print(words)

    for button in predicted_button_list:
        button.destroy()

    predicted_button_list.clear()

    if len(words) < 5:
        t = len(words)
    else:
        t = 5

    if flag == 1:
        if text_box_data.find(' ') > -1:
            text_box_data = text_box_data.rsplit(' ', 1)[0]
            initial_flag = 1
        else:
            text_box_data = ''
            initial_flag = 0

        for i in range(0, t):
            if initial_flag == 0:
                word = words[i][0]+' '
            elif initial_flag == 1:
                word = text_box_data+' '+words[i][0]+' '

            command = lambda x=word: buttonCommand(x)
            predicted_button_list.append(tkinter.Button(predicted_word_frame, text=words[i][0],font='Lohit-Assamese', width=23, command=command))
            predicted_button_list[i].grid(row=2, column=i)
    elif flag == 0:
        for i in range(0, 5):
            predicted_button_list.append(tkinter.Button(predicted_word_frame, font='Lohit-Assamese',text=i, width=23))
            predicted_button_list[i].grid(row=2, column=i)



Keyboard_App.bind("<Key>", keypress)
Keyboard_App.bind("<ButtonRelease>", keypress)'''

########################################################################################################################
# the main loop
Keyboard_App.configure(background="red")
Keyboard_App.mainloop()

