import autocomplete
import time
autocomplete.load()


is_word=0
is_char=0   

sentence=''
word=''
char=''
take_new_input=''
store=[]
idx=0
space=0


def phrases():
    file=open("word.txt","r")
    contents=file.readlines()
    for x in contents:
        print(x)

def add(word):
    file=open("word.txt","a+")
    file.write(word+"\n")


def undo():
    global sentence
    global space
    if(space==0):
        sentence=''
        main()
    else:
        for i in range(len(sentence)-1,0,-1):
            if(sentence[i]==' '):   
                temp=i
                break;
        sentence=sentence[:temp+1]
        main()

def erase():
    global sentence
    sentence=''
    main()

def word_prediction(keyword1,keyword2):   #word prediction
    global is_word
    global is_char
    global is_first_char
    global sentence
    global word
    global char
    global take_new_input
    global store
    global idx
    global space

    store=autocomplete.predict(keyword1,keyword2)
    if(idx==0):
        store=store[0:3]
    elif(idx>0):
        store=store[idx*3:(idx+1)*3]    
        
    if(len(store)==0):
                print("word 1:"+keyword1)
    else:
            print("word 1 : "+keyword1+keyword2)
            k=2
            for keys in store:
                print("word {} : {}".format(k,keys[0]))
                k=k+1       
    print("select word")
    if(len(store)>=3):
        print("select 5 for more words")
        
    select=int(input())
#    word_prediction_part_two(select)

#def word_prediction_part_two(select):
    if(select==1):
            word=keyword1
            is_char=1
            is_word=0
            idx=0
    elif(select==2):
            word=store[0][0]
            keyword1=word
            is_char=0
            is_word=1
            idx=0
    elif(select==3):
            word=store[1][0]
            keyword1=word
            is_char=0
            is_word=1
            idx=0
    elif(select==4):
            word=store[2][0]
            keyword1=word
            is_char=0
            is_word=1
            idx=0
    elif(select==5):
        idx=idx+1
        word_prediction(keyword1,keyword2)
    if(is_char==0):
        flg=0
        temp=len(sentence)
        for i in range(len(sentence)-1,0,-1):
            if(sentence[i]==' '):   
                temp=i
                flg=1
                break;
        if(flg==1):
            sentence=sentence[:temp+1]
        sentence=sentence+word
    if(is_char==1):
        sentence=sentence+take_new_input


    
    print(sentence)
        
    print("Enter new word/character")
    take_new_input=raw_input()
    if(take_new_input==' '):
        sentence=sentence+' '
        space=space+1
        main()
    if(is_char):
        keyword1=keyword1+take_new_input
        word_prediction(keyword1,'')
    elif(sentence[len(sentence)-1]!=' ' and is_word==1):
        word_prediction(keyword1+take_new_input,'')
    elif(sentence[len(sentence)-1]==' ' and is_word==1):
        word_prediction(keyword1,take_new_input)        



def main(): 
    global take_new_input
    while(1):
        print("Enter new word/character")
        take_new_input=raw_input()
        print("--------------")
        word_prediction(take_new_input,'')

main()



