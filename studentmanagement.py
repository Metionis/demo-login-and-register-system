##library ipmort
from tkinter import *
from datetime import date
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl, xlrd
from openpyxl import Workbook
import pathlib

background = "#06283D" 
framebg = "#EDEDED"
framefg = "#06283D"

root = Tk()
root.title("Student Registration System")
root.geometry("1530x850")
root.config(bg= background)

file = pathlib.Path('student_data.xlsx')
if file.exists():
    pass
else:
    file = Workbook()
    sheet = file.active()
    sheet['A1'] = "Registration No."
    sheet['B1'] = "Name"
    sheet['C1'] = "Class"
    sheet['D1'] = "Gender"
    sheet['E1'] = "DOB"
    sheet['F1'] = "Date Of Registration"
    sheet['G1'] = "Religion"
    sheet['H1'] = "Skill"
    sheet['I1'] = "Father Name"
    sheet['J1'] = "Mother Name"
    sheet['K1'] = "Father's Occupation"
    sheet['L1'] = "Mother's Occupation"
    
    file.save("Student_Data.xlsx")
    
##top frames
Label(root, text = "abcdxyz@gmail.com", width = 10, height = 3, bg = '#f0687c', anchor ='e').pack(side = TOP, fill = X)
    








root.mainloop()