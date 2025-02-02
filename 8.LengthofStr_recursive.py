str="hello"



def str_len(s):
    if s=="":
        return 0
    else:
        return 1+ str_len(s[1:])
    
print(str_len(str))