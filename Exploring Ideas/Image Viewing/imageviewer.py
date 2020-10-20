from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Learn to Code with Agonnee")



my_img1 = ImageTk.PhotoImage(Image.open("Images/1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("Images/2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Images/3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("Images/4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("Images/5.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]


my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def fwd(image_number):
    global my_label
    global button_fwd
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_fwd = Button(root, text=">>", command=lambda: fwd(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    my_label.grid(row=0, column=0, columnspan=3)

    if image_number == 5:
        button_fwd = Button(root, text=">>", state=DISABLED)

    status = Label(root, text="Image "+ str(image_number) +" of " + str(len(image_list)) + "   ", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    button_back.grid(row=1, column=0, padx=120)
    button_fwd.grid(row=1, column=2, padx=120)

def back(image_number):
    global my_label
    global button_fwd
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_fwd = Button(root, text=">>", command=lambda: fwd(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    my_label.grid(row=0, column=0, columnspan=3)

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)) + "   ", bd=1, relief=SUNKEN, anchor=E)

    button_back.grid(row=1, column=0, padx=120)
    button_fwd.grid(row=1, column=2)

status = Label(root, text="Image 1 of " + str(len(image_list)) + "   ", bd=1, relief=SUNKEN, anchor=E)

button_back = Button(root, text="<<", state=DISABLED)
button_quit = Button(root, text="Exit Program", command=root.quit)
button_fwd = Button(root, text=">>", command=lambda: fwd(2))

button_back.grid(row=1, column=0, padx=120)
button_quit.grid(row=1, column=1)
button_fwd.grid(row=1, column=2, padx=120)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
