import pandas as pd
import numpy as np
from tkinter import *
from tkinter import messagebox

# ------Load csv ------
try:
    data = pd.read_csv("salary.csv")
except:
    sample = pd.DataFrame({"salary": [25000,45000,67000,4567,23478,90567,45675]})
    sample.to_csv("salary.csv",index=False)
    data = pd.read_csv("salary.csv")

# try and except are keywords in python for exception handling 
# what is exception =exception is an error that occurs during program e.g file not found,division by zero,invalid input
#sample is a pandas dataframe 
# to_csv() is a pandas function it converts DataFrame into csv file 
#index=false by default pandas also saves index numbers so we don't want index number so we write false here

data.columns = data.columns.str.strip().str.lower()
salary = np.array(data["salary"])

salary = np.array(data["salary"])
#takes salary columns from dataframe named data then it converts it into numpy array and store in variable named salary

#-------Tkinter Window---------
# Tk() is a class from tkinter library it represents the main application window
root = Tk()
root.title("Salary Data Analysis")
root.geometry("500x500")

Label(root, text="Salary Data Analysis System", font =("Arial",16,"bold")).pack(pady=10)
#label will create a heading on our window
result = Text(root,height=12,width=55)
result.pack()
#Create a big text area inside window and display it on screen.”

#------Functions---

def show_statistics():
    result.delete(1.0,END)

    text = f"""
Average Salary : {np.mean(salary)}
Highest Salary : {np.max(salary)}
Lowest  Salary : {np.min(salary)}
Total   Salary : {np.sum(salary)}
std Deviation  : {np.std(salary)}
"""
    result.insert(END, text)
#result.delete(1.0,END) result is our multi-line text area delete(start,end) delete function removes text from the text box
# 1.0 is the index position in text widget here 1 is line number and 0 is character positiin =line.character
# end is constant means till the end of all the content
# result.delete(1.0, END) clears all text from the Tkinter Text widget starting from first character to the last character
# f""" starts a formatted multi-line string where variables and expressions can be inserted using { }.
# result.insert(END, text) New content goes after existing content

def increament_salary():
    data["Increamented Salary"] = salary + salary * 0.10
    messagebox.showinfo("Success", "10% Increament Added")

def yearly_salary():
    data["Yearly Salary"] = salary * 12
    messagebox.showinfo("Success", "Yearly Salary Added")

def filter_high_salary():
    high = data[data["salary"] > 30000]
    result.delete(1.0,END)
    result.insert(END, str(high))

def sort_salary():
    sorted_data = data.sort_values("salary" ,ascending=False)
    result.delete(1.0,END)
    result.insert(END, str(sorted_data))

def add_new_salary():
    s = int(Entry.get())
    data.loc[len(data)] = [s]
    messagebox.showinfo("Added","Salary Added Successfully")

def save_file():
    data.to_csv("updated_salary.csv" , index=False)
    messagebox.showinfo("Saved", "updated_salary.csv Created")
def future():
    messagebox.showinfo("Future Enhancements",
     "* Graphs using matplotlib\n"
     "* Excel support\n"
     "* Department wise salary\n"
     "* Flask Web App")

#-------GUI Widgets----------

Button(root, text="Show Statistics",
       command=show_statistics).pack(pady=3)
              
Button(root, text="10% Increament",
       command=increament_salary).pack(pady=3)

Button(root, text="Yearly Salary",
       command=yearly_salary).pack(pady=3)

Button(root, text="Filter > 30000",
       command=filter_high_salary).pack(pady=3)

Button(root, text="Sort Salary",
       command=sort_salary).pack(pady=3)

Button(root, text="Save CSV",
       command=save_file).pack(pady=3)

Button(root, text="Future Enhancements",
       command=future).pack(pady=3)

root.mainloop()
              

              

              

              

              

              



    


