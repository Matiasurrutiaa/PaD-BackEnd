import re 

def validar_palabra(palabra):
    if re.search("^[a-z0-9]+$",palabra):
        return palabra
    else:
        return ""
    
    