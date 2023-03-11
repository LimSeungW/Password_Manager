import functions as func
from tkinter import *
from PIL import Image, ImageTk
import os
import tkinter.messagebox as msgbox
from functools import partial

def Get_Icons(filename,x_size, y_size):
    """
    this func is get filname, and then return image
    @parameter filename, x size, y size
    @return img
    """
    Path = f'./icons/{filename}.png'
    img  = Image.open(Path)
    img =  img.resize((x_size,y_size))
    img =  ImageTk.PhotoImage(img)
    return img

def Change_entry_state(Entry, var):
    """
    this func is change the entry state.
    if var is enable, entry is enable too.
    @parameter Entry(tkinter.entry), var (connect variable)
    """
    if(var.get() == 1):
        Entry.config(state="normal")
    else:
        Entry.config(state="disabled")

def main(jsons):
    #수정)paramter에 json 추가해야함
    
    decode_ID = ''.join(func.decryption(jsons[0]['id'], str(int(jsons[0]['code']/3))))
    decode_PW =''.join(func.decryption(jsons[0]['pw'], str(int(jsons[0]['code']/3))))
    decode_CODE = int(jsons[0]['code'])//3
    # decode_name  = func.decryption(jsons[0]['name'], str(int(jsons[0]['code']/3)))

    pg = Tk()
    pg.title("Password Manager")
    pg.wm_iconphoto(False,PhotoImage(file = "./icons/key-chain.png"))
    Screen_width , Screen_height = func.Calc_Screen_Size(pg)
    #GUI size is 500 x 350
    pg.geometry(f"500x350+{int((Screen_width - 500) /2)}+{int((Screen_height - 350 )/2)}")
    back_color = "#65A8E1"
    pg['bg'] = back_color

    fonts = func.Font()
    #icons[0] = setting icon
    icons = []
    icons.append(Get_Icons("setting", 30,30)) #setting
    icons.append(Get_Icons("search",27,27)) #search
    icons.append(Get_Icons("save",27,27)) #save


    # CODE  = str(int(jsons[0]['code'])/3)
    blank = Frame(pg,width = 15,bg = back_color) #this is just blank frame (using margin left)
    blank.pack(side=LEFT, fill=Y)

    def get_list():
        """
        read json and return names decryption
        @return list(str) 
        """
        list_name = []
        for i  in range(0, int(jsons[-1]['index']+1)):
            list_name.append(''.join(func.decryption(jsons[i]['name'], str(int(jsons[0]['code']/3)))))
        return list_name

    def update_list(list):
        """
        update the list 
        @parameter list(listbox) , names(list(str))
        """
        names = get_list()
        list.delete(0,END)
        for name in names:
            list.insert(END, name)

    list = Listbox(pg, relief="solid", bd=1, takefocus= True)
    update_list(list)
    list.pack(side= LEFT, pady = 20,fill= Y)
    
    scroll = Scrollbar(pg, orient="vertical", command= list.yview)
    scroll.pack(side = LEFT, pady = 20,fill= Y)

   

    #setting icons . 
    def setting_GUI():
        """
        show setting menu GUI.
        this menu include delete the All data, or change the user ID, PW or CODE
        """
        set = Toplevel(pg)
        set.title("SETTING")
        set.resizable(False,False)
        set.wm_iconphoto(False,PhotoImage(file = "./icons/key-chain.png"))
        #GUI size is 300 x 200
        set.geometry(f"300x200+{int((Screen_width - 300) /2)}+{int((Screen_height - 200 )/2)}")
        set['bg'] = 'white'


        #delete data button 
        def Delete_All_data():
            """
            Delete all data button event handler
            """
            warning = msgbox.askquestion("Warning", "Are you sure you want to delete the all of data? ")
            if(warning == 'yes'): #if answer is yes , delete the all data
                if os.path.isfile('./data.json'):
                    os.remove('./data.json')  
                else :
                    msgbox.showerror("Error", "The data isn't exists")

        delete_btn = Button(set, text= "Delete All data", bg = "white", relief="solid", bd = 2
            , font=fonts[0], command= Delete_All_data)
        delete_btn.pack(pady=5)
        
        def Edit_data():
            new = Toplevel(set)
            new.title("Edit User Data")
            new.resizable(False,False)
            new.wm_iconphoto(False,PhotoImage(file = "./icons/key-chain.png"))
            new.geometry(f"200x180+{int((Screen_width - 200) /2)}+{int((Screen_height - 180 )/2)}")
            new['bg'] = 'white'

            ID_Frame= Frame(new, width =180  , height= 50 ,  bg="white")
            ID_Frame.pack(pady=3,fill=X)
            #ID Entry
            ID_StrVar = StringVar()
            ID_Entry = Entry(ID_Frame, textvariable=ID_StrVar, relief="solid", bd = 1)
            ID_Entry.insert(0,decode_ID)  ###수정)여기 바꾸고
            ID_Entry.config(state="disabled")
            #ID Checkbox
            ID_Check_var = IntVar()
            ID_Check = Checkbutton(ID_Frame, variable= ID_Check_var, bg = 'white'
                ,command = partial(Change_entry_state,ID_Entry, ID_Check_var))
            ID_Check.pack(side = LEFT ,anchor=NW)
            #ID text 
            ID_label = Label ( ID_Frame, text = "ID", bg = 'white', font=fonts[1])
            ID_label.pack(side = LEFT)
            ID_Entry.pack()
            
            PW_Frame= Frame(new, width =180  , height= 50 ,  bg="white")
            PW_Frame.pack(pady=3,fill=X)
            #PW Entry
            PW_StrVar = StringVar()
            PW_Entry = Entry(PW_Frame, relief="solid", bd = 1, textvariable=PW_StrVar)
            PW_Entry.insert(0,decode_PW)  ###수정)여기 바꾸고
            PW_Entry.config(state="disabled")
            #PW Checkbox
            PW_Check_var = IntVar()
            PW_Check = Checkbutton(PW_Frame, variable= PW_Check_var, bg = 'white'
                ,command = partial(Change_entry_state,PW_Entry, PW_Check_var))
            PW_Check.pack(side = LEFT ,anchor=NW)
            #PW text 
            PW_label = Label ( PW_Frame, text = "PW", bg = 'white', font=fonts[0])
            PW_label.pack(side = LEFT)
            PW_Entry.pack()

            CD_Frame= Frame(new, width =180  , height= 50 ,  bg="white")
            CD_Frame.pack(pady=3,fill=X)
            #CD Entry
            CD_StrVar = StringVar()
            CD_Entry = Entry(CD_Frame, relief="solid", bd = 1, textvariable=CD_StrVar)
            CD_Entry.insert(0,decode_CODE)  
            CD_Entry.config(state="disabled")
            #PW Checkbox
            CD_Check_var = IntVar()
            CD_Check = Checkbutton(CD_Frame, variable= CD_Check_var, bg = 'white'
                ,command = partial(Change_entry_state,CD_Entry, CD_Check_var))
            CD_Check.pack(side = LEFT ,anchor=NW)
            #CD text 
            CD_label = Label(CD_Frame, text = "CODE", bg = 'white', font=fonts[0])
            CD_label.pack(side = LEFT)
            CD_Entry.pack()
            
            def complete(ID_var, PW_var, Code_var):
                """
                complete button event handler
                @parameter ID_var(Entry textvariable) , PW_var(Entry textvariable), Code_var((Entry textvariable))
                """
                jsons[0]['id'] = func.encryption(ID_var.get(), Code_var.get())
                jsons[0]['pw'] = func.encryption(PW_var.get(), Code_var.get())
                jsons[0]['code'] = int(int(Code_var.get())*3)
                
                msgbox.showinfo("Done", "Change data is successfull, Please restart the program")
                func.Save_Json(jsons)
                # print(func.decryption(jsons[0]['id'], str(int(jsons[0]['code']/3))))
                # print(func.decryption(jsons[0]['pw'], str(int(jsons[0]['code']/3))))
                new.destroy()
            complete_btn = Button(new, text= "complete", font=fonts[0], bg= "white", relief="solid",bd= 1)
            complete_btn['command'] = partial(complete,ID_StrVar,PW_StrVar,CD_StrVar)
            complete_btn.pack(side=BOTTOM, pady=10)


            new.mainloop()

        edit_btn = Button(set, text = "Edit user data",  bg = "white", relief="solid", bd = 2
            , font=fonts[0], command= Edit_data)
        edit_btn.pack(pady=5)

        set.mainloop()
    #https://www.flaticon.com/
    setting_btn = Button(pg, image= icons[0],background=back_color, relief="flat",bd =0)
    setting_btn['command'] = setting_GUI
    setting_btn.pack(side = RIGHT, anchor=NE)

    # Main Frame
    Input_Frame = Frame(pg, width = 200, height= 250, bg= "white",relief="solid",bd= 1)
    Input_Frame.pack(pady=20)

    Left_frame = Frame(Input_Frame ,bg= "white",relief="solid",bd= 1)
    Left_frame.pack(side=LEFT)

    Left_Labels=[] #label list
    font_size = 1 #fonts index number
    Left_Labels.append(Label(Left_frame,bg="white", text = "NAME", font = fonts[font_size]))
    Left_Labels.append(Label(Left_frame, bg="white",text = "ID", font = fonts[font_size]))
    Left_Labels.append(Label(Left_frame, bg="white",text = "PW", font = fonts[font_size]))
    for i in Left_Labels:
        i.pack(pady = 3)

    
    Right_frame = Frame(Input_Frame ,bg= "white",relief="solid",bd= 1)
    Right_frame.pack(side=LEFT, fill= Y)
    Right_var = [] #Entry StringVariables
    Right_var.append(StringVar()) #NAME
    Right_var.append(StringVar()) #ID
    Right_var.append(StringVar()) #PW

    Right_Entrys = [] #Entries
    Right_Entrys.append(Entry(Right_frame, bg= "white", relief="solid", bd= 2 ))
    Right_Entrys.append(Entry(Right_frame, bg= "white", relief="solid", bd= 2))
    Right_Entrys.append(Entry(Right_frame, bg= "white", relief="solid", bd= 2))
    
    for i in range(3):
        Right_Entrys[i]['textvariable'] = Right_var[i]
        Right_Entrys[i].pack(pady = 6)


    Button_frame = Frame(pg,bg= "white",relief="solid",bd= 1)
    Button_frame.pack(pady=10)
    
    #functions
    #ADD
    def add_data(text_var):
        """
        add the data to the listbox, and edit the json file.
        @parameter text_var(list(String var))
        """
        position = jsons[-1]['index'] + 1 
        for var in text_var: #check the black. if value is blank. occur error
            if(var.get() == ''):
                msgbox.showerror("error","Please fill the blank")
                return
        jsons.append({
            "index":position,
            "id": func.encryption(text_var[1].get(), str(int(decode_CODE))),
            "pw": func.encryption(text_var[2].get(), str(int(decode_CODE))),
            "code":int(decode_CODE)*3,
            "name":func.encryption(text_var[0].get(), str(int(decode_CODE)))
        })
        func.Save_Json(jsons)
        update_list(list)
    Add_Btn = Button(Button_frame, text = "Add", font= fonts[1], bg = "white")
    Add_Btn['command'] = partial(add_data, Right_var)
    Add_Btn.pack(side =LEFT)

    #Delete
    def delete_item():
        """
        delete the item and save the json file
        """
        warning = msgbox.askquestion("Warning", f"Are you sure you want to delete the data? ")
        if(warning == 'yes'): #if answer is yes , delete the all data
            del jsons[list.curselection()[0]] #delete json list
            #and then,  adjust the index
            for i in range(list.curselection()[0], jsons[-1]['index']):
                jsons[i]['index'] = jsons[i]['index']  - 1
            print(jsons[-1])
            func.Save_Json(jsons)
            update_list(list)

    Delete_Btn = Button(Button_frame, text = "Delete",font= fonts[1], bg = "white", command= delete_item)
    Delete_Btn.pack(side =LEFT, padx=3)

    #Search
    
    global idx
    idx = -1
    def Search_data():
        """
        Search button event handler
        """
        global idx
        idx = list.curselection()[0]
        for Right_Entry in Right_Entrys:# clear the entry
            Right_Entry.delete(0,END)
        Right_Entrys[0].insert(0,''.join(func.decryption(jsons[idx]['name'], str(int((jsons[0]['code']/3))))))
        Right_Entrys[1].insert(0,''.join(func.decryption(jsons[idx]['id'], str(int((jsons[0]['code']/3))))))
        Right_Entrys[2].insert(0,''.join(func.decryption(jsons[idx]['pw'], str(int((jsons[0]['code']/3))))))
    Search_Btn = Button(Button_frame, image = icons[1], bg ="white", command=Search_data)
    Search_Btn.pack(side =LEFT, padx=3)
    
    #save
    def Edit_before_Save():
        """
        save button event hander
        """
        jsons[idx]['name'] = func.encryption(Right_var[0].get(), str(int(decode_CODE)))
        jsons[idx]['id'] = func.encryption(Right_var[1].get(), str(int(decode_CODE)))
        jsons[idx]['pw'] = func.encryption(Right_var[2].get(), str(int(decode_CODE)))
        
        msgbox.showinfo("Save Done", "Save data is successfull")
        func.Save_Json(jsons)
    Save_Btn = Button(Button_frame, image = icons[2], bg ="white",command=Edit_before_Save)
    Save_Btn.pack(side =LEFT, padx=3)
    pg.mainloop()
