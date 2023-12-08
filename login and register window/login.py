##library import
from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from mysql import connector
background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

##variable
global trail_number
trail_number = 0

##trail function when the input is false
def trail():
    global trail_number
    
    trail_number = trail_number + 1
    print("Trail no is: ", trail_number)
    if trail_number == 3:
        root.destroy()
    else:
        messagebox.showwarning("Warning!", "If you try more than 3 times you will be blocked.")
        
##Login function
def loginuser():
    #When user type in username and password into the blanket box
    username = user.get()
    password = code.get()
    
    #The case that username is empty or equal to "user id" means same as default value also password
    #It will return a error box with the text
    if (username=="" or username=="user id") or (password=="" or password=="Password"):
        messagebox.showerror("Entry error", "Type username or Password")
    
    #if not try to connect to mySQL Database, if success then print the announce line    
    else:
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", password='Quanlatui777', database="studentregistration")
            mycursor = mydb.cursor()
            print("Connected to the Database!!")
            
    #if not success show the error box then stop the function
        except:
            messagebox.showerror("Connection", "Database connection not stablish")
            return
    
    command = "use studentregistration"
    mycursor.execute(command)
    
    command= "SELECT * FROM login WHERE Username=%s and Password=%s"
    mycursor.execute(command, (username, password))
    myresult = mycursor.fetchone()
    print(myresult)  
    
    if myresult == None:
        messagebox.showinfo("invalid", "invalid userid and password")
        trail()


def register():
    root.destroy()
    import register
    
    
     
root = Tk()
root.title("Login system")
root.geometry("1600x900")
root.config(bg = background)
root.resizable(False, False)

#icon image 
image_icon = PhotoImage(file="demo-login-page\images\lolo.png")
root.iconphoto(False, image_icon)

#background image
frame = Frame(root, bg = 'red')
frame.pack(fill = Y)

backgroundimage = ImageTk.PhotoImage(Image.open('demo-login-page\images\loginimage.png'))
Label(frame, image = backgroundimage).pack()

####user entry
user = Entry(frame, width=33, fg= '#fff', border = 0, bg = '#375174', font = ("Arial", 24))

def user_enter (e):
    user.delete(0 ,'end')

def user_leave (e):
    name = user.get()
    if name == '':
        user.insert(0, 'UserId')


user.insert(0, 'user id')
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x = 400, y = 315)


####password entry
code = Entry(frame, width=33, fg= '#fff', border = 0, bg = '#375174', font = ("Arial", 24))

def code_enter (e):
    code.delete(0 ,'end')

def code_leave (e):
    passwd = code.get()
    if passwd == '':
        code.insert(0, 'Password')


code.insert(0, 'Password')
code.bind("<FocusIn>", code_enter)
code.bind("<FocusOut>", code_leave)
code.place(x = 400, y = 383)

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
eyeButton.place(x = 950, y = 383)


##login button
loginButton = Button(root, text = "LOGIN", bg ="#1f5675", fg= "white", width= 10, height = 1, font= ("arial", 16, 'bold'), bd= 0, command= loginuser)
loginButton.place(x = 600, y = 450)

label = Label (root, text = "I don't have account", fg= '#fff', bg= "#00264d", font= ('Microsoft YaHei UI Light', 9))
label.place (x = 1000, y = 426)


registerButton = Button(root, text= "Add new user", bg = "#1f5675", fg= "white", width= 10, height = 1, font= ("arial", 16, 'bold'), bd= 0, command = register)
registerButton.place(x = 850, y = 450)

root.mainloop()