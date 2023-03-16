import tkinter as tk
import random
from tkinter.constants import CENTER, DISABLED
from PIL import ImageTk, Image
import json
from tkinter import Entry, Label, PhotoImage, messagebox, Button, ttk


i = 0
                
cont = 0
cont2 = 0

def win():
    global window,player_score1,player_score2,player_score_lb1
    player_score1 = 0
    player_score2 = 0
    window = tk.Tk()
    window.geometry("900x600+600+200")
    window.configure(bg="white")
    window.resizable(True, True)
    window.title("Final Game")


    # frames

    settings_frame = tk.Frame(
        window,
        #height=20,
        bg="white"
        #bg="#302B2B"
    )
    settings_frame.pack(fill = "y", side = "right")

    score_frame = tk.Frame(
        window,
       # height=20,
        bg="white"
    )
    score_frame.pack(fill = "y", side = "left")
    #score_frame.grid(row=100,column=0,padx=100,pady=100)


    dealer_frame = tk.Frame(
        window,
      #  height=20,
        bg="white"
    )
    dealer_frame.pack(pady=20)


    player_frame = tk.Frame(
        window,
        bg="white",
       # height=60
    )
    player_frame.pack(pady=30)


    # Create Tkinter Object
 
    # Read the Image
    dot = Image.open("dot.png")
    #line = Image.open("line.png")
    #line2= Image.open("line2.png")
 
    # Resize the image using resize() method
    resize_image = dot.resize((30, 30))
    #resize_line = line.resize((60, 60))
    #resize_line2 = line2.resize((60, 60))

    newdot = ImageTk.PhotoImage(resize_image)
    #newline = ImageTk.PhotoImage(resize_line)
    #newline2 = ImageTk.PhotoImage(resize_line2)

    cnt = 0
    btn_pos = {}
    j=1


    for i in range(1, 12):
        for j in range(1, 12):
            label = Label(dealer_frame, image=newdot)
            label.image = newdot

            global label1, label2

            label1 = Button(
                dealer_frame,
                width = 7,
                height = 1,
                bg = "black",
                command=changecolor1
            )
            #label1.image = newline

            label2 = Button(
                dealer_frame,
                width = 1,
                height = 3,
                bg = "black",
                command=changecolor2

            )
            #label2.image = newline2
            
            if (i%2==1 and j%2 == 1):
                label.grid(row=i, column=j)  
            if(i%2==1 and j%2==0):
                label1.grid(row=i, column = j)
                with open("btn_pos.json") as f:
                    btn_pos.update({cnt:[i, j]})
            if(i%2==0 and j%2==1):
                label2.grid(row=i,column=j)
                with open("btn_pos.json") as f:
                    btn_pos.update({cnt:[i, j]})


            cnt += 1

    print(btn_pos)

    global name, name2
    
    name="Player 1"
    name2 = "Player 2"

    # scores
    
    player_score_lb1 = tk.Label(
        score_frame,
        text=f"Your score {name}: 0",
        bg="white",
        font=("Helvetica", 17)
    )
    player_score_lb1.grid(row=1, column=0, padx=0,pady=(100,100))

    player_score_lb1.config(text=f"Your Score {name}: " + str(player_score1)+'\n' + f"Your Score {name2}: " + str(player_score2))

    # buttons

    restart_bt = tk.Button(
        score_frame,
        text="Restart",
        command=restart,
        relief=tk.FLAT,
        font=("Helvetica", 14),
        width=15,
        #fg="#FFFFFF",
        bg="#77AAE8"
    )
    restart_bt.grid(row=5, column=0, pady=2)

    name_bt = tk.Button(
        settings_frame,
        text="Name Player 1",
        command=changename,
        relief=tk.FLAT,
        font=("Helvetica", 14),
        width=15,
        bg="#8896B9"
    )
    name_bt.grid(row=7, column=10, pady=2)

    name_bt2 = tk.Button(
        settings_frame,
        text="Name Player 2",
        command=changename2,
        relief=tk.FLAT,
        font=("Helvetica", 14),
        width=15,
        bg="#8896B9"
    )
    name_bt2.grid(row=8, column=10, pady=2)



    window.mainloop()


def changecolor1():
    global label1, cont, cont2
    cont+=1
    cont2 += 1
    if label1['bg'] == 'black':
        if(cont%2==1):
            label1.config(bg="blue", state=tk.DISABLED)
            label1['state'] = 'disabled'
        else:
            label1.config(bg="red", state=tk.DISABLED)
    print(label1['bg'])

def changecolor2():
    global label2, cont, cont2
    cont += 1
    cont2 += 1
    if label2['bg'] == 'black':
        if(cont2%2 == 1):
            label2.config(bg="blue", state=tk.DISABLED)
        else:
            label2.config(bg = "red", state=tk.DISABLED)
    print(label2['bg'])


def changename():
    
    #open a frame
    windowname = tk.Tk()
    windowname.geometry("300x200")
    windowname.configure(bg="#302B2B")
    windowname.resizable(True, True)
    windowname.title("Name")

    def name_command():
        global name_text,name, name2
        name = name 
        name2 = name2
        name_text=entry1.get()
        print(name_text)
        name=name_text
        player_score_lb1.config(text=f"Your Score {name}: " + str(player_score1)+'\n' + f"Your Score {name2}" + str(player_score2))
        return None

    entry1=Entry(windowname,width=50)
    entry1.pack(padx=50,pady=50)
    
    name_bt = tk.Button(
        windowname,
        text="Name",
        #command=windowbet.configure(),
        #commnad=windowbet.config(state=tk.DISABLED),
        command=name_command,
        relief=tk.FLAT,
        font=("Helvetica", 12),
        width=15,
        bg="#8896B9"
    )
    name_bt.pack()
    

