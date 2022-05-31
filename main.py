from tkinter import *
from PIL import Image, ImageTk
names = []

class Quiz:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
 
        background_color="white"
      
        self.heading_label=Label(parent, text="", font=("Tw Cen MT","18","bold"))
        self.heading_label.grid(row=0) 

        #label for username
        self.user_label=Label(parent, text="", font=("Tw Cen MT","16"),bg=background_color)
        self.user_label.place(x=50,y=230)
        
        #entry box
        self.entry_box=Entry(parent)
        self.entry_box.place(x=225,y=315) 
        
        #continue button
        self.continue_button = Button(parent, text="Continue", font=("Helvetica", "35", "bold"), bg="light blue", command=self.name_collection)
        self.continue_button.place(x=208,y=365)       
       

    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #add name to names list declared at the beginning
        #self.quiz_frame.destroy() #Destroy name frame then open the quiz runner
      
           

if __name__ == "__main__":
    root = Tk()
    root.title("NZ Road Rules Quiz") 
    root.geometry("700x450")
    bg_image = Image.open("images/home_screen.png") #need to use Image if need to resize 
    bg_image = bg_image.resize((700, 450), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image) 
          #label for image
    image_label= Label(root, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always

    quiz_instance = Quiz(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear

