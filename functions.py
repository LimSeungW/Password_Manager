import json
import tkinter.font as tkFont


Login_done = False

def encryption(sentence, CODE):
    """
    this function will encryption the data.
    the data include id,password
    @parameter input(string), code (string)
    @return list(int)
    """
    def sum_code(CODE):
        """
        This function returns the sum of each digit in the code. 
        """
        sum = 0
        for i in range(0, len(str(CODE))):
            sum += int(CODE[i])
        return (sum - 10 ) * (sum + 10) + sum

    encryption_key = sum_code(CODE)
    result = []
    #ord(char) -> Int 
    
    for i in range(0,len(str(sentence))):
        result.append(ord(sentence[i]) + encryption_key*2)

    return result

def decryption(list, CODE):
    """
    decode the data.
    @parameter list(int), CODE(int)(code must be devide 3 )
    @return list(string)
    """
    
    sum = 0
    for i in range(0, len(str(CODE))):
        sum += int(CODE[i])
    
    result = []
    # chr(Int)-> char
    decryption_key = (sum - 10) * (sum + 10) + sum
    for i in list:
        result.append(chr(i - decryption_key * 2))
    return result

def Font():
    """
    Change text size.
    return array(fonts)
    """
    fonts = []
    fonts.append(tkFont.Font(size=10, weight="bold"))
    fonts.append(tkFont.Font(size=12, weight="bold"))
    fonts.append(tkFont.Font(size=15, weight="bold"))
    fonts.append(tkFont.Font(size=20, weight="bold"))
    return fonts


def Save_Json(json_object):
    """
    Save json file.
    @parameter : json 
    """
    with open("data.json", "w") as json_file:
            json.dump(json_object, json_file)

def Read_Json():
    """
    if json file is exist , return data\n
    else, create json file
    @return json(index (int), id(string), pw(string), code(int),name(string)), bool(true or false)
    """
    try:
        with open('./data.json', "r") as f:
            # 로드 해서 배열 넣기 필요.
            json_object = json.load(f)
            return json_object,True
    except:
        json_object = [{
            "index":0,
            "id": "",
            "pw": "",
            "code":0,
            "name":""
        }]
        return json_object,False


def Calc_Screen_Size(top_root):
    """
    Calculate the Screen size
    @return width, height(double)
    """
    width = top_root.winfo_screenwidth()
    height = top_root.winfo_screenheight()
    return width, height