def changename2():
    
    #open a frame
    windowname = tk.Tk()
    windowname.geometry("300x200")
    windowname.configure(bg="#302B2B")
    windowname.resizable(True, True)
    windowname.title("Name")

    def name_command2():
        global name_text2,name2, name
        name_text2=entry1.get()
        print(name_text2)
        name2=name_text2
        player_score_lb1.config(text=f"Your Score {name}: " + str(player_score1)+'\n' + f"Your Score {name2}: " + str(player_score2))
        return None

    entry1=Entry(windowname,width=50)
    entry1.pack(padx=50,pady=50)
    
    name_bt2 = tk.Button(
        windowname,
        text="Name",
        #command=windowbet.configure(),
        #commnad=windowbet.config(state=tk.DISABLED),
        command=name_command2,
        relief=tk.FLAT,
        font=("Helvetica", 12),
        width=15,
        bg="#8896B9"
    )
    name_bt2.pack()
'''
global decision
decision=1    

def stand():
    hit_bt.config(state=tk.DISABLED)
    global i,dealer_chips,player_chips,decision,decace,dealer_score,dealer_card2,dealer_card3
    i = 1
    dealer_card2 = random.choice(cards)
    cards.remove(dealer_card2)
    dealer_card2.show_card(dealer_frame)
    dealer_score = dealer_card.value

    if dealer_card2.typer == "ace" and dealer_score < 11:
        dealer_card2.value == 11
        decace = random.choice([1,11])
        if decace==1:
            dealer_card2.value=1
   
    print(dealer_card2.value)

    
    dealer_score = dealer_score + dealer_card2.value
    print(dealer_score)
    dealer_score_lb1.config(text="Dealer's Score: " + str(dealer_score)+'\n'+"Dealer's chips: "+str(dealer_chips))
    player_score_lb1.config(text=f"Your Score {name}: " + str(player_score)+'\n'+f"Your chips {name}: "+str(player_chips))

    while dealer_score < 21 and decision==1:
        i = i + 1
        #random hit or stand
        if(dealer_score>14):
            decision = random.choice([1,2])
        #print(decision,dealer_score)
        if decision==1:
            dealer_card3 = random.choice(cards)
            cards.remove(dealer_card3)
            dealer_card3.show_card(dealer_frame)
            if dealer_card3.typer == "ace" and dealer_score < 11:
               dealer_card3.value == 11
               decace = random.choice([1,11])
               if decace==1:
                  dealer_card3.value=1
            dealer_score = dealer_score + dealer_card3.value
            dealer_score_lb1.config(text="Dealer's Score: " + str(dealer_score)+'\n'+"Dealer's chips: "+str(dealer_chips))

    if dealer_score > 21:
        messagebox.showinfo("Blackjack", "Congratulations, you won!")
        player_chips+=chips
        dealer_chips-=chips
        dealer_score_lb1.config(text="Dealer's Score: " + str(dealer_score)+'\n'+"Dealer's chips: "+str(dealer_chips))
        player_score_lb1.config(text=f"Your Score {name}: " + str(player_score)+'\n'+f"Your chips {name}: "+str(player_chips))
        #player_chips++ dealer_chips--
        youwin()

    elif dealer_score == player_score:
        messagebox.showinfo("Blackjack", "It is draw, money will split!")
        #player_chips dealer_chips

    elif dealer_score > player_score:
        messagebox.showinfo("Blackjack", "You lost, try again!")
        #player_chips-- dealer_chips++
        player_chips-=chips
        dealer_chips+=chips
        dealer_score_lb1.config(text="Dealer's Score: " + str(dealer_score)+'\n'+"Dealer's chips: "+str(dealer_chips))
        player_score_lb1.config(text=f"Your Score {name}: " + str(player_score)+'\n'+f"Your chips {name}: "+str(player_chips))
        youlose()
    elif dealer_score < player_score:
        messagebox.showinfo("You won, congratulations!")
        #player_chips++ dealer_chips--
        player_chips+=chips
        dealer_chips-=chips
        dealer_score_lb1.config(text="Dealer's Score: " + str(dealer_score)+'\n'+"Dealer's chips: "+str(dealer_chips))
        player_score_lb1.config(text=f"Your Score {name}: " + str(player_score)+'\n'+f"Your chips {name}: "+str(player_chips))
        youwin()
    stand_bt.config(state=tk.DISABLED)
'''

def youwin():
    windowwin = tk.Toplevel(window)
    windowwin.geometry("400x500+600+200")
    windowwin.configure(bg="#FFFFFF")
    windowwin.resizable(True, True)
    img=ImageTk.PhotoImage(Image.open("./images/youwin.jpg"))
    windowwin.iconphoto = ImageTk.PhotoImage(file="./images/youwin.jpg")
    windowwin.title("You win")
    lb1=tk.Label(windowwin,image=img)
    lb1.image=img
    lb1.pack()

def youlose():
    windowlose = tk.Toplevel(window)
    windowlose.geometry("400x500+600+200")
    windowlose.configure(bg="#BBBBBB")
    windowlose.resizable(True, True)
    img=ImageTk.PhotoImage(Image.open("./images/youlose.jpg"))
    windowlose.iconphoto = ImageTk.PhotoImage(file="./images/youlose.jpg")
    windowlose.title("You lost")
    label1=tk.Label(windowlose,image=img)
    label1.image=img
    label1.pack()

def restart():
    window.destroy()
    win()


win()
