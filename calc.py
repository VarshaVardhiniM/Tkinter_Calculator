import tkinter as tk

#Button click handler
def press(v):
    entry.insert(tk.END,v)
    
#Clear function
def clear():
    entry.delete(0,tk.END)
    
#Calculation function
def Calc():
    try:
        result=eval(entry.get())
        """entry.get() retrives the expression, eval() evaluates the string as a python expression"""
        
        entry.delete(0,tk.END) #Clears the old expression
        entry.insert(0,result) #Displays the result of expression
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Invalid Expression")
        """"Handles invalid expressions (e.g. 5++), displays "error" instead of crashing"""
        
#Main Window creation
root=tk.Tk() 
"""It creates the main application Window"""
root.title("Calculator")
root.configure(bg="#1e1e1e")
root.resizable(False,False)

#Entry Widgets (Display Screen)
entry=tk.Entry(root,font=("Times new Roman",20),bg="#2d2d2d",fg="white",bd=0,justify="right")
entry.grid(row=0,column=0,columnspan=4,padx=12,pady=12,ipady=10)
'''Place entry at top
columnspan=4 makes it streach across 4 Columns'''

# Button labels
buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+",
]

#Dynamic Button Creation
r=1
c=0
'''Rows and Column counters for grid layout'''
for b in buttons:
    cmd=Calc if b=="=" else lambda x=b: press(x)
    tk.Button(root,text=b,command=cmd,font=("Calibri",14),width=5,height=2,bg="#ff9500" if b in "+-*/" else "#3a3a3a",fg="white",bd=0).grid(row=r,column=c,padx=6,pady=6)
    
    c+=1
    #After 4 columns, move to next row
    if c==4:
        r+=1
        c=0
    #Moves to next row after 4 buttons
    
# Clear button
tk.Button(root, text="C", font=("Calibri", 14), bg="#f3bf3b",command=clear, width=22, height=2,bd=0).grid(row=r, column=0, columnspan=4, pady=8)

# Run the application (Event Loop)
root.mainloop()
    