import os 
import termcolor

def Namechecker(name) :
    print(termcolor.colored("[*] Hi Welcome............." , "green"))
    if name == "" :
        print(termcolor.colored("[*] Name is emty!!!!!!!!!!!!","red"))
        os.close()
    elif name == None :
        print(termcolor.colored("[*] Name is None!!!!!!!!!!!!!","red"))
        os.close()
    elif name == int : 
        print(termcolor.colored("[*] Don't enter Number!!!!!!!!!!","red"))
        os.close()
    elif name == list :
        print(termcolor.colored("[*] Don't enter List!!!!!!!!!!!!!","red"))
        os.close()
    elif type(name) == int :
        print(termcolor.colored("[*] Don't enter Number!!!!!!!!!!","red"))
        os.close()
    elif type(name) == list :
        print(termcolor.colored("[*] Don't enter List!!!!!!!!!!!!!","red"))
        os.close()
    elif type(name) == None :
        print(termcolor.colored("[*] Name is None!!!!!!!!!!!!!","red"))
        os.close()
    else :
        print(termcolor.colored("[*] " + name + " is Corect........" , "green"))
        print("\n")
        
        
        
        