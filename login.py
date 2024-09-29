from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from hotel import HotelManagementSystem



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
      
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\ARJUN\Pictures\festive-indian-food-with-rice-and-chicken-i39qrhkpvunqe0hb.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=465,y=140,width=340,height=450)
        
        #frame
        img2=Image.open(r"C:\Users\ARJUN\Pictures\WhatsApp Image 2024-03-08 at 20.09.14_66fe1a2c1.jpg")
        img2=img2.resize((100,100),Image.ADAPTIVE)
        self.photoimage1=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage1,bg="blue",borderwidth=0)
        lblimg2.place(x=585,y=145,width=100,height=100)
        
        
        get_str=Label(frame,text="Get started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
        
        # label
        
        username=lbl=Label(frame,text="Username",font=("times new roman",20,"bold"),fg="white",bg="black")
        username.place(x=70,y=145)
        self.txtuser=ttk.Entry(frame,font=("time new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        
        password=lbl=Label(frame,text="Password",font=("times new roman",20,"bold"),fg="white",bg="black")
        password.place(x=70,y=215)
        self.txtpass=ttk.Entry(frame,font=("time new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        #icon images
        
        img2=Image.open(r"C:\Users\ARJUN\Pictures\WhatsApp Image 2024-03-08 at 20.09.14_66fe1a2c1.jpg")
        img2=img2.resize((25,25),Image.ADAPTIVE)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="blue",borderwidth=0)
        lblimg2.place(x=505,y=290,width=25,height=25)
        
        img3=Image.open(r"C:\Users\ARJUN\Pictures\lockscrn.jpg")
        img3=img3.resize((25,25),Image.ADAPTIVE)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="blue",borderwidth=0)
        lblimg3.place(x=505,y=360,width=25,height=25)
        
        #login
        loginbtn=Button(frame,text="Login",command=self.login,font=("time new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red", activeforeground="white",activebackground="black")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        loginbtn=Button(frame,text="New user Register",command=self.rigister_window,font=("time new roman",13,"bold"),fg="white",bg="black", activeforeground="white",activebackground="black")
        loginbtn.place(x=20,y=350,width=160)
        
        loginbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("time new roman",13,"bold"),fg="white",bg="black", activeforeground="white",activebackground="black")
        loginbtn.place(x=20,y=400,width=160)
        
    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "arjun" and self.txtpass.get() == "arjun123":
            messagebox.showinfo("Success", "Welcome to Hotel")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="arjun123",database="sys")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                         self.txtuser.get(),
                         self.txtpass.get()
            
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username And password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            # reset password
            
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security Question ")
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer")
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="arjun123",database="sys")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer")
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset ,please login new password")
        
            
            
            
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="arjun123",database="sys")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("My error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+465+170")
                l=Label(self.root2,text="Forget Password",font="serif 15 bold",fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                
                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)
                
                self.combo_security_Q = ttk.Combobox(self.root2, width=20, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your birth place","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
                
                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)
                
                
                new_password_A=Label(self.root2,text="New password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password_A.place(x=50,y=220)
                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_new_password.place(x=50,y=250,width=250)
                
                btn=Button(self.root2,text="Rest",command=self.reset_pass,font=("times new roman",15,"bold"),bg="green",fg="white")
                btn.place(x=100,y=290)
                
                
                        
                
            
            
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("register")
        self.root.geometry("1600x900+0+0")
        
        # variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()
        
        # bg image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\ARJUN\Pictures\festive-indian-food-with-rice-and-chicken-i39qrhkpvunqe0hb.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        #left image
        
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\ARJUN\Pictures\festive-indian-food-with-rice-and-chicken-i39qrhkpvunqe0hb.jpg")
        lbl_bg1=Label(self.root,image=self.bg1)
        lbl_bg1.place(x=50,y=100,width=470,height=500)
        
        
        # main frame
        
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=700,height=550)
        
        register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)
        
        #label and entry
        # row 1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)
        
        #row 2
        
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)
        
        #row 3
        
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ, width=20, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your birth place","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)
        
        #row 4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        
        # check button
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree terms and condition",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380,width=250)
        
        #button
        
        loginbtn=Button(frame,text="REGISTER NOW",command=self.register_data,font=("time new roman",13,"bold"),fg="white",bg="black", activeforeground="white",activebackground="black",cursor="hand2")
        loginbtn.place(x=50,y=430,width=250)
        
        loginbtn=Button(frame,text="LOGIN NOW",font=("time new roman",13,"bold"),fg="white",bg="black", activeforeground="white",activebackground="black",cursor="hand2")
        loginbtn.place(x=370,y=430,width=250)
        
        # function declaration
        
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")   
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="arjun123",database="sys")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already  exist,Please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                    self.var_fname.get(),
                                                    self.var_lname.get(),
                                                    self.var_contact.get(),
                                                    self.var_email.get(),
                                                    self.var_securityQ.get(),
                                                    self.var_securityA.get(),
                                                    self.var_pass.get()
                   
        
                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")
        
        
        
        
if __name__== "__main__":
     main()
    