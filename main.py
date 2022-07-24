from tkinter import *
from PIL import Image, ImageTk
import random 
from tkinter import messagebox
import math
import sys
import os
names = []
asked = []
score=0



def scrambler(): 
   global qnum
   qnum = random.randint(1,11) 
   if qnum not in asked:
      asked.append(qnum)
   elif qnum in asked:
      scrambler()


class UserEnterQuiz:
  def __init__(self, parent):
      self.heading= Label (parent, text = "THE MUSIC QUIZ", font=("Helvetica", "35", "bold"), bg="#07989d", fg="white")
      self.heading.place(x=140,y=150)
      
        #label for username
      self.username_label=Label (parent, text="Enter Username Here:", font=("Helvetica","15" ), bg="#07989d", fg="white")
      self.username_label.place(x=235,y=270)
        
        #entry box
      self.entry_box=Entry (parent, font=("Times 20 italic bold","20"))
      self.entry_box.place(x=175,y=305) 
        
         #continue button
      self.play_button = Button (parent, text="CONTINUE", font=("Helvetica", "35", "bold",), bg="#07989d", command=self.name_check, fg="white")  
      self.play_button.place(x=208,y=365)

      
  def name_check(self):
    entry = self.entry_box.get()
    if entry == "":
       messagebox.showerror('error', "please enter your username")
    else:
      self.name_collection()
    
  
    


  def name_collection(self):  
    name=self.entry_box.get()
    names.append(name) #add name to names list declared at the beginning
    self.heading.destroy()
    self.username_label.destroy()
    self.entry_box.destroy()
    self.play_button.destroy()
    Questions(root)



      
      #add name to names list declared at the beginning
        #self.quiz_frame.destroy() #Destroy name frame then open the quiz runner
class Questions:  
  def __init__(self, parent):
    scrambler()


#questions storage, tells the quiz about question, image and options 
    self.questions_answers =  {
  1: ["How many studio albums have the k-pop group blackpink  released?", '4', '8', '2', '732', '2', 3, "images/BLK.png" ],
  2: ["What is the Weeknd's 4th album?", 'Kissland', 'My Dear melonchy', 'Dawn FM', 'Beauty behind the madness', 'After Hours',4, "images/we.png" ],
  3: ["Who starrred in the music video Out of Time by the Weeknd?", 'HoYeon Jung', 'Lee Jung-jae', 'Jeffrey Su', 'Anupam Tripathi', 'HoYeon Jung',1, "images/out.png" ],
  4: ["How many strings on a violin?", '3', '-17', '0', '4', '4',4, "images/v.png" ],
  5: ["Which show made One Direction?", 'The Voice ', 'X Factor', 'Americas Got Talents', 'American Idol', 'X Factor',2, "images/od.png" ],
  6: ["When did Beyonce debut?", '1997', '2001', '1995', '2015', '1995',3, "images/be.png" ],
  7: ["What is Drakes most streamed song to date?", 'Gods Plan', 'Hotline Bling', 'One Dance', 'In my Feelings', 'One Dance',3, "images/drake.png" ],
  8: ["What year was YMCA realeased?", '1956', '1978', '1996', '1986', '1978',2, "images/YMCA.png" ],
  9: ["How many members does BTS have?", '12', '7', '15','78', '7',2, "images/bts.png" ],
  10: ["Which mathematical symbol was the title of Ed Sheeran’s first album in 2011?", '+', '-', 'x','=', '+',1, "images/ed.png" ],
  11: ["How old was Mozart when he wrote his first piece?", '5', '17', '15','25', '5',1, "images/mozrt.png" ],
   
}
    
