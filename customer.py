from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Cust_Win:
    def __init__(self, root):
        self.root = root  
        self.root.title("Hotel Management System")
        self.root.geometry("1050x500+225+220")   # 1050x480+230+220
                
        #==================== variables ===========
        self.var_ref=StringVar()
        x=random.randint(1000,99999)
        self.var_ref.set(str(x))
        
        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_address=StringVar()

        #=============== title===================
        
        lbl_title = Label(self.root, text="Add Customer Details", font=("serif", 15, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1050, height=30)
        
        # img2 = Image.open("C:/Users/ARJUN/Pictures/_50f25245-143a-4491-834e-9997a9d55aef.jpg")
        # img2 = img2.resize((100, 45), Image.ADAPTIVE)
        # self.photoimg2 = ImageTk.PhotoImage(img2)
        # lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=SUNKEN)
        # lblimg2.place(x=5, y=2, width=100, height=45)
        
        # Label frame left
        labelframeleft = LabelFrame(self.root, bd=4, relief=RIDGE, text="Customer Details", font=("serif", 10, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=350, height=410)
        
        # Customer Ref
        cust_ref = Label(labelframeleft, text="Customer Ref", font=("serif", 10, "bold"), padx=2, pady=6)
        cust_ref.grid(row=0, column=0, sticky=W)
        entry_ref = ttk.Entry(labelframeleft,textvariable=self.var_ref, width=29, font=("serif", 10, "bold"),state="readonly")
        entry_ref.grid(row=0, column=1)
        
        # Customer Name
        cust_name = Label(labelframeleft, text="Customer Name", font=("serif", 10, "bold"), padx=2, pady=6)
        cust_name.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(labelframeleft,textvariable=self.var_cust_name, width=29, font=("serif", 10, "bold"))
        txtcname.grid(row=1, column=1)
        
        # Mother Name
        Mother_name = Label(labelframeleft, text="Mother Name", font=("serif", 10, "bold"), padx=2, pady=6)
        Mother_name.grid(row=2, column=0, sticky=W)
        txtmname = ttk.Entry(labelframeleft,textvariable=self.var_mother, width=29, font=("serif", 10, "bold"))
        txtmname.grid(row=2, column=1)
        
        # Gender combobox
        cust_gender = Label(labelframeleft, text="Gender", font=("serif", 10, "bold"), padx=2, pady=6)
        cust_gender.grid(row=3, column=0, sticky=W)
        gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender,width=27, font=("serif", 10, "bold"), state="readonly")
        gender["values"] = ("Male", "Female", "Other")
        gender.grid(row=3, column=1)
        
        # Postcode
        postcode = Label(labelframeleft, text="Postcode", font=("serif", 10, "bold"), padx=2, pady=6)
        postcode.grid(row=4, column=0, sticky=W)
        txt_postcode = ttk.Entry(labelframeleft,textvariable=self.var_post, width=29, font=("serif", 10, "bold"))
        txt_postcode.grid(row=4, column=1)
        
        # Mobile Number
        mobile = Label(labelframeleft, text="Mobile Number", font=("serif", 10, "bold"), padx=2, pady=6)
        mobile.grid(row=5, column=0, sticky=W)
        txt_mobile = ttk.Entry(labelframeleft,textvariable=self.var_mobile, width=29, font=("serif", 10, "bold"))
        txt_mobile.grid(row=5, column=1)
        
        # Email Id
        email_id = Label(labelframeleft, text="Email Id", font=("serif", 10, "bold"), padx=2, pady=6)
        email_id.grid(row=6, column=0, sticky=W)
        txt_email = ttk.Entry(labelframeleft,textvariable=self.var_email, width=29, font=("serif", 10, "bold"))
        txt_email.grid(row=6, column=1)
        
        # Nationality
        nationaliry= Label(labelframeleft, text="Nationality", font=("serif", 10, "bold"), padx=2, pady=6)
        nationaliry.grid(row=7, column=0, sticky=W)
        nationaliry= ttk.Combobox(labelframeleft,textvariable=self.var_nationality, width=27, font=("serif", 10, "bold"), state="readonly")
        nationaliry["values"] = ("Indian", "American", "Britist")
        nationaliry.grid(row=7, column=1)
                
        # Idproof type combobox
        id_proof_type = Label(labelframeleft, text="ID Proof Type", font=("serif", 10, "bold"), padx=2, pady=6)
        id_proof_type.grid(row=8, column=0, sticky=W)
        id_proof = ttk.Combobox(labelframeleft,textvariable=self.var_id_proof, width=27, font=("serif", 10, "bold"), state="readonly")
        id_proof["values"] = ("Aadhar Card", "Voter ID","Passport", "Driving License", )
        id_proof.grid(row=8, column=1)
        
        # Id number
        id_number = Label(labelframeleft, text="ID Number", font=("serif", 10, "bold"), padx=2, pady=6)
        id_number.grid(row=9, column=0, sticky=W)
        txt_id_number = ttk.Entry(labelframeleft,textvariable=self.var_id_number, width=29, font=("serif", 10, "bold"))
        txt_id_number.grid(row=9, column=1)
        
        # Address
        address = Label(labelframeleft, text="Address", font=("serif", 10, "bold"), padx=2, pady=6)
        address.grid(row=10, column=0, sticky=W)
        txt_address = ttk.Entry(labelframeleft, textvariable=self.var_address,width=29,  font=("serif", 10, "bold"))
        txt_address.grid(row=10, column=1)
        
        #============= Buttons==============
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=350)
        btnadd=Button(btn_frame,text="add",command=self.add_data,font=("serif", 10, "bold"),bg="black",fg="gold",width=8)
        btnadd.grid(row=0,column=0,padx=3)
        
        btnadd=Button(btn_frame,text="update",command=self.update,font=("serif", 10, "bold"),bg="black",fg="gold",width=8)
        btnadd.grid(row=0,column=1,padx=3)
        
        btnadd=Button(btn_frame,text="delete",command=self.mDelete,font=("serif", 10, "bold"),bg="black",fg="gold",width=8)
        btnadd.grid(row=0,column=2,padx=3)
        
        btnadd=Button(btn_frame,text="reset",command=self.reset,font=("serif", 10, "bold"),bg="black",fg="gold",width=8)
        btnadd.grid(row=0,column=3,padx=3)
        
         # tabel Label frame search
        table_frame = LabelFrame(self.root, bd=4, relief=RIDGE, text="view details and search", font=("serif", 10, "bold"), padx=2)
        table_frame.place(x=360, y=50, width=670, height=410)
        
        search= Label(table_frame, text="search by:", font=("serif", 10, "bold"),bg="red",fg="white")
        search.grid(row=0, column=0, sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_search = ttk.Combobox(table_frame,textvariable=self.search_var, width=20, font=("serif", 10, "bold"), state="readonly")
        combo_search["values"] = ("mob", "Ref no")
        combo_search.current(0)
        combo_search.grid(row=0, column=1)
        
        self.txt_search=StringVar()
        txt_search = ttk.Entry(table_frame, textvariable=self.txt_search,width=20, font=("serif", 10, "bold"))
        txt_search.grid(row=0, column=2,padx=2)
        
        btnsearch=Button(table_frame,text="search",command=self.search,font=("serif", 10, "bold"),bg="black",fg="gold",width=8)
        btnsearch.grid(row=0,column=3,padx=3)
        
        btnshow_all=Button(table_frame,text="Show All",command=self.fetch_data,font=("serif", 10, "bold"),bg="black",fg="gold",width=8)
        btnshow_all.grid(row=0,column=4,padx=3)
        
        #=============== show data table ==============
        details_table_frame=Frame(table_frame,bd=2,relief=RIDGE)
        details_table_frame.place(x=0,y=50,width=650,height=310)
        
        scroll_x=ttk.Scrollbar(details_table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table_frame,orient=VERTICAL)
        
        self.Cust_details_table=ttk.Treeview(details_table_frame,column=("ref","name",
                                                                          "mother","gender",
                                                                          "post","mobile","email","nationality",
                                                                          "idproof","idnumber","address"),
                                             xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Cust_details_table.xview)
        scroll_y.config(command=self.Cust_details_table.yview)
        
        self.Cust_details_table.heading("ref",text="Refer No")
        self.Cust_details_table.heading("name",text="Name")
        self.Cust_details_table.heading("mother",text="Mother Name")
        self.Cust_details_table.heading("gender",text="Gender")
        self.Cust_details_table.heading("post",text="Postcode")
        self.Cust_details_table.heading("mobile",text="Mobile")
        self.Cust_details_table.heading("email",text="Email")
        self.Cust_details_table.heading("nationality",text="Nationality")
        self.Cust_details_table.heading("idproof",text="Id proof")
        self.Cust_details_table.heading("idnumber",text="Id number")
        self.Cust_details_table.heading("address",text="Address")
        
        self.Cust_details_table["show"]="headings"
        
        self.Cust_details_table.column("ref",width=100)
        self.Cust_details_table.column("name",width=100)
        self.Cust_details_table.column("mother",width=100)
        self.Cust_details_table.column("gender",width=100)
        self.Cust_details_table.column("post",width=100)
        self.Cust_details_table.column("mobile",width=100)
        self.Cust_details_table.column("email",width=100)
        self.Cust_details_table.column("nationality",width=100)
        self.Cust_details_table.column("idproof",width=100)
        self.Cust_details_table.column("idnumber",width=100)
        self.Cust_details_table.column("address",width=100)
       
        self.Cust_details_table.pack(fill=BOTH,expand=1)
        self.Cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data() 
      
            # add function
    def add_data(self):
            if (self.var_mobile.get() == "" or self.var_mother.get() == "" or self.var_cust_name.get() == "" or 
            self.var_gender.get() == "" or self.var_post.get() == "" or self.var_email.get() == "" or 
            self.var_nationality.get() == "" or self.var_address.get() == "" or self.var_id_proof.get() == "" or 
            self.var_id_number.get() == ""):
               messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                try:
                   conn = mysql.connector.connect(host="localhost", username="root", password="arjun123", database="sys")
                   my_cursor = conn.cursor()
                   my_cursor.execute("INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                                  (self.var_ref.get(), 
                                   self.var_cust_name.get(), 
                                   self.var_mother.get(),
                                   self.var_gender.get(), 
                                   self.var_post.get(), 
                                   self.var_mobile.get(),
                                   self.var_email.get(), 
                                   self.var_nationality.get(), 
                                   self.var_id_proof.get(), 
                                   self.var_id_number.get(),
                                   self.var_address.get()
                                   ))
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Success", "Customer has been added", parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
                    
            # fetch data function           
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="arjun123", database="sys")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            for i in rows:
                self.Cust_details_table.insert("",END,values=i)
        conn.commit()
        conn.close()
        
                        
    def get_cursor(self,event=""):
        cursor_row=self.Cust_details_table.focus()
        content=self.Cust_details_table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])
        
        
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
            
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="arjun123", database="sys")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,idnumber=%s,Address=%s where Ref=%s",(
                                                
                                                self.var_cust_name.get(), 
                                                self.var_mother.get(),
                                                self.var_gender.get(), 
                                                self.var_post.get(), 
                                                self.var_mobile.get(),
                                                self.var_email.get(), 
                                                self.var_nationality.get(), 
                                                self.var_id_proof.get(), 
                                                self.var_id_number.get(),
                                                self.var_address.get(),
                                                self.var_ref.get(),    
                                                   ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfullly",parent=self.root)
            
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel management Sytem","Do you want delete this customer",parent=self.root)
        if mDelete>0:
           conn = mysql.connector.connect(host="localhost", username="root", password="arjun123", database="sys")
           my_cursor = conn.cursor()
           query="delete from customer where Ref=%s"
           value=(self.var_ref.get(),)
           my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
        
    def reset(self):
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        # self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
       
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="arjun123", database="sys")
        my_cursor = conn.cursor()
        
        # Get the selected search criteria and the search text
        search_criteria = self.search_var.get()
        search_text = self.txt_search.get()
        
        # Check if search text is empty
        if search_text.strip() == "":
            messagebox.showwarning("Warning", "Please enter search text", parent=self.root)
            return
        
        # Define the SQL query based on the selected search criteria
        if search_criteria == "mob":
            sql_query = "SELECT * FROM customer WHERE mobile LIKE '%" + search_text + "%'"
        elif search_criteria == "Ref no":
            sql_query = "SELECT * FROM customer WHERE ref LIKE '%" + search_text + "%'"
        else:
            messagebox.showerror("Error", "Invalid search criteria", parent=self.root)
            return
        
        try:
            my_cursor.execute(sql_query)
            rows = my_cursor.fetchall()
            
            # Clear the table before inserting new search results
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            
            # Insert search results into the table
            for row in rows:
                self.Cust_details_table.insert("", END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error in executing SQL query: {str(e)}", parent=self.root)
        
        conn.close()
            
if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
