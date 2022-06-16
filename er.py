def name_collection_check(self):

    if len(names) == 0:
        msg = 'name can\'t be empty'
        UserEnterQuiz(root)
    else:
        try:
            if any(ch.isdigit() for ch in name):
                msg = 'Name can\'t have numbers'
                UserEnterQuiz(root)
                
            elif len(name) <= 2:
                msg = 'name is too short.'
                UserEnterQuiz(root)
            elif len(name) > 100:
                msg = 'name is too long.'
                UserEnterQuiz(root)
             
            else:
                msg = 'Success!'
        except Exception as ep:
            messagebox.showerror('error', ep)
        
    messagebox.showinfo('message', msg)