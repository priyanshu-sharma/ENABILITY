import pyttsx3
engine = pyttsx3.init()
matrix = [[1,-1,-1,-1,-1,-1], [1,1,-1,-1,-1,-1], [1,-1,-1,1,-1,-1], [1,-1,-1,1,1,-1], [1,-1,-1,-1,1,-1], [1,1,-1,1,-1,-1],[1,1,-1,1,1,-1],
          [1,1,-1,-1,1,-1],[-1,1,-1,1,-1,-1],[-1,1,-1,1,1,-1], [1,-1,1,-1,-1,-1], [1,1,1,-1,-1,-1], [1,-1,1,1,-1,-1], [1,-1,1,1,1,-1], [1,-1,1,-1,1,-1],
          [1,1,1,1,-1,-1], [1,1,1,1,1,-1], [1,1,1,-1,1,-1], [-1,1,1,1,-1,-1], [-1,1,1,1,1,-1], [1,-1,1,-1,-1,1], [1,1,1,-1,-1,1], [-1,1,-1,1,1,1], [1,-1,1,1,-1,1],
          [1,-1,1,1,1,1], [1,-1,1,-1,1,1], [-1,1,-1,-1,-1,-1], [-1,1,1,-1,-1,-1], [-1,1,-1,-1,1,-1], [-1,1,-1,-1,1,1], [-1,1,1,-1,1,-1], [-1,1,1,-1,1,1],
          [-1,1,1,-1,-1,1], [-1,-1,1,-1,1,-1], [-1,-1,1,-1,1,1], [-1,-1,1,-1,-1,-1], [-1,-1,1,-1,-1,1] , [-1,-1,-1,-1,-1,1] , [-1,-1,1,1,1,1] , [-1,-1,-1,-1,1,1],
          [1,1,1,1,-1,1], [1,1,1,1,1,1], [1,1,1,-1,1,1], [-1,1,1,1,-1,1], [-1,1,1,1,1,1], [1,-1,-1,-1,-1,1], [1,1,-1,-1,-1,1], [1,-1,-1,1,-1,1], [1,-1,-1,1,1,1],
          [1,-1,-1,-1,1,1], [1,1,-1,1,-1,1], [1,1,-1,1,1,1], [1,1,-1,-1,1,1], [-1,1,-1,1,-1,1], [-1,1,-1,-1,-1,1], [-1,-1,1,1,-1,-1], [-1,-1,1,1,-1,1], [-1,-1,1,1,1,-1]]

data = {0:['a','1'], 1:['b','2'], 2:['c','3'], 3:['d','4'], 4:['e','5'], 5:['f','6'], 6:['g','7'], 7:['h','8'], 8:['i','9'], 9:['j','0'], 10:['k'],
        11:['l'], 12:['m'], 13:['n'], 14:['o'], 15:['p'], 16:['q'], 17:['r'], 18:['s'], 19:['t'], 20:['u'], 21:['v'], 22:['w'], 23:['x'], 24:['y'], 25:['z'],
        26:[','], 27:[';'], 28:[':'], 29:['.'], 30:['!'], 31:['(',')'], 32:['?','"'], 33:['*'], 34:['"'], 35:["'"], 36:['-']}

abb = {0:['a'], 1:['but'], 2:['can'], 3:['do'], 4:['every'], 5:['from'], 6:['go'], 7:['have'], 9:['just'], 10:['knowledge'],
        11:['like'], 12:['more'], 13:['not'], 15:['people'], 16:['quite'], 17:['rather'], 18:['so'], 19:['that'], 20:['us'], 21:['very'], 22:['will'], 23:['it'],
        24:['you'], 25:['as'], 27:['bb'], 28:['cc'], 29:['dd'], 31:['gg','were'], 33:['in'], 40:['and'], 41:['for'], 42:['of'], 43:['the'], 44:['with'], 45:['child','ch'],
        46:['g','h'], 47:['shall','sh'], 48:['this','th'], 49:['which','wh'], 50:['ed'], 51:['er'], 52:['out','ou'], 53:['ow'], 54:['en'], 55:['st'], 56:['ing'], 57:['ar']}

speak = {26:['comma'], 27:['semicolon'], 28:['colon'], 29:['full stop'], 30:['exclamation mark'], 31:['open bracket','close bracket'], 32:['question mark','opening quotation mark'],
         33:['asterisk'], 34:['closing quotation mark'], 35:["apostrophe"], 36:['hyphen']}

m = len(matrix)
#print(m)
n = len(matrix[0])
#print(n)

#Resultant String
a = ""

#constants
letter = 1
capital = 0
number = 0
ch = []
count = 0

engine.say("Welcome to Braille Grade 2 system")
engine.runAndWait()
engine.say("This system converts from Braille to text")
engine.runAndWait()
engine.say("Right Now letter mode is enable but for disbling it enter the Braille Code for it")
engine.runAndWait()
engine.say("Capital letter and Number mode is disable but for enabling it enter the Braille Code for it")
engine.runAndWait()

for j in range(0,20):
    engine.say("Enter The Braille Code")
    engine.runAndWait()
    print("Enter The Braille Code :")
    l = []          #input
    for i in range(0,n):
        x = int(input())
        l.append(x)

    for i in range(0,n):
        print(l[i])

    for i in range(0,m):
        if(matrix[i]==l):
            if(i==37):
                if(capital==0):
                    engine.say("Capital Letter Mode Enable")
                    engine.runAndWait()
                    print("Capital Letter Mode Enable")
                    capital=1
                    
                elif(capital==1):
                    engine.say("Small Letter Mode Enable")
                    engine.runAndWait()
                    print("Small Letter Mode Enable")
                    capital=0
                    

            elif(i==38):
                
                if(number==0):
                    engine.say("Number Mode Enable")
                    engine.runAndWait()
                    print("Number Mode Enable")
                    number=1
                    
                elif(number==1):
                    engine.say("Number Mode Disable")
                    engine.runAndWait()
                    print("Number Mode Disable")
                    number=0


            elif(i==39):
                
                if(letter==0):
                    engine.say("Letter Mode Enable and Abbreviation Mode off")
                    engine.runAndWait()
                    print("Letter Mode Enable and Abbreviation Mode off")
                    letter=1
                    
                elif(letter==1):
                    engine.say("Letter Mode Disable and Abbreviation Mode on")
                    engine.runAndWait()
                    print("Letter Mode Disable and Abbreviation Mode on")
                    letter=0
                    
                
            elif(i>-1 and i<26 and letter==1):
                
                if(capital==1 and number==0):
                    b = data[i][0]
                    c = ord(b)
                    b = chr(c-32)
                    
                elif(capital==0 and number==0):
                    b = data[i][0]

                elif(number==1 and i>-1 and i<10): 
                    b = data[i][1]
        
                a = a+b
                engine.say("Entered Braille Code is for the word: "+b)
                engine.runAndWait()
                print("Entered Braille Code is for the word: "+b)

            elif(i>25 and i<37 and letter==1):
                k = len(data[i])
                
                if(k==1):
                    spk = 0
                    b = data[i][0]
                    
                elif(k==2):
                    engine.say("You have two choices")
                    engine.runAndWait()
                    engine.say("First one is "+speak[i][0])
                    engine.runAndWait()
                    engine.say("Second one is "+speak[i][1])
                    engine.runAndWait()
                    engine.say("Enter 1 in Braille for first option and 2 in Braille for second option")
                    engine.runAndWait()
                    print("You have two choices : ")
                    engine.say("Enter The Braille Code for the choice that you have made")
                    engine.runAndWait()
                    print("Enter The Braille Code for the choice that you have made :")
                    for r in range(0,n):
                        inp = int(input())
                        ch.append(inp)

                    if(matrix[0]==ch):
                        spk = 0
                        b = data[i][0]
                        
                    elif(matrix[1]==ch):
                        spk = 1
                        b = data[i][1]

                engine.say("Entered Braille Code is for the word: "+speak[i][spk])
                engine.runAndWait()
                print("Entered Braille Code is for the word: "+b)
                a = a+b
                ch.clear()
                    
                
            elif(letter==0):
                k = len(abb[i])  
                if(k==1):
                    b = abb[i][0]
                    
                elif(k==2):
                    engine.say("You have two choices")
                    engine.runAndWait()
                    engine.say("First one is "+abb[i][0])
                    engine.runAndWait()
                    engine.say("Second one is "+abb[i][1])
                    engine.runAndWait()
                    engine.say("Enter 1 in Braille for first option and 2 in Braille for second option")
                    engine.runAndWait()
                    print("You have two choices : ")
                    engine.say("Enter The Braille Code for the choice that you have made")
                    engine.runAndWait()
                    print("Enter The Braille Code for the choice that you have made :")
                    for r in range(0,n):
                        inp = int(input())
                        ch.append(inp)

                    if(matrix[0]==ch):
                        b = abb[i][0]
                        
                    elif(matrix[1]==ch):
                        b = abb[i][1]
                        
                engine.say("Entered Braille Code is for the word: "+b)
                engine.runAndWait()
                print("Entered Braille Code is for the word: "+b)
                a = a+b
                ch.clear()

            engine.say("Sentence : "+a)
            engine.runAndWait()
            print("Sentence : "+a)
            #print(a)
        else:
            count = count+1
            #print(count)

    if(count==m):
        engine.say("Wrong Braille Code")
        engine.runAndWait()
        print("Wrong Braille Code")
        
    l.clear()

