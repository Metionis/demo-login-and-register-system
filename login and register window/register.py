from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from mysql import connector
######################################################
background = '#06283D'
framebg = '#EDEDED'
framefg = '#06283D'

##root create and determine the size of the window of register
root = Tk()
root.title('Register system')
root.geometry("1600x900")

root.config(bg=background)
root.resizable(False, False)

##Register function
def register():
    ##Get the username, password and admincode that user type in the entry
    username = user.get()
    password = code.get()
    admincode = adminaccess.get()
    
    ##Give an admincode equal to 12345
    ##if it true then go to next case
    if admincode == '12345':
        ##if username is left blank or it similar as default value or password is blank or equal to
        ##first existed then show the error messagebox
        if (username == "" or username == "UserId") or (password=="" or password == "Password"):
            messagebox.showerror("Entry Error!", "Type username or password")
        
        ##if not
        else:
            ##try to connect to MySQL
            try:
                mydb = mysql.connector.connect(host="localhost", user="root",password= "Quanlatui777", database="studentregistration")
                mycursor = mydb.cursor()
                print("Connection Established")
                
            except:
                messagebox.showerror("Connection", "Database connection is not established")
            
            # command = "use studentregsitration"
            # mycursor.execute(command)
            
            # mydb = mysql.connector.connect(host= 'localhost',user = 'root', password= "Quanlatui777", database = "studentregsitration")
            # mycursor = mydb.cursor()
                
            command = "insert into login(Username, Password) VALUES(%s, %s)"
            mycursor.execute(command, (username, password))
            mydb.commit()
            mydb.close()
            messagebox.showinfo("Register", "New user is added")
            
            ##Connect to database
            # try:     
                # command = "CREATE DATABASE StudentRegsitration"
                # mycursor.execute(command)
                
                # command = "use studentregsitration"
                # mycursor.execute(command)
                
                # command = "create table login(user int auto_increment key not null, Username varchar(50), Password VARCHAR(100))"
                # mycursor.execute(command)
            # except:
                # mycursor.execute("use StudentRegsitration")
                # mydb = mysql.connector.connect(host= 'localhost',user = 'root', password= "Quanlatui777", database = "StudentRegsitration")
                # mycursor = mydb.cursor()
                
                # command = "insert into login(Username, Password) VALUES(%s, %s)"
                # mycursor.execute(command, (username, password))
                # mydb.commit()
                # mydb.close()
                # messagebox.showinfo("Register", "New user is added")
                
    #Other
    else:
        messagebox.showerror("Admin code!", "You are not admin")



def back_to_login():
    root.destroy() #close current window
    import login


#icon image
image_icon = PhotoImage(file = "demo-login-page\images\lolo.png")
root.iconphoto(False, image_icon)

#background image
frame= Frame(root,bg="red")
frame.pack(fill = Y)

backgroundimage = ImageTk.PhotoImage(Image.open('demo-login-page\images\qbackgroundimage.png'))
Label(frame, image = backgroundimage).pack()

adminaccess = Entry(frame, width = 20, fg="#000", border = 0, bg="#e8ecf7", font = ("Arial", 20), show ="*")
adminaccess.focus()
adminaccess.place(x = 260, y = 410)

#########user entry

user = Entry(frame, width = 20, fg="#fff", bg = "#375174", border=0, font = ("Arial", 20))

def user_enter (e):
    user.delete(0 ,'end')

def user_leave (e):
    name = user.get()
    if name == '':
        user.insert(0, 'UserId')
        
user.insert(0, "UserId")
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)

user.place(x = 260, y = 222)



###password entry
code = Entry(frame, width=20, fg= '#fff', border = 0, bg = '#375174', font = ("Arial", 20))

def code_enter (e):
    code.delete(0 ,'end')

def code_leave (e):
    passwd = code.get()
    if passwd == '':
        code.insert(0, 'Password')


code.insert(0, 'Password')
code.bind("<FocusIn>", code_enter)
code.bind("<FocusOut>", code_leave)
code.place(x = 260, y = 320)


####Hide and show button
button_mode = True
def hide():
    global button_mode
    if code.cget("show") == "*":
        code.config(show="")
        eyeButton.config(text="Show")
        button_mode = False
    else:
        button_mode = True
        code.config(show="*")
        eyeButton.config(text="Hide")
        
eyeButton = Button(frame, bg="#375174", width= 4, text= "Hide", font="Arial", command=hide)
eyeButton.place(x = 570, y = 320)


###register button
regis_button = Button(root, text = "ADD NEW USER", bg = "#455c88", fg= "white", width = 13, height = 1, font = ("Arial", 16), bd = 0, command = register)
regis_button.place(x= 730, y = 525)


backbutton = Button(root, text = "BACK", bg = "#455c88", fg="white", width = 4, command = back_to_login)
backbutton.place(x = 460, y= 0)



root.mainloop()
