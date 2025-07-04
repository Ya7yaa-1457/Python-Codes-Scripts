from tkinter import *  # Start
window = Tk()  # set up

photo = PhotoImage(
    file='C:\\Users\\yahya\\Downloads\\image-removebg-preview_optimized.png')

window.geometry("210x210")  # Size
window.title("Yahya")  # Title name
# Pick Icon ( name & insert icon)
icon = PhotoImage(
    file='C:\\Users\\yahya\\Downloads\\image-removebg-preview_optimized.png')
window.iconphoto(True, icon)  # Icon - On
window.config(background="black")  # Change Background Color

label = Label(window, text="Hello World", font=('Georgia', 20, 'bold'), fg='white',
              bg='black', relief=RAISED, bd=10, padx=10, pady=10, image=photo, compound=BOTTOM)
label.place(x=0, y=0)


window.mainloop()  # place a window on the computer screen

# text is the text that u want to put inside the GUI
# font customize
# fg is the text Color
# bg background of the Text
# relief is the lines outside the text
# padx is the spacing of the lines x , y
# compound is the position of the picture
