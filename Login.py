import functions as func
from tkinter import *
import tkinter.messagebox as msgbox

def main(jsons):
    login = Tk()
    login.title("Password Manager")
    login.wm_iconphoto(False,PhotoImage(file = "./icons/key-chain.png"))
    #Program size is 300x250
    Screen_width , Screen_height = func.Calc_Screen_Size(login)
    login.geometry(f"300x250+{int((Screen_width - 300) /2)}+{int((Screen_height - 250 )/2)}")

    #Program background is white
    login['bg'] = 'white'
    
    fonts = func.Font()
    init_text_label = Label(login, text= "File loaded successfully", bg= "white",font= fonts[1])
    init_text_label.pack(pady=5)
    
    Main_text_label = Label(login, text = "Login", font= fonts[1], bg = "white")
    Main_text_label.pack(pady=5)
    #Login screen 

    user_ID = StringVar()
    user_PW = StringVar()
    
    #Left_frame is group of labels(text)
    Left_frame = Frame(login, bg = "white", width = 90, height= 160)
    Left_frame.pack(side = LEFT, padx= 10,pady= 50)


    ID_Label = Label(Left_frame, font=fonts[1], text = "ID", bg="white")
    PW_Label = Label(Left_frame, font=fonts[1], text = "PW", bg="white")
    ID_Label.pack()
    PW_Label.pack()

    #Right_frame is group of Entry(text box)
    Right_frame = Frame(login , bg = "white", width = 150, height= 160)
    Right_frame.pack(side = LEFT,pady= 50)

    ID_Entry = Entry(Right_frame, textvariable= user_ID, relief="solid",bd=1 )
    PW_Entry = Entry(Right_frame, textvariable= user_PW, show='*', relief="solid",bd=1)
    ID_Entry.pack(pady= 7)
    PW_Entry.pack(pady= 7)

    #Enter Btn
    def Check_user():
        """
        this function is check the input and compare login data.
        if input is right, go to the next step.
        """
        decode_ID =func.decryption(jsons[0]['id'], str(int(jsons[0]['code']/3)))
        decode_PW =func.decryption(jsons[0]['pw'], str(int(jsons[0]['code']/3)))
        # decode_CODE = int(jsons[0]['code'])/3
        # decode_name  = func.decryption(jsons[0]['name'], str(int(jsons[0]['code']/3)))

        if(''.join(decode_ID) == user_ID.get() and ''.join(decode_PW) == user_PW.get()):
            msgbox.showinfo("Login", f"Login successfull, Welcome {user_ID.get()}")
            #login successfull. destroy and deliver login successment to the main
            login.destroy()
            func.Login_done = True
        else:
            msgbox.showerror("Error", "Please, Check the ID or PW")

    Login_btn = Button(login, text= "Enter", bg= "white",  relief="solid", bd= 1,
        width = 10, height= 3, command= Check_user, font= fonts[0])
    Login_btn.pack(side = LEFT, padx= 15)




    login.mainloop()