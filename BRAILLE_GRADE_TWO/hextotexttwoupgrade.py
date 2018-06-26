alphahexcode = {'210':'a', '230':'b', '218':'c', '21c':'d', '214':'e', '238':'f', '23c':'g', '234':'h', '228':'i', '22c':'j',
                '250':'k', '270':'l', '258':'m', '25c':'n', '254':'o', '278':'p', '27c':'q', '274':'r', '268':'s', '26c':'t',
                '252':'u', '272':'v', '22e':'w', '25a':'x', '25e':'y', '256':'z'}

numberhexcode = {'210':'1', '230':'2','218':'3','21c':'4', '214':'5', '238':'6', '23c':'7', '234':'8', '228':'9', '22c':'0'}

specialhexcode = {'226':'.', '220':',', '260':';', '224':':', '264':'!', '262':'?', '240':'\'', '242':'-'}

specialhexcodetwo = {'262':'"', '246':'"', '232':'(', '24c':')', '248':'/', '244':'*', '300':' ', '280':'\n'}

abbhexcode = {'210':'a', '230':'but', '218':'can', '21c':'do', '214':'every', '238':'from', '23c':'go', '234':'have', '228':'i', '22c':'just',
                '250':'knowledge', '270':'like', '258':'more', '25c':'not', '254':'o', '278':'people', '27c':'quite', '274':'rather', '268':'so', '26c':'that',
                '252':'us', '272':'very', '22e':'will', '25a':'it', '25e':'you', '256':'as', '260':'bb', '224':'cc' , '226':'dd', '264':'ff',
                '24c':'ar', '248':'st', '246':'by', '244':'in', '242':'com', '232':'gh', '220':'ea'}

extrahexcode = {'212':'ch', '216':'wh', '21a':'sh', '21e':'th', '222':'en', '22a':'ow', '236':'ou', '23a':'ed', '23e':'er', '24a':'ing', '26a':'the', '26e':'with',
                '276':'of', '27a':'and', '27e':'for', '266':'gg'}

'''hexcode = ['202','216','212','300','24e','210','230','236','202','202','21e','266','222','300','23e']'''

hexcode = ['20c','262','202','22e','234','210','26c','300','228','268','300','210','300','26c','210','250','214','25c','254','26c',
           '214','262','300','202','22e','228','270','270','300','254','252','274','300','300','268','254','274','300','230','214',
           '300','230','214','25c','228','238','228','26c','26c','214','21c','300','236','228','26c','234','300','26c','234','228',
           '268','300','26c','214','218','234','25c','254','270','254','23c','25e','264','280','20c','262','202','26c','210','250',
           '214','25c','254','26c','214','300','204','232','22e','254','274','250','268','300','254','25c','300','26c','234','214',
           '300','278','274','228','25c','218','228','278','270','214','300','254','238','300','230','27c','201','274','210','228',
           '270','270','210','201','214','300','27c','201','278','274','228','25c','26c','228','25c','23c','204','24c','300','228',
           '268','300','210','300','218','254','258','278','210','218','26c','220','300','214','210','264','201','268','25e','300',
           '26c','254','300','234','210','25c','270','201','21c','270','214','300','25c','254','26c','214','300','26c','210','250',
           '214','274','300','268','278','214','218','228','210','270','270','25e','300','300','238','254','274','300','278','214',
           '254','278','270','214','300','21e','228','26c','234','300','272','228','268','228','254','25c','300','228','258','278',
           '210','228','27c','258','214','25c','26c','300','26c','254','300','26c','210','250','214',
           '268','300','25c','254','26c','214','268','300','254','25c','300','26c','234','214','300','23c','254','20c','246','226',
           '300','202','228','26c','300','234','210','268','300','24e','210','230','300','230','252','26c','26c','254','25c','268',
           '300','210','25c','200','21c','300','24e','230','300','268','270','254','26c','268','220','300','254','25c','214','300',
           '238','254','274','300','26c','234','214','300','202','202','268','21c','300','218','210','274','21c','300','210','25c',
           '21c','300','26c','234','214','300','254','26c','234','214','274','300','238','254','274','300','26c','234','214','300',
           '258','228','218','274','254','300','202','202','252','268','230','226','20c','246','300']


string = ""
capitalcount = 0
numbercount = 0

def add(word):
    file=open("word.txt","a+")
    file.write(word+"\n")

length = len(hexcode)
#print(length)


for i in range(0,length):
    a = hexcode[i]
    #print(a)
    


    if(a=='262' and hexcode[i-1]!='20c'):
        b = '?'
        string = string + b
        #print(b)



    elif(a=='202' and hexcode[i+1]!='202' and hexcode[i-1]!='202'):
        capitalcount = 2
        mode = 1



    elif(a=='202' and hexcode[i+1]=='202'):
        capitalcount = 0
        mode = 2
        i = i + 1
        while(hexcode[i]!='300'):
            capitalcount = capitalcount + 1
            i = i + 1
        capitalcount = capitalcount + 1
        #print("capitalcount : "+str(capitalcount))


    elif (a=='206'):
        numbercount = 0


    elif (a=='201'):
        #print("string")
        #print(string)
        string = string[:-1]
        #print(string)


    elif (a=='24e'):
        numbercount = 0
        i = i + 1
        #print(hexcode[i])
        while(hexcode[i]!='300'):
            numbercount = numbercount + 1
            i = i + 1
            #print("Hello")
        numbercount = numbercount + 1
        #print("numbercount : "+str(numbercount))

    
    elif a in specialhexcodetwo:
        b = specialhexcodetwo[a]
        string = string + b
        #print(b)

    elif a in specialhexcode:
        b = specialhexcode[a]
        string = string + b
        #print(b)



    elif (a in numberhexcode and numbercount>0):
        b = numberhexcode[a]
        string = string + b
        #print(b)


    elif (i>0 and i<length-1 and hexcode[i-1]=='300' and hexcode[i+1]=='300'):
        if a in abbhexcode:
            b = abbhexcode[a]  
            string = string + b
            print(b)

    
    elif a in alphahexcode:
        if(numbercount > 0):
            numbercount = 0
        b = alphahexcode[a]
        if(capitalcount>0):
            b = ord(b)
            b = chr(b-32)
        string = string + b
        #print(b)

    elif a in extrahexcode:
        if(numbercount > 0):
            numbercount = 0
        b = extrahexcode[a]
        c = len(b)
        if(capitalcount==1 and mode==1):
            subi = b[0]
            subf = ord(subi)
            subf = chr(subf-32)
            b = b.replace(subi,subf)
            print("SUBi : "+subi)
            print("SUBf : "+subf)
            print("B : "+b)

        elif(capitalcount>0 and mode==2):
            b = b.upper()
            
        string = string + b
        print(b)


    elif(a=='20e' or a=='20c' or a=='204' or (hexcode[i-1]=='202' and a=='202')):
        #print("Here")
        pass

    else:
        #print("Wrong Code")
        pass


    if(capitalcount>0):
            capitalcount = capitalcount - 1

    if(numbercount>0):
            numbercount = numbercount - 1

        
print("String is : ")
print(string)
add(string)

    
