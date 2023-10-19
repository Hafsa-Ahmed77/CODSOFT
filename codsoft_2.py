from tkinter import *

def end_():
     from tkinter import messagebox
     messagebox.showinfo("end","YOU ENDED THE PROGRAM, HOPE YOU LIKED OUR SERVICE")
     exit()

def done():
     inputs=entry.get()
     if "+" in inputs:
          inp=inputs.split("+")
          ans=int(inp[0])+int(inp[1])
          entry.delete(0,END)
          entry.insert(0,ans)
     elif "-" in inputs:
          inp=inputs.split("-")
          ans=int(inp[0])-int(inp[1])
          entry.delete(0,END)
          entry.insert(0,ans)
     elif "x" in inputs:
          inp=inputs.split("x")
          ans=int(inp[0])*int(inp[1])
          entry.delete(0,END)
          entry.insert(0,ans)
     else :
          inp=inputs.split("÷")
          ans=int(inp[0])/int(inp[1])
          entry.delete(0,END)
          entry.insert(0,ans)
     

def delete():
     entry.delete(0,END)

def display(text):
     leng=len(entry.get())
     entry.insert(leng,text)
      
# forming gui window
r=Tk()
r.title("SIMPLE CALCULATOR")
# frame for digits and operators
main_frame=LabelFrame(r,bd=0)
main_frame.grid(row=3,column=3,padx=20,pady=2)
# frame to display inputs
display_frame=LabelFrame(r)
display_frame.grid(row=2,column=3,pady=5)
entry=Entry(display_frame,width=28)
entry.grid()
                                                                                                  
                                                                                                                    # SETTING BUTTONS OF CALCULATOR

# buttons for digits
Button(main_frame,text="1",font="arial 20",relief="sunken",bg="orange",command=lambda:display(1)).grid(row=0,column=0,padx=2,pady=2)
Button(main_frame,text="2",font="arial 20",relief="sunken",bg="orange",command=lambda:display(2)).grid(row=0,column=1,padx=2,pady=2)
Button(main_frame,text="3",font="arial 20",relief="sunken",bg="orange",command=lambda:display(3)).grid(row=0,column=2,padx=2,pady=2)
Button(main_frame,text="4",font="arial 20",relief="sunken",bg="orange",command=lambda:display(4)).grid(row=1,column=0,padx=2,pady=2)
Button(main_frame,text="5",font="arial 20",relief="sunken",bg="orange",command=lambda:display(5)).grid(row=1,column=1,padx=2,pady=2)
Button(main_frame,text="6",font="arial 20",relief="sunken",bg="orange",command=lambda:display(6)).grid(row=1,column=2,padx=2,pady=2)
Button(main_frame,text="7",font="arial 20",relief="sunken",bg="orange",command=lambda:display(7)).grid(row=2,column=0,padx=2,pady=2)
Button(main_frame,text="8",font="arial 20",relief="sunken",bg="orange",command=lambda:display(8)).grid(row=2,column=1,padx=2,pady=2)
Button(main_frame,text="9",font="arial 20",relief="sunken",bg="orange",command=lambda:display(9)).grid(row=2,column=2,padx=2,pady=2)
Button(main_frame,text="0",font="arial 20",relief="sunken",bg="orange",command=lambda:display(0)).grid(row=3,column=1,padx=2,pady=2)

# button for operators
Button(main_frame,text="+",font="arial 20",relief="sunken",bg="black",fg="white",command=lambda:display("+")).grid(row=0,column=4,padx=2,pady=2)
Button(main_frame,text="-",font="arial 20",relief="sunken",width=2,bg="black",fg="white",command=lambda:display("-")).grid(row=1,column=4,padx=2,pady=2)
Button(main_frame,text="x",font="arial 20",relief="sunken",width=2,bg="black",fg="white",command=lambda:display("x")).grid(row=2,column=4,padx=2,pady=2)
Button(main_frame,text="÷",font="arial 20",relief="sunken",bg="black",fg="white",command=lambda:display("÷")).grid(row=3,column=4,padx=2,pady=2)
# button for clear text
Button(main_frame,text="Clear",font="arial 10",height=3,relief="sunken",bg="black",fg="white",command=delete).grid(row=3,column=0,padx=2,pady=2)

# button for answer
Button(main_frame,text="=",font="arial 20",relief="sunken",bg="black",fg="white",command=done).grid(row=3,column=2,padx=2,pady=2)

# button for ending program
Button(r,text="CLOSE",font="arial 10",relief="sunken",bg="black",fg="white",command=end_).grid(row=5,column=2,padx=2,pady=2)

