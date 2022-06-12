from tkinter import *
from PIL import Image, ImageTk
import random 
from tkinter import messagebox
import math
names = []
global questions_answers
asked = []
score=0

questions_answers = {
  1: ["How many studio albums have the k-pop group blackpink  released?", '4', '8', '2', '732', '2', 3],
  2: ["What is the Weeknd 4rd album?", 'Kissland', 'My Dear mEelonchy', 'Dawn FM', 'Beauty behind the madness', 'After Hours',4],
  3: ["Who starrred in the music video Out of Time by the Weeknd", 'HoYeon Jung', 'Lee Jung-jae', 'Jeffrey Su', 'Anupam Tripathi', 'HoYeon Jung',1],
  4: ["How many strings on a violin?", '3', '-17', '0', '4', '4',4],
  5: ["Which show made One Direction", 'The Voice ', 'X Factor', 'Americas Got Talents', 'American Idol', 'X Factor',2],
  6: ["When did Beyonce debut?", '1997', '2001', '1945', '2015', '1995',4],
  7: ["What is Drakes most streamed song to date?", 'Gods Plan', 'Hotline Bling', 'One Dance', 'In my Feelings', 'One Dance',3],
  8: ["What year was YMCA realeased?", '1956', '1978', '1996', '1986', '1978',2],
  9: ["How many memebers does BTS have?", '12', '7', '15','78', '7',2],
}

def scrambler(): 
   global qnum
   qnum = random.randint(1,9)
   if qnum not in asked:
      asked.append(qnum)
   elif qnum in asked:
      scrambler()


class UserEnterQuiz:
  def __init__(self, parent):
      self.heading_label = Label (parent, text = "", font=("", "1", "bold"))
      self.heading_label.place(x=50,y=230)
      
        #label for username
      self.user_label=Label(parent, text="", font=("","1" ))
      self.user_label.place(x=45,y=230)
        
        #entry box
      self.entry_box=Entry(parent, font=("Times 20 italic bold","20"))
      self.entry_box.place(x=175,y=305) 
        
        #continue button
      self.play_button = Button(parent, text="CONTINUE", font=("Helvetica", "35", "bold",), bg="light blue", command=self.name_collection)  
      self.play_button.place(x=208,y=365)              
       
  def name_collection(self):
    name=self.entry_box.get()
    names.append(name) #add name to names list declared at the beginning
    self.heading_label.destroy()
    self.user_label.destroy()
    self.entry_box.destroy()
    self.play_button.destroy()
    UserEnterQuiz(root)
    
      
      #add name to names list declared at the beginning
        #self.quiz_frame.destroy() #Destroy name frame then open the quiz runner
class Questions:  
  def __init__(self, parent):
    scrambler()

    self.title_label = Label (parent, text= "The Music Quiz", font=("Courier", "18", "bold"))
    self.title_label.place (x=90, y=75)
    
    self.question_label = Label (parent, text = questions_answers[qnum][0], font=("Tw Cen MT", "9", "bold"))
    self.question_label.place(x=12,y=120)

    self.var1=IntVar()
 
    self.rb1= Radiobutton(parent, text=questions_answers[qnum][1], font=("Courier","11"),value=1,padx=10,pady=10,
                variable=self.var1)
    self.rb1.place(x=300,y=260)
     
    self.rb2= Radiobutton(parent, text=questions_answers[qnum][2], font=("Courier","11"),value=2,padx=10,pady=10,
                variable=self.var1)
    self.rb2.place(x=300,y=310)

    self.rb3= Radiobutton(parent, text=questions_answers[qnum][3], font=("Courier","11"), value=3,padx=10,pady=10,
                variable=self.var1)
    self.rb3.place(x=300,y=360)

    self.rb4= Radiobutton(parent, text=questions_answers[qnum][4], font=("Courier","11"), value=4,padx=10,pady=10,
                variable=self.var1)
    self.rb4.place(x=300,y=410)

    self.confirm_button = Button(parent, text="Confirm", font=("Courier","11"), bg="light blue", command=self.test_progress)
    self.confirm_button.place(x=450,y=300)   
      
    self.score_label=Label(parent, text="Score", font=("Helvetica", "17"))
    self.score_label.place(x=300,y=10)

    self.answer_label=Label(parent, font=("Courier", "14"))
    self.answer_label.place(x=300,y=110)


  def questions_setup(self):
    randomiser()
    self.var1.set(0)
    self.question_label.config(text=questions_answers[qnum][0])
    self.rb1.config(text=questions_answers[qnum][1])
    self.rb2.config(text=questions_answers[qnum][2])
    self.rb3.config(text=questions_answers[qnum][3])
    self.rb4.config(text=questions_answers[qnum][4])    

      
           




  




if __name__ == "__main__":
    root = Tk()
    root.title("The Music Quiz") 
    root.geometry("700x450")
    bg_image = Image.open("images/home_screen.png") #need to use Image if need to resize 
    bg_image = bg_image.resize((700, 450), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image) 
          #label for image
    image_label= Label(root, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always

    quiz_instance = UserEnterQuiz(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear

