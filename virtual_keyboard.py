from functools import partial
from tkinter import *
import tkinter
import keyboard_2
#import pyautogui as pyautog
import select_word_from_db
########################################################################################################################
# the main keyboard window
global words
words=[]
global predict
predict=1
def virtual_keyboard():
        virtual_keyboard = tkinter.Tk()
        virtual_keyboard.title("Assamese keyboard")
        virtual_keyboard.configure(background="silver")
        virtual_keyboard.resizable(0,0)

        virtual_keyboard_menu=Menu(virtual_keyboard)
        virtual_keyboard.config(menu=virtual_keyboard_menu)
        virtual_keyboard_menu.config(background="green")

    ########################################################################################################################
    ## for the menu of the virtual keyboard
        thememenu = Menu(virtual_keyboard_menu)
        pedictionmenu = Menu(virtual_keyboard_menu)

        commandoff= lambda x=0: prediction(x)
        commandon= lambda x=1: prediction(x)

        virtual_keyboard_menu.add_cascade(label="Prediction", menu=pedictionmenu)
        pedictionmenu.add_command(label="ON",command=commandon)
        pedictionmenu.add_command(label="OFF",command=commandoff)

        def prediction(value):
            global predict
            predict=value


        ########################################################################################################################
    # frames for textbox, numbers, predicted word select buttons, letter buttons, spacebar

        text_box_frame = Frame(virtual_keyboard)
        text_box_frame.pack()

        predicted_word_frame = Frame(virtual_keyboard)
        predicted_word_frame .pack()

        number_buttons_frame = Frame(virtual_keyboard)
        number_buttons_frame.pack()

        letter_buttons_frame = Frame(virtual_keyboard)
        letter_buttons_frame.pack()

        spacebar_frame = Frame(virtual_keyboard)
        spacebar_frame.pack()

        # the row and column
        varRow = 0
        varColumn = 0

        ########################################################################################################################
        # the textbox

        # text_box = Text(text_box_frame, width=135, height=15, font=('arial'))
        '''text_box = ScrolledText.ScrolledText(text_box_frame, width=133, height=15, font=('arial'))
        text_box.grid(row = varRow, columnspan = 40)
        text_box.focus()

        varRow += 1'''

        #####################################################
        # Auto Correct and Auto Terminate Button

        AutoCorrect_button = Button(text_box_frame, text="Auto Correct",pady=8,bg="#D7FF33",activeforeground="black",activebackground="#B5C9B1",width=50).grid(row=varRow, column=0)
        AutoCorrect_terminate = Button(text_box_frame, text="Auto Terminate",pady=8,bg="#D7FF33",activeforeground="black",activebackground="#B5C9B1", width=50).grid(row=varRow, column=4)

        ########################################################################################################################
        # predicted words

        varRow +=1
        predicted_button_list = []

        for i in range(0, 5):
            predicted_button_list.append(tkinter.Button(predicted_word_frame, text=i, font='Lohit-Assamese',width=10))
            predicted_button_list[i].grid(row=varRow, column=varColumn)

            varColumn += 1

        varRow += 1

        ########################################################################################################################
        # numbers

        numrber_list = [
            '১', '২', '৩', '৪', '৫', '৬', '৭', ' ৮', '৯', '০','backspace'
        ]

        varColumn = 0
        for assamese_number in numrber_list:
            command = lambda x= assamese_number: keyboard_2.text_box.insert(tkinter.END, x)
            if assamese_number != "backspace":
               tkinter.Button(number_buttons_frame, text=assamese_number,padx=5,pady=5,width=6,bg="#D7FF33",activeforeground="black",activebackground="#B5C9B1",command=command).grid(row=varRow, column=varColumn)
            else:
                tkinter.Button(number_buttons_frame, text=assamese_number, padx=5, pady=7, width=12,bg="#FFAF33",fg="black",activeforeground="BLACK",activebackground="RED",command=keyboard_2.backspacefun).grid(row=varRow, column=varColumn)

            varColumn += 1
        varRow += 1
        ########################
        def buttonCommand(text_box_data):

            #print("DATA:")
            #print(text_box_data)
            #list_writen=text_box_data.split(" ")
            keyboard_2.text_box.delete('1.0', END)
            keyboard_2.text_box.insert(tkinter.END, text_box_data)



        def autoButtonCommand(text_box_data, flag):

            data = keyboard_2.text_box.get('1.0', END)
            print("Data:")
            print(data)
            keyboard_2.text_box.delete('1.0', END)
            if flag == 0:
                if len(data) > 1:
                    print("len1")
                    keyboard_2.text_box.insert(tkinter.CURRENT, data[:len(data)-2]+text_box_data)
                elif len(data) == 1:
                    print("len2")
                    keyboard_2.text_box.insert(tkinter.CURRENT, text_box_data)

            elif flag == 1:
                try:
                    index = data.rindex(' ')
                except ValueError:
                    keyboard_2.text_box.insert(tkinter.CURRENT, text_box_data)

                if data.endswith(' '):
                    keyboard_2.text_box.insert(tkinter.CURRENT, data + text_box_data)
                else:
                    try:
                        keyboard_2.text_box.insert(tkinter.CURRENT, data[: index] +' '+text_box_data)
                    except UnboundLocalError:
                        print("Local Error")

        def autoCorrectCommand(word):
            flag=0
            data = keyboard_2.text_box.get('1.0', END)
            if len(data) == 1:
                autoButtonCommand(word,1)
            last_word = data.split()[-1]
            print(last_word)
            words = select_word_from_db.selectWordFromDb(last_word, flag)
            #flag = 1
            print("Length:",end='')
            print(len(words))
            if len(words) == 0:
                autoButtonCommand(word,1)

        def keypress(key):
            text_box_data =  keyboard_2.text_box.get('1.0', 'end-1c')
            flag = 0
            #global words = []

            if text_box_data.endswith(' ') or text_box_data == '':
                flag = 0
            else:
                last_word = text_box_data.split()[-1]
                print(last_word)
                global words
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

            if(predict!=0):
                if flag == 1:
                    if text_box_data.find(' ') > -1:
                        text_box_data = text_box_data.rsplit(' ', 1)[0]
                        initial_flag = 1
                    else:
                        text_box_data = ''
                        initial_flag = 0

                    if words !=[]:
                        for i in range(0, t):
                            if initial_flag == 0:
                                word = words[i][0] + ' '
                            elif initial_flag == 1:
                                word = text_box_data + ' ' + words[i][0] + ' '

                            def autoTerminate(event):
                                # if autoB == 0:
                                autoButtonCommand(words[0][0], 0)

                            def autoCorrect(event):
                                autoCorrectCommand(words[0][0])
                                #   autoB=1

                            virtual_keyboard.bind("<F1>", autoTerminate)

                            virtual_keyboard.bind("<F2>", autoCorrect)
                            command = lambda x=word: buttonCommand(x)
                            predicted_button_list.append(
                                tkinter.Button(predicted_word_frame, text=words[i][0], bg="#E69A0C",
                                               activeforeground="black", activebackground="#B5C9B1",
                                               font='Lohit-Assamese',
                                               width=15, command=command))

                            predicted_button_list[i].grid(row=3, column=i)

                    else:
                        wrong=tkinter.Button(predicted_word_frame, bg="#E69A0C", activeforeground="black",
                                       activebackground="#B5C9B1", font='Lohit-Assamese', text="Your Word is wrong /তোমাৰ বানান  ভুল  হৈছে ",
                                       width=79).grid(row=3)

                elif flag == 0:
                    for i in range(0, 5):
                        predicted_button_list.append(
                            tkinter.Button(predicted_word_frame, bg="#E69A0C", activeforeground="black",
                                           activebackground="#B5C9B1", font='Lohit-Assamese', text=i, width=15))
                        predicted_button_list[i].grid(row=3, column=i)

            else:
                print("yes")

                tkinter.Button(predicted_word_frame, bg="#E69A0C", activeforeground="black",
                               activebackground="#B5C9B1", font='Lohit-Assamese', text="Prediction is off", width=79).grid(
                         row=3)

        virtual_keyboard.bind("<Key>", keypress)
        virtual_keyboard.bind("<ButtonRelease>", keypress)

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
            command = lambda x= button:  keyboard_2.text_box.insert(tkinter.END, x)
            tkinter.Button(letter_buttons_frame, text=button,bg="#ADF5CB",font='Lohit-Assamese',padx=5,pady=3,width=3,foreground="red" ,activeforeground="black",activebackground="#B5C9B1",command=command).grid(row=varRow, column=varColumn)

            varColumn += 1
            if varColumn > 15:
                varColumn = 0
                varRow += 1

        ########################################################################################################################
        # spacebar

        command = lambda x= 'Space':  keyboard_2.text_box.insert(tkinter.END, ' ')
        tkinter.Button(spacebar_frame, text="Space",pady=8,bg="#ADF5CB",foreground="red",activeforeground="black",activebackground="#B5C9B1",width = 102, command=command).grid(row=varRow)
        varRow += 1




        ########################################################################################################################
######Font Menu





        ##############################################################################################################
        # the main loop


        virtual_keyboard.mainloop()


