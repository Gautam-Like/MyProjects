from tkinter import *
from PIL import Image, ImageTk
# from customer import Cust_Win
# from room import Roombooking
# from details import DetailsRoom

class DetailsRoom:
    def __init__(self, root):
        self.root = root  
        self.root.title("Hotel Management System")
        self.root.geometry("1500x800+0+0")
        
        # First image
        img1 = Image.open(r"C:\Users\ARJUN\Pictures\pngtree-blue-royal-background-image_302413.jpg")
        img1 = img1.resize((1550, 140), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(self.root, image=self.photoimg1, bd=4, relief=SUNKEN)
        lblimg1.place(x=0, y=0, width=1550, height=140)
        
        # Logo
        img2 = Image.open(r"C:\Users\ARJUN\Pictures\letter-a-logo-vector-25576006.jpg")
        img2 = img2.resize((230, 140), Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=SUNKEN)
        lblimg2.place(x=0, y=0, width=230, height=140)
        
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("serif", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)
        
        # Main frame
        main_frame = Frame(self.root, bd=4, relief=SUNKEN)
        main_frame.place(x=0, y=190, width=1290, height=620)
        
if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()
