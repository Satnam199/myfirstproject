words=['orange','Mango','Apple','Gun','Fan','Tv','Laptop','mom','graps']

def labelslider():
    global count, sliderword
    text= 'welcome to typing speed increaser game'
    if(count>=len(text)):
        count= 0
        sliderword = ''
    sliderword += text[count] 
    count+=1
    fontlabel.configure(text=sliderword)  
    fontlabel.after(150,labelslider) 


def time():
    global timeleft,score,miss
    if (timeleft>=11):
        pass
    else:
        timelabelcount.configure(fg='red')
    if (timeleft>0):
        timeleft -= 1
        timelabelcount.configure(text=timeleft)
        timelabelcount.after(1000,time)
    else:
        gameplaydetaillabel.configure(text='Hit ={} | Miss = {} | totalscore ={}'.format(score,miss,score-miss))   
        rr= messagebox.askretrycancel('askretrycancle','for play againhit retry button')
        if(rr==True):
            score=0
            timeleft=60
            miss=0
            timelabelcount.configure(text=timeleft)
            wordlabel.configure(text=words[0])
            scorelabelcount.configure(text=score)



def startgame(event):
    global score,miss
    if(timeleft == 60):
        time()
    gameplaydetaillabel.configure(text='')
    if(wordentry.get()== wordlabel['text']):
        score += 1
        scorelabelcount.configure(text=score)
        
    else:
        miss += 1
        
        
    random.shuffle(words) 
    wordlabel.configure(text=words[0])   
    wordentry.delete(0,END)



from tkinter import *
import random
from tkinter import messagebox

################################################### root method
root = Tk()
root.geometry('800x600+400+100')
root.configure(bg='powder blue')
root.title('TYPING SPEED INCREASER GAME')
# root.iconbitmap('typingspeed.ico')
#################################################################################### VARIABLE
score=0
timeleft=60
count =0
sliderword = ''
miss=0
############################################################## label method
fontlabel = Label(root,text='welcome to typing speed increaser game',font=('airal',25,'italic bold'),
                              bg='powder blue',fg='red',width=40)

fontlabel.place(x=10,y=10)
labelslider()

random.shuffle(words)

wordlabel =Label(root,text=words[0],font=('airal',40,'italic bold'),bg='powder blue')
wordlabel.place(x=280,y=200)


scorelabel = Label(root,text='your score : ',font=('airal',25,'italic bold'),bg='powder blue')
scorelabel.place(x=10,y=100)


scorelabelcount = Label(root,text=score,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
scorelabelcount.place(x=80,y=180)
############################################################################################### entry method
wordentry =Entry(root,font=('airal',20,'italic bold'),bd=10,justify='center')
wordentry.place(x=250,y=300)
timerlabel = Label(root,text='time left :',font=('airal',25,'italic bold'),bg='powder blue')
timerlabel.place(x=600,y=100)

timelabelcount = Label(root,text=timeleft,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
timelabelcount.place(x=680,y=180)

gameplaydetaillabel=Label(root,text='type word and hit enter button',font=('airal',30,'italic bold'),
                      bg='powder blue',fg='dark gray')
gameplaydetaillabel.place(x=120,y=450)

wordentry.focus_set()

############################################################
root.bind('<Return>',startgame)
root.mainloop()