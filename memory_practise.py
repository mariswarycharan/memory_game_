
# import pyttsx3

# engine = pyttsx3.init()
# engine.setProperty("rate",50)
# voice_id = engine.getProperty("voices")
# for i in voice_id:
#     print(i)
#     if i == "tamil":
#         print(i)
# print(voice_id[0].id)
# print(voice_id[1].id)


# engine.setProperty("voice",voice_id[1].id)
# engine.say("hi mariswary are you prepared tomato rice")
# engine.runAndWait()

# from tkinter.filedialog import askopenfile

# file = askopenfile("r",filetypes=[("files","*.txt")])
# con = file.read()

# print(con)
import pyttsx3
from tkinter.messagebox import showinfo
from itertools import count
import random
from tkinter.font import BOLD, ITALIC
from logging import root
from secrets import choice
from tkinter import *
from PIL import Image,ImageTk
import time
engine = pyttsx3.init()
list_ima = ["D:\\Downloads\\big.png","D:\\Downloads\\elephant.png","D:\\Downloads\\fish.png","D:\\Downloads\\bird.png",
            "D:\\Downloads\\peacoak.png","D:\\Downloads\\lion.png","D:\\Downloads\\elephant.png","D:\\Downloads\\anil.png",
            "D:\\Downloads\\fish.png","D:\\Downloads\\lion.png","D:\\Downloads\\korila.png","D:\\Downloads\\peacoak.png",
            "D:\\Downloads\\big.png","D:\\Downloads\\bird.png","D:\\Downloads\\anil.png","D:\\Downloads\\korila.png",
            "D:\\Downloads\\tiger.png","D:\\Downloads\\zebara.png","D:\\Downloads\\tiger.png","D:\\Downloads\\zebara.png",
            "D:\\Downloads\\dog.png","D:\\Downloads\\jack.png","D:\\Downloads\\dog.png","D:\\Downloads\\jack.png"]
# print(len(list_ima))
l = [i for i in range(0,len(list_ima))]
# print(l)
add = []
add_b = []
score = 0
choice1 = random.shuffle(list_ima)
choice2 = random.shuffle(l)   
n = random.random()

image_ques = Image.open("D:\\Downloads\\question.png")
image_show = Image.open("D:\\Downloads\\idea.png")

ima1 = Image.open(list_ima[l[0]])
ima2 = Image.open(list_ima[l[1]])
ima3 = Image.open(list_ima[l[2]])
ima4 = Image.open(list_ima[l[3]])
ima5 = Image.open(list_ima[l[4]])
ima6 = Image.open(list_ima[l[5]])
ima7 = Image.open(list_ima[l[6]])
ima8 = Image.open(list_ima[l[7]])
ima9 = Image.open(list_ima[l[8]])
ima10 = Image.open(list_ima[l[9]])
ima11 = Image.open(list_ima[l[10]])
ima12 = Image.open(list_ima[l[11]])
ima13 = Image.open(list_ima[l[12]])
ima14 = Image.open(list_ima[l[13]])
ima15 = Image.open(list_ima[l[14]])
ima16 = Image.open(list_ima[l[15]])
ima17 = Image.open(list_ima[l[16]])
ima18 = Image.open(list_ima[l[17]])
ima19 = Image.open(list_ima[l[18]])
ima20 = Image.open(list_ima[l[19]])
ima21 = Image.open(list_ima[l[20]])
ima22 = Image.open(list_ima[l[21]])
ima23 = Image.open(list_ima[l[22]])
ima24 = Image.open(list_ima[l[23]])


image_question_resize = image_ques.resize((100,100)) 
image_idea_resize = image_show.resize((100,100))
   
image1 = ima1.resize((100,100))
image2 = ima2.resize((100,100))
image3 = ima3.resize((100,100))
image4 = ima4.resize((100,100))
image5 = ima5.resize((100,100))
image6 = ima6.resize((100,100))
image7 = ima7.resize((100,100))
image8 = ima8.resize((100,100))
image9 = ima9.resize((100,100))
image10 = ima10.resize((100,100))
image11 = ima11.resize((100,100))
image12 = ima12.resize((100,100))
image13 = ima13.resize((100,100))
image14 = ima14.resize((100,100))
image15 = ima15.resize((100,100))
image16 = ima16.resize((100,100))
image17 = ima17.resize((100,100))
image18 = ima18.resize((100,100))
image19 = ima19.resize((100,100))
image20 = ima20.resize((100,100))
image21 = ima21.resize((100,100))
image22 = ima22.resize((100,100))
image23 = ima23.resize((100,100))
image24 = ima24.resize((100,100))

root = Tk()
root.geometry("550x730")

count = 0

