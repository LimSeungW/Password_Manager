import functions as func
from tkinter import *
import account as ac
import Login 
import Program  

def Main():
    """
    Main
    """
    # first, json load. (account.py)
    jsons, json_result = func.Read_Json()
    if(json_result == False):
        #json file is NULL, Create login ID,PW and CODE
        ac.account(jsons)
    
    #second, display the Login GUI (Login.py)
    Login.main(jsons)
    if(func.Login_done == True): # login success.
        Program.main(jsons)



Main()


