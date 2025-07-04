from tkinter import *
window = Tk()
window.config(bg='black')
image = PhotoImage(file='Images/Tap2.png')
window.title("Yahya")
Icon = PhotoImage(
    file='C:\\Users\\yahya\\Downloads\\image-removebg-preview_optimized.png')
image2 = PhotoImage(file="Images/ClickProject2.png")


count = 0


def click():
    global count
    count += 1
    label.config(text=count)
    label2.pack()


button = Button(window, text='Click Here')
button.config(command=click)
button.pack()
button.config(font=('Ink Free', 50, 'bold'))
button.config(bg='black', fg='white')
button.config(activebackground='black')
button.config(activeforeground='white')
button.config(image=image, compound=BOTTOM)
button.config(state=ACTIVE)
label = Label(window, text=count)
label.pack()
label.config(font=('Ink Free', 50), bg='black', fg='white')
label2 = Label(window, image=image2)
label2.config(bg='black')
window.iconphoto(True, Icon)


window.mainloop()