def main1():
    global i1,add,count
    b1.config(image=im1)
    add.append(list_ima[l[0]])
    add_b.append(b1)
    count += 1 
    b1.configure(state=DISABLED)
    
   
    if count == 2:
        mainc()
    

def main2():
    global ima1,add,count
    b2.config(image=im2)
    
    add.append(list_ima[l[1]])
    add_b.append(b2)
    
    count += 1
    b2.configure(state=DISABLED)
    
    if count == 2:
        
        mainc()
    

def main3():
    global i2,add,count
    b3.config(image=im3)

    add.append(list_ima[l[2]])
    add_b.append(b3)
    count += 1
    b3.configure(state=DISABLED)
    if count == 2:
        mainc()
        
def main4():
    global i2,add,count
    b4.config(image=im4)
  
    add.append(list_ima[l[3]]) 
    add_b.append(b4)
    count += 1
    b4.configure(state=DISABLED)
    
    if count == 2:
        mainc()
        
def main5():
    global i1,add,count
    b5.config(image=im5)
    add.append(list_ima[l[4]])
    add_b.append(b5)
    count += 1 
    b5.configure(state=DISABLED)
    
   
    if count == 2:
        mainc()
    

def main6():
    global ima1,add,count
    b6.config(image=im6)
    
    add.append(list_ima[l[5]])
    add_b.append(b6)
    
    count += 1
    b6.configure(state=DISABLED)
    
    if count == 2:
        
        mainc()
    
def main7():
    global i2,add,count
    b7.config(image=im7)

    add.append(list_ima[l[6]])
    add_b.append(b7)
    count += 1
    b7.configure(state=DISABLED)
    if count == 2:
        mainc()
        
def main8():
    global i2,add,count
    b8.config(image=im8)
  
    add.append(list_ima[l[7]]) 
    add_b.append(b8)
    count += 1
    b8.configure(state=DISABLED)
    
    if count == 2:
        mainc()
        
def main9():
    global i1,add,count
    b9.config(image=im9)
    add.append(list_ima[l[8]])
    add_b.append(b9)
    count += 1 
    b9.configure(state=DISABLED)
    
   
    if count == 2:
        mainc()
    

def main10():
    global ima1,add,count
    b10.config(image=im10)
    
    add.append(list_ima[l[9]])
    add_b.append(b10)
    
    count += 1
    b10.configure(state=DISABLED)
    
    if count == 2:
        
        mainc()
    

def main11():
    global i2,add,count
    b11.config(image=im11)

    add.append(list_ima[l[10]])
    add_b.append(b11)
    count += 1
    b11.configure(state=DISABLED)
    if count == 2:
        mainc()
        
def main12():
    global i2,add,count
    b12.config(image=im12)
  
    add.append(list_ima[l[11]]) 
    add_b.append(b12)
    count += 1
    b12.configure(state=DISABLED)
    
    if count == 2:
        mainc()
        
def main13():
    global i1,add,count
    b13.config(image=im13)
    add.append(list_ima[l[12]])
    add_b.append(b13)
    count += 1 
    b13.configure(state=DISABLED)
    
   
    if count == 2:
        mainc()
    

def main14():
    global ima1,add,count
    b14.config(image=im14)
    
    add.append(list_ima[l[13]])
    add_b.append(b14)
    
    count += 1
    b14.configure(state=DISABLED)
    
    if count == 2:
        
        mainc()
    
def main15():
    global i2,add,count
    b15.config(image=im15)

    add.append(list_ima[l[14]])
    add_b.append(b15)
    count += 1
    b15.configure(state=DISABLED)
    if count == 2:
        mainc()
        
def main16():
    global i2,add,count
    b16.config(image=im16)
  
    add.append(list_ima[l[15]]) 
    add_b.append(b16)
    count += 1
    b16.configure(state=DISABLED)
    
    if count == 2:
        mainc()
        
def main17():
    global i1,add,count
    b17.config(image=im17)
    add.append(list_ima[l[16]])
    add_b.append(b17)
    count += 1 
    b17.configure(state=DISABLED)
    
   
    if count == 2:
        mainc()
    

def main18():
    global ima1,add,count
    b18.config(image=im18)
    
    add.append(list_ima[l[17]])
    add_b.append(b18)
    
    count += 1
    b18.configure(state=DISABLED)
    
    if count == 2:
        
        mainc()
    
def main19():
    global i2,add,count
    b19.config(image=im19)

    add.append(list_ima[l[18]])
    add_b.append(b19)
    count += 1
    b19.configure(state=DISABLED)
    if count == 2:
        mainc()
        
def main20():
    global i2,add,count
    b20.config(image=im20)
  
    add.append(list_ima[l[19]]) 
    add_b.append(b20)
    count += 1
    b20.configure(state=DISABLED)
    
    if count == 2:
        mainc()
        