#the buttons and labels for the question screen
    self.title_label = Label (parent, text= "The Music Quiz", font=("Courier", "18", "bold"), bg="#07989d", fg="white")
    self.title_label.place (x=385, y=60)
    
    self.question_label = Label (parent, text = self.questions_answers[qnum][0], font=("Tw Cen MT", "10", "bold"),bg="#07989d", fg="white")
    self.question_label.place(x=25,y=100)

    self.var1=IntVar()
 
    self.op1= Radiobutton(parent, text=self.questions_answers[qnum][1], font=("Courier","9"),value=1,padx=10,pady=10,
                variable=self.var1)
    self.op1.place(x=450,y=160)
     
    self.op2= Radiobutton(parent, text=self.questions_answers[qnum][2], font=("Courier","9"),value=2,padx=10,pady=10,
                variable=self.var1)
    self.op2.place(x=450,y=210)

    self.op3= Radiobutton(parent, text=self.questions_answers[qnum][3], font=("Courier","9"), value=3,padx=10,pady=10,
                variable=self.var1)
    self.op3.place(x=450,y=260)

    self.op4= Radiobutton(parent, text=self.questions_answers[qnum][4], font=("Courier","9"), value=4,padx=10,pady=10,
                variable=self.var1)
    self.op4.place(x=450,y=310)

    self.confirm_button = Button(parent, text="Confirm", font=("Courier","17"), fg="white", bg="#07989d", command=self.tester)
    self.confirm_button.place(x=490,y=400)   
      
    self.score_label=Label(parent, text="Score", font=("Helvetica", "15"), bg="#07989d", fg="white")
    self.score_label.place(x=300,y=10)

    self.answer_label=Label(parent, font=("Courier", "10", ), fg="white", bg="#07989d")
    self.answer_label.place(x=105,y=415)

    self.quit= Button(parent, text="Quit", font=("Courier", "15"), fg="white", bg="red",   command=self.endScreen)
    self.quit.place(x=20,y=410)

    self.photo= PhotoImage(file = "BLK.png") #place holder image 
    self.image= Button(parent, image = self.photo)
    self.image.place(x=60, y=145)
    self.photo.config(file=self.questions_answers[qnum][7])#sets the correct image for the first question
    



  
    


  


  def questions_setup(self):
    scrambler()
    self.var1.set(0)#configs the buttons and titles to fit the new question
    self.question_label.config(text=self.questions_answers[qnum][0])
    self.op1.config(text=self.questions_answers[qnum][1])
    self.op2.config(text=self.questions_answers[qnum][2])
    self.op3.config(text=self.questions_answers[qnum][3])
    self.op4.config(text=self.questions_answers[qnum][4]) 
    self.photo.config(file=self.questions_answers[qnum][7])#the image button is configed 
    
  def tester(self):
    global score 
    scr_label = self.score_label 
    score_label = self.answer_label
    choice = self.var1.get() 
    if len(asked)>10: #to determine if its the last question and just end the quiz after
      if choice==self.questions_answers[qnum][6]: 
        score +=1 
        scr_label.configure(text=score) 
        self.confirm_button.config(text="Confirm") 
        score_label.configure(text="")
        self.endScreen()
      else:
        score+=0 
        score_label.configure(text=" NO!...The correct answer is"+ self.questions_answers[qnum][5]) 
        self.confirm_button.config(text="Confirm")
        self.endScreen()
    else:
      if choice==0:#if the user does not select an  option
        messagebox.showerror('error', "please select an option") #error message 
        choice=self.var1.get() 
      else: #if the choice is made
        if choice==self.questions_answers[qnum][6]: #if choice made is correct
          score+=1 #add one to score
          scr_label.configure(text=score)
          self.confirm_button.configure(text="Confirm")
          score_label.configure(text="")
          self.questions_setup() #run method to next question
        else: #if choice is incorrect
          score+=0
          messagebox.showinfo("Oh no","The correct answer was " + self.questions_answers[qnum][5])
          self.confirm_button.configure(text="Confirm")
          self.questions_setup() #move to next question
          
  def endScreen(self): 
    #destroys the labels and buttons to open the leaderboard window
    self.title_label.destroy()
    self.question_label.destroy()
    self.confirm_button.destroy()
    self.score_label.destroy()
    self.answer_label.destroy()
    self.quit.destroy()
    self.op1.destroy()
    self.op2.destroy()
    self.op3.destroy()
    self.op4.destroy()
    self.image.destroy()
    name=names[0]
    file=open("board.txt","a") #opens the highscores file
    
    if name == "admin_reset": 
      file=open("board.txt", "w")
    else:
      file.write(str(score))  #turns the score into a string
      file.write(" - ") #writes into the text file
      file.write(name+ "\n") #writes the name into the text file and then goes to a new line
      file.close() #closes the file
    inputFile= open("board.txt", "r") #opens the highscores file in read mode
    lineList = inputFile.readlines() #line list equals the each line in the list
    lineList.sort()
    top=[]
    top5=(lineList[-5:])
    for line in top5:
      point=line.split(" - ")
      top.append((int(point[0]), point[1]))
    file.close() 
    top.sort()
    top.reverse()
    return_string = ""
    for i in range(len(top)):
      return_string +="{} - {}\n".format(top[i][0], top[i][1])
    print(return_string) #for testing to show on the console
    open_endscrn=leaderboard(root)
    open_endscrn.leader_button.config(text=return_string)   
   


          
#starting point 
scrambler()




class Leaderboard:
  def __init__(self, parent):
    background="light blue"
    self.end_window= Toplevel(root)
    self.end_window.title("leaderBoared")

    self.end_frame = Frame (self.end_window, width=1000, height=1000, bg=background)
    self.end_frame.grid(row=0)

    self.end_heading = Label (self.end_frame, text='Well Done', font=('Tw Cen MT', 22 , 'bold'), bg=background, pady=10)
    self.end_heading.grid(row=0)

    self.leader_button = Button (self.end_frame, text="Exit", width=10, bg="#07989d", font=('Tw Cen MT', 12 , 'bold'), fg="white"  )
    self.leader_button.grid(row=4, pady=10)
    
    self.restart_button = Button (self.end_frame, text="Restart", width=10, bg="Green", font=('Tw Cen MT', 12 , 'bold'), command=self.restart )
    self.restart_button.grid(row=8, pady=10)

    self.exit = Button (self.end_frame, text="Exit", width=10, bg="Red", font=('Tw Cen MT', 12 , 'bold'), command=self.close_end )
    self.exit.grid(row=7, pady=10)


  def close_end(self):
    self.end_box.destroy()#destroys the window 
    root.withdraw()#minimizes 

  def restart(self):
    python = sys.executable
    os.execl(python, python, * sys.argv)#restarts the quiz using the OS



  




if __name__ == "__main__":
    root = Tk()
    root.title("The Music Quiz") 
    root.geometry("700x450")
    bg_image = Image.open("images/home_screen1.PNG") #need to use Image if need to resize 
    bg_image = bg_image.resize((700, 450), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image) 
          #label for image
    image_label= Label(root, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always

    quiz_instance = UserEnterQuiz(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear

