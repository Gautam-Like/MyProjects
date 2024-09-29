from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom

class HotelManagementSystem:
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
        
        # Menu
        lbl_menu = Label(main_frame, text="MENU", font=("serif", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)
        
        # Button frame
        btn_frame = Frame(main_frame, bd=4, relief=SUNKEN)
        btn_frame.place(x=0, y=35, width=228, height=190)
        
        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=22, font=("serif", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        cust_btn.grid(row=0, column=0, pady=1)
        
        room_btn = Button(btn_frame, text="ROOM",command=self.roombooking, width=22, font=("serif", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)
        
        detail_btn = Button(btn_frame, text="DETAILS",command=self.details_room, width=22, font=("serif", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        detail_btn.grid(row=2, column=0, pady=1)
        
        # reports_btn = Button(btn_frame, text="REPORTS", width=22, font=("serif", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        # reports_btn.grid(row=3, column=0, pady=1)
        
        logout_btn = Button(btn_frame, text="LOGOUT", width=22, font=("serif", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        logout_btn.grid(row=4, column=0, pady=1)
        
        # RIGHT SIDE IMAGE
        img3 = Image.open(r"C:\Users\ARJUN\Pictures\_dc136877-53bf-4c54-96d6-dfc0c0483966.jpg")
        img3 = img3.resize((1310, 590), Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(main_frame, image=self.photoimg3, bd=4, relief=SUNKEN)
        lblimg3.place(x=225, y=0, width=1060, height=510)
        
        # Down images
        img4 = Image.open(r"C:\Users\ARJUN\Pictures\HD-wallpaper-food-indian-food-chicken-soup-thumbnail.jpg")
        img4 = img4.resize((230, 210), Image.ADAPTIVE)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lblimg4 = Label(main_frame, image=self.photoimg4, bd=4, relief=SUNKEN)
        lblimg4.place(x=0, y=185, width=230, height=175)
        
        img5 = Image.open(r"C:\Users\ARJUN\Pictures\festive-indian-food-with-rice-and-chicken-i39qrhkpvunqe0hb.jpg")
        img5 = img5.resize((230, 190), Image.ADAPTIVE)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lblimg5 = Label(main_frame, image=self.photoimg5, bd=4, relief=SUNKEN)
        lblimg5.place(x=0, y=355, width=230, height=175)
        
    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)
        
    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)
        
        
    def details_room(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)
        
        
        
        

if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