def main21():
    global i1,add,count
    b21.config(image=im21)
    add.append(list_ima[l[20]])
    add_b.append(b21)
    count += 1 
    b21.configure(state=DISABLED)
    
   
    if count == 2:
        mainc()
    

def main22():
    global ima1,add,count
    b22.config(image=im22)
    
    add.append(list_ima[l[21]])
    add_b.append(b22)
    
    count += 1
    b22.configure(state=DISABLED)
    
    if count == 2:
        
        mainc()
    

def main23():
    global i2,add,count
    b23.config(image=im23)

    add.append(list_ima[l[22]])
    add_b.append(b23)
    count += 1
    b23.configure(state=DISABLED)
    if count == 2:
        mainc()
        
def main24():
    global i2,add,count
    b24.config(image=im24)
  
    add.append(list_ima[l[23]]) 
    add_b.append(b24)
    count += 1
    b24.configure(state=DISABLED)
    
    if count == 2:
        mainc()

image_question = ImageTk.PhotoImage(image_question_resize)
image_idea = ImageTk.PhotoImage(image_idea_resize)

im1 = ImageTk.PhotoImage(image1)
im2 = ImageTk.PhotoImage(image2)
im3 = ImageTk.PhotoImage(image3)
im4 = ImageTk.PhotoImage(image4)
im5 = ImageTk.PhotoImage(image5)
im6 = ImageTk.PhotoImage(image6)
im7 = ImageTk.PhotoImage(image7)
im8 = ImageTk.PhotoImage(image8)
im9 = ImageTk.PhotoImage(image9)
im10 = ImageTk.PhotoImage(image10)
im11 = ImageTk.PhotoImage(image11)
im12= ImageTk.PhotoImage(image12)
im13 = ImageTk.PhotoImage(image13)
im14 = ImageTk.PhotoImage(image14)
im15 = ImageTk.PhotoImage(image15)
im16 = ImageTk.PhotoImage(image16)
im17 = ImageTk.PhotoImage(image17)
im18 = ImageTk.PhotoImage(image18)
im19 = ImageTk.PhotoImage(image19)
im20 = ImageTk.PhotoImage(image20)
im21 = ImageTk.PhotoImage(image21)
im22 = ImageTk.PhotoImage(image22)
im23 = ImageTk.PhotoImage(image23)
im24 = ImageTk.PhotoImage(image24)



label_title= Label(root,text="MEMOrY GAME",font = ("ALGERIAN",50,BOLD), foreground="red",background="black",padx=30)
label_title.grid(row=1,column=1,columnspan=11)


b1 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main1)
b1.grid(row=3,column=1)

b2 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main2)
b2.grid(row=3,column=2)

b3 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main3)
b3.grid(row=3,column=3)

b4 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main4)
b4.grid(row=3,column=4)

b5 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main5)
b5.grid(row=4,column=1)

b6 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main6)
b6.grid(row=4,column=2)

b7 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main7)
b7.grid(row=4,column=3)

b8 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main8)
b8.grid(row=4,column=4)

b9 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main9)
b9.grid(row=5,column=1)

b10 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main10)
b10.grid(row=5,column=2)

b11 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main11)
b11.grid(row=5,column=3)

b12 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main12)
b12.grid(row=5,column=4)

b13 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main13)
b13.grid(row=6,column=1)

b14 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main14)
b14.grid(row=6,column=2)

b15 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main15)
b15.grid(row=6,column=3)

b16 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main16)
b16.grid(row=6,column=4)

b17 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main17)
b17.grid(row=7,column=1)

b18 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main18)
b18.grid(row=7,column=2)

b19 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main19)
b19.grid(row=7,column=3)

b20 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main20)
b20.grid(row=7,column=4)

b21 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main21)
b21.grid(row=8,column=1)

b22 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main22)
b22.grid(row=8,column=2)

b23 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main23)
b23.grid(row=8,column=3)

b24 = Button(root,padx=50,pady=40,image=image_question,borderwidth=2,relief="solid",command=main24)
b24.grid(row=8,column=4)

label_move = Label(root,text="move",foreground="blue",font = ("D:/Downloads/poppins/Poppins-Medium.otf",30,BOLD,ITALIC))
label_move.grid(row=3,column=5)
move = 30
label_move_num = Label(root,text = move,foreground="#FBB177",font = ("D:/Downloads/poppins/Poppins-Medium.otf",40,BOLD,ITALIC))
label_move_num.grid(row=4,column=5)


label_score = Label(root,text="score",foreground="blue",font = ("D:/Downloads/poppins/Poppins-Medium.otf",30,BOLD,ITALIC))
label_score.grid(row=5,column=5) 
label_score_num = Label(root,foreground="#F4A460",font = ("D:/Downloads/poppins/Poppins-Medium.otf",40,BOLD,ITALIC))
label_score_num.grid(row=6,column=5)


