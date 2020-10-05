from tkinter import *
from tkinter import messagebox
def replace(string,text,index):
    new_str = ""
    a=0
    for i in range (len(string)):
            if i == index and a == 0:
                new_str += text.lower()
                a = 1
            else:
                new_str += string[i]
    return new_str                
def check(button):
    w_check = 0
    b  = 0
    global i
    for j in range(len(words_list2[i])):
       if(button["text"].lower() == words_list2[i][j] or button["text"] == words_list2[i][j]) :
          new_str = replace(words_list[i],button["text"],j)
          #print(new_str)
          words_list[i] = new_str
          words_l.config(text=new_str)
          b = 1
    if b == 0:
            global left
            left -= 1
            #print(left)
            chance_score_l.config(text = left)
    if left == 0:
        rr = messagebox.showinfo("Loose","You have loose the game press ok to exit")                      
        root.destroy()
    if i == 9:
        r1 = messagebox.showinfo("Won","You have won the game!")
        root.destroy()
    if words_list[i] == words_list2[i]:
           i += 1
           if i == 9:
                r1 = messagebox.showinfo("Won","You have won the game!")
                root.destroy()  
           words_l.configure(text=words_list[i])

                 
def choosewords():
    pass           
#VARIABLES============================
left = 5
words_list = ["A** **ndi**on**","S**o*l","H***i","L**t*p","B***l*","S**p*a**h","B*i**","S*ft***e","A**i*a"]
words_list2 = ["Air conditioner","School","Hindi","Laptop","Bottle","Stopwatch","Brick","Software","Almira"]
#print(words_list[0][2])
i = 0
#Root congiguration
root = Tk()
root.title("Hangman Game")
root.geometry("700x500+300+100")
root.configure(bg="light green")
root.wm_iconbitmap("E:\\Python projects - G\\Hangman\\logo.ico")
#Label====================================================
head_l = Label(root,text="Welcome to the Hangman Game",font=("times","20","underline italic bold"),bg="light green",fg="blue")
head_l.place(x=170,y=20)

chance_left_l = Label(root,text=f"Chance Left:",font = ("arial","15","bold"),bg="light green")
chance_left_l.place(x=10,y=200)

chance_score_l = Label(root,text=left,font = ("arial","15","bold"),bg="light green")
chance_score_l.place(x=50,y=235)

words_l = chance_left_l = Label(root,text=words_list[i],font = ("arial","20","bold"),bg="light green")
words_l.place(x=80,y=100,width=500)
#Buttons======================================================================
A_btn = Button(root,text="A",font="arial 15 bold",bg="red",fg="blue",command=lambda:check(A_btn))
A_btn.place(x=10,y=300,width=55,height=55)

B_btn = Button(root,text="B",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(B_btn))
B_btn.place(x=70,y=300,width=55,height=55)

C_btn = Button(root,text="C",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(C_btn))
C_btn.place(x=130,y=300,width=55,height=55)

D_btn = Button(root,text="D",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(D_btn))
D_btn.place(x=190,y=300,width=55,height=55)

E_btn = Button(root,text="E",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(E_btn))
E_btn.place(x=250,y=300,width=55,height=55)

F_btn = Button(root,text="F",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(F_btn))
F_btn.place(x=310,y=300,width=55,height=55)

G_btn = Button(root,text="G",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(G_btn))
G_btn.place(x=370,y=300,width=55,height=55)

H_btn = Button(root,text="H",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(H_btn))
H_btn.place(x=430,y=300,width=55,height=55)

I_btn = Button(root,text="I",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(I_btn))
I_btn.place(x=490,y=300,width=55,height=55)

J_btn = Button(root,text="J",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(J_btn))
J_btn.place(x=550,y=300,width=55,height=55)

K_btn = Button(root,text="K",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(K_btn))
K_btn.place(x=610,y=300,width=55,height=55)

L_btn = Button(root,text="L",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(L_btn))
L_btn.place(x=10,y=360,width=55,height=55)

M_btn = Button(root,text="M",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(M_btn))
M_btn.place(x=70,y=360,width=55,height=55)

N_btn = Button(root,text="N",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(N_btn))
N_btn.place(x=130,y=360,width=55,height=55)

O_btn = Button(root,text="O",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(O_btn))
O_btn.place(x=190,y=360,width=55,height=55)

P_btn = Button(root,text="P",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(P_btn))
P_btn.place(x=250,y=360,width=55,height=55)

Q_btn = Button(root,text="Q",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(Q_btn))
Q_btn.place(x=310,y=360,width=55,height=55)

R_btn = Button(root,text="R",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(R_btn))
R_btn.place(x=370,y=360,width=55,height=55)

S_btn = Button(root,text="S",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(S_btn))
S_btn.place(x=430,y=360,width=55,height=55)

T_btn = Button(root,text="T",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(T_btn))
T_btn.place(x=490,y=360,width=55,height=55)

U_btn = Button(root,text="U",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(U_btn))
U_btn.place(x=550,y=360,width=55,height=55)

V_btn = Button(root,text="V",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(V_btn))
V_btn.place(x=610,y=360,width=55,height=55)

W_btn = Button(root,text="W",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(W_btn))
W_btn.place(x=210,y=420,width=55,height=55)

Y_btn = Button(root,text="X",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(Y_btn))
Y_btn.place(x=270,y=420,width=55,height=55)

X_btn = Button(root,text="Y",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(X_btn))
X_btn.place(x=330,y=420,width=55,height=55)

Z_btn = Button(root,text="Z",font="arial 15 bold",bg="red",fg="blue",width="4",height=2,command=lambda:check(Z_btn))
Z_btn.place(x=390,y=420,width=55,height=55)


root.mainloop()