from tkinter import *
import functions
import tkinter.messagebox as msgbox


def account(jsons):
    sub = Tk()
    sub.title("Create Account")
    sub.wm_iconphoto(False,PhotoImage(file = "./icons/key-chain.png"))
    width, height = functions.Calc_Screen_Size(sub)
    #sub screen size is 300 x 150
    sub.geometry(f"300x150+{int((width - 300) /2)}+{int((height - 150 )/2)}")
    
    #back ground color is #65A8E1
    back_color = "#65A8E1"
    sub['bg'] = back_color
    fonts = functions.Font()

    #guide message
    message_label = Label(sub, text = "Create an account", bg = back_color, font = fonts[2])
    message_label.pack()

    #text box frame
    Text_Frame = Frame(sub,bg=back_color, 
        width= 200, height= 100)
    Text_Frame.pack(side=LEFT, padx= 10)

    #Label part
    Label_frame = Frame(Text_Frame, width= int(Text_Frame['width']) /4, height= int(Text_Frame['height']), bg= back_color)
    Label_frame.pack(side=LEFT)

    ID_label = Label(Label_frame , bg = back_color, text = "ID", font = fonts[0])
    PW_label = Label(Label_frame , bg = back_color, text = "PW", font = fonts[0])
    Code_label = Label(Label_frame , bg = back_color, text = "CODE", font = fonts[0])

    ID_label.pack(pady=3)
    PW_label.pack(pady=3)
    Code_label.pack(pady=3)

    #This is data of user informations
    user_data = []
    user_data.append(StringVar()) #user_data[0] is ID
    user_data.append(StringVar()) #user_data[1] is PW
    user_data.append(StringVar()) #user_data[2] is CODE, this is only int.

    #Box part
    Box_frame = Frame(Text_Frame, width= (int(Text_Frame['width'])/4)*3, height= int(Text_Frame['height']), 
        bg= back_color)
    Box_frame.pack()

    ID_box = Entry(Box_frame, textvariable=user_data[0], bg = 'white', bd= 1, relief="solid")
    PW_box = Entry(Box_frame , textvariable=user_data[1], bg='white', bd= 1, relief="solid")
    CODE_box = Entry(Box_frame, textvariable=user_data[2], bg= 'white', bd= 1, relief="solid")

    ID_box.grid(row=1,column=1,pady=5)
    PW_box.grid(row=2,column = 1,pady=5)
    CODE_box.grid(row=3 ,column= 1, pady=5)

    def Sign_in():
        """
        When user pressed the Enter btn, this func will start.
        this func is get data from Entry box and then, Check the form of the data ,
        save the data to json file
        """
        try:
            if(int(user_data[2].get()) < 0 or int(user_data[2].get())> 9999):
                #An error occurs when the data format entered by the user is not correct.
                raise Exception

            jsons[0]['id'] = functions.encryption(user_data[0].get(), user_data[2].get())
            jsons[0]['pw'] = functions.encryption(user_data[1].get(), user_data[2].get())
            jsons[0]['code'] = int(user_data[2].get()) * 3 
            jsons[0]['name'] = functions.encryption("login", user_data[2].get())
            functions.Save_Json(jsons)
            msgbox.showinfo("Notice", "Create an account is Successfull")
            sub.destroy()
        except Exception as e:
            print(e)
            msgbox.showerror("Error", "Please enter the correct format.\nCODE is must be Integer(Min:0 ~ MAX:9999)")

    #Enter Button
    Enter_btn = Button(sub,bg='white', bd=2, relief="solid", width=10,height=8, text="ENTER",font=fonts[0])
    Enter_btn['command'] = Sign_in
    Enter_btn.pack(side=RIGHT,padx=10, pady= 30)
    
    sub.mainloop()