def mainc():
    global count,im1,score,move,rend_score,rend_moves,voice_id
 
    if len(add)>= 2:
        if add[0] == add[1]:
            add_b[0].configure(state= DISABLED)
            add_b[1].configure(state= DISABLED)
            score += 25
            label_score_num.config(text=score)
            move -= 1
            label_move_num.config(text=move)
            
            if move == 0:
                rend_score = "your score is  " + str(score)
                rend_moves = "your remaining moves are" + str(move)
                engine.setProperty("rate",150)
                voice_id = engine.getProperty("voices")
                engine.setProperty("voice",voice_id[1].id)
                engine.say(rend_score)
                engine.say(rend_moves)
                engine.runAndWait()
                showinfo("game result","game over")
                
                root.destroy()
            # print(score)
            # print(add_b)
            add_b.clear()
            add.clear()
        else:
            
            add_b[0].config(image = image_question)
            add_b[1].config(image = image_question)
            add_b[0].configure(state=ACTIVE )
            add_b[1].configure(state= ACTIVE)
            move -= 1
            label_move_num.config(text=move)
            if move == 0:
                rend_score = "your score is  " + str(score)
                rend_moves = "your remaining moves are" + str(move)
                engine.setProperty("rate",150)
                voice_id = engine.getProperty("voices")
                engine.setProperty("voice",voice_id[1].id)
                engine.say(rend_score)
                engine.say(rend_moves)
                engine.runAndWait()
                showinfo("game result","game over")
                root.destroy()
            
            
            add_b.clear()
            add.clear()
    count =0
    
            
# root.bind('<Return>',mainc)
def show():
    global b1,b2,b3,b4,im1,im2,im3,im4
    root1 = Toplevel(root)

    
    b1x = Button(root1,padx=50,image=im1,pady=40)
    b1x.grid(row=1,column=1)

    b2x = Button(root1,padx=50,image=im2,pady=40)
    b2x.grid(row=1,column=2)

    b3x = Button(root1,padx=50,image=im3,pady=40)
    b3x.grid(row=1,column=3)

    b4x = Button(root1,padx=50,image=im4,pady=40)
    b4x.grid(row=1,column=4)
    
    b5x = Button(root1,padx=50,image=im5,pady=40)
    b5x.grid(row=2,column=1)

    b6x = Button(root1,padx=50,image=im6,pady=40)
    b6x.grid(row=2,column=2)

    b7x = Button(root1,padx=50,image=im7,pady=40)
    b7x.grid(row=2,column=3)

    b8x = Button(root1,padx=50,image=im8,pady=40)
    b8x.grid(row=2,column=4)
    
    b9x = Button(root1,padx=50,image=im9,pady=40)
    b9x.grid(row=3,column=1)

    b10x = Button(root1,padx=50,image=im10,pady=40)
    b10x.grid(row=3,column=2)

    b11x = Button(root1,padx=50,image=im11,pady=40)
    b11x.grid(row=3,column=3)

    b12x = Button(root1,padx=50,image=im12,pady=40)
    b12x.grid(row=3,column=4)
    
    b13x = Button(root1,padx=50,image=im13,pady=40)
    b13x.grid(row=4,column=1)

    b14x = Button(root1,padx=50,image=im14,pady=40)
    b14x.grid(row=4,column=2)

    b15x = Button(root1,padx=50,image=im15,pady=40)
    b15x.grid(row=4,column=3)

    b16x = Button(root1,padx=50,image=im16,pady=40)
    b16x.grid(row=4,column=4)
    
    b17x = Button(root1,padx=50,image=im17,pady=40)
    b17x.grid(row=5,column=1)

    b18x = Button(root1,padx=50,image=im18,pady=40)
    b18x.grid(row=5,column=2)

    b19x = Button(root1,padx=50,image=im19,pady=40)
    b19x.grid(row=5,column=3)

    b20x = Button(root1,padx=50,image=im20,pady=40)
    b20x.grid(row=5,column=4)
    
    b21x = Button(root1,padx=50,image=im21,pady=40)
    b21x.grid(row=6,column=1)

    b22x = Button(root1,padx=50,image=im22,pady=40)
    b22x.grid(row=6,column=2)

    b23x = Button(root1,padx=50,image=im23,pady=40)
    b23x.grid(row=6,column=3)

    b24x = Button(root1,padx=50,image=im24,pady=40)
    b24x.grid(row=6,column=4)
    
    root1.after(4000,lambda:root1.destroy())
    Button_idea.configure(state=DISABLED)
    root1.mainloop()
  

    
Button_idea = Button(root,image=image_idea,padx=50,pady=40,command= show)
Button_idea.grid(row=8,column=5)



root.mainloop()
