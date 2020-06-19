
def xnor_operation(text,key):
    list_textbin = []
    for i in text:
        list_textbin.append(str(bin(ord(i))[2:]).rjust(8,"0"))
    print(list_textbin)
    list_keybin = []
    for j in key:
        list_keybin.append(str(bin(ord(j))[2:]).rjust(8,"0"))
    key_fix = (list_keybin*len(list_textbin))[:len(list_textbin)]
    print(key_fix)
    flag = ""
    for i,j in zip(list_textbin,key_fix):
        flag += chr(255-(int(i,2)^int(j,2)))
    return flag
    
        

text = "1NOMAROZI"
key = "Zoro"
print(xnor_operation(text,key))
