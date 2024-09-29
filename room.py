from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox


class Roombooking:
  def __init__(self, root):
    self.root = root  
    self.root.title("Hotel Management System")
    self.root.geometry("1050x500+225+220")   # 1050x480+230+220
        
        #========== variables==============
    
    self.var_roomavailable=StringVar()
    x=random.randint(1,101)
    self.var_roomavailable.set(str(x))    
        
    self.var_contact=StringVar()
    self.var_checkin=StringVar()
    self.var_checkout=StringVar()
    self.var_roomtype=StringVar()
    # self.var_roomavailable=StringVar()
    self.var_meal=StringVar()
    self.var_noOfdays=StringVar()
    self.var_paidtax=StringVar()
    self.var_actualtotal=StringVar()
    self.var_total=StringVar()

    lbl_title = Label(self.root, text="ROOM BOOKING", font=("serif", 15, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
    lbl_title.place(x=0, y=0, width=1050, height=30)
                
        # Label frame left
    labelframeleft = LabelFrame(self.root, bd=4, relief=RIDGE, text="Room Booking", font=("serif", 10, "bold"), padx=2)
    labelframeleft.place(x=5, y=50, width=350, height=410)
        
        # Customer contact
    lbl_cust_contact = Label(labelframeleft, text="Contact", font=("serif", 10, "bold"), padx=2, pady=6)
    lbl_cust_contact.grid(row=0, column=0, sticky=W)
    entry_contact = ttk.Entry(labelframeleft,textvariable=self.var_contact, width=18, font=("serif", 10, "bold"))
    entry_contact.grid(row=0, column=1,sticky=W)
          # fetch data 
    fetchData=Button(labelframeleft,text="fetch data",command=self.fetch_contact,font=("serif", 8, "bold"),bg="black",fg="gold",width=8)
    fetchData.place(x=240,y=4)
        
        # Check in date
    check_in_date = Label(labelframeleft, text="Check in date", font=("serif", 10, "bold"), padx=2, pady=6)
    check_in_date.grid(row=1, column=0, sticky=W)
    txtcheck_in_date = ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29, font=("serif", 10, "bold"))
    txtcheck_in_date.grid(row=1, column=1)
        
        # Check out date
    check_out_date = Label(labelframeleft, text="Check out date", font=("serif", 10, "bold"), padx=2, pady=6)
    check_out_date.grid(row=2, column=0, sticky=W)
    txtcheck_out_date = ttk.Entry(labelframeleft, textvariable=self.var_checkout,width=29, font=("serif", 10, "bold"))
    txtcheck_out_date.grid(row=2, column=1)
        
        # Room type
    label_Room_type = Label(labelframeleft, text="Room Type", font=("serif", 10, "bold"), padx=2, pady=6)
    label_Room_type.grid(row=3, column=0, sticky=W)
    combo_Roomtype = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, width=27, font=("serif", 10, "bold"), state="readonly")
    combo_Roomtype["values"] = ("Single", "Double", "Luxury")
    combo_Roomtype.current(0)
    combo_Roomtype.grid(row=3, column=1)
        
        # Available room
    lblRoomavailable = Label(labelframeleft, text="Available room", font=("serif", 10, "bold"), padx=2, pady=6)
    lblRoomavailable.grid(row=4, column=0, sticky=W)
    txtRoomavailable = ttk.Entry(labelframeleft,textvariable=self.var_roomavailable, width=29, font=("serif", 10, "bold"),state="readonly")
    txtRoomavailable.grid(row=4, column=1)
        
        # Meal
    lblmeal = Label(labelframeleft, text="Meal", font=("serif", 10, "bold"), padx=2, pady=6)
    lblmeal.grid(row=5, column=0, sticky=W)
    txtmeal = ttk.Combobox(labelframeleft,textvariable=self.var_meal, width=27, font=("serif", 10, "bold"),state="readonly")
    txtmeal["values"]=("Breakfast","Launch","Dinner")
    txtmeal.current(0)
    txtmeal.grid(row=5, column=1)
        
        # No of days
    lbl_noOfDays = Label(labelframeleft, text="No of days", font=("serif", 10, "bold"), padx=2, pady=6)
    lbl_noOfDays.grid(row=6, column=0, sticky=W)
    txtnoOfDays = ttk.Entry(labelframeleft,textvariable=self.var_noOfdays, width=29, font=("serif", 10, "bold"))
    txtnoOfDays.grid(row=6, column=1)
        
        # Paid Tax
    lblpaidTax = Label(labelframeleft, text="Paid tax", font=("serif", 10, "bold"), padx=2, pady=6)
    lblpaidTax.grid(row=7, column=0, sticky=W)
    txtpaidTax = ttk.Entry(labelframeleft,textvariable=self.var_paidtax, width=29, font=("serif", 10, "bold"))
    txtpaidTax.grid(row=7, column=1)
        
        # Sub total
    lblsubTotal = Label(labelframeleft, text="Sub total", font=("serif", 10, "bold"), padx=2, pady=6)
    lblsubTotal.grid(row=8, column=0, sticky=W)
    txtsubTotal = ttk.Entry(labelframeleft,textvariable=self.var_actualtotal, width=29, font=("serif", 10, "bold"))
    txtsubTotal.grid(row=8, column=1)
        
        # Total cost
    lbltotalCost = Label(labelframeleft, text="Total cost", font=("serif", 10, "bold"), padx=2, pady=6)
    lbltotalCost.grid(row=9, column=0, sticky=W)
    txttotalCost = ttk.Entry(labelframeleft,textvariable=self.var_total, width=29, font=("serif", 10, "bold"))
    txttotalCost.grid(row=9, column=1)
        
        #================= bill button
        
    billButton=Button(labelframeleft,text="Bill",command=self.total,font=("serif", 10, "bold"),bg="black",fg="gold",width=8)
    billButton.grid(row=10,column=0,padx=3,sticky=W)
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
        
        # right side image
    img3 = Image.open("C:/Users/ARJUN/Pictures/_9e391c19-c557-4722-891d-df88b67c8845_upscayl_4x_realesrgan-x4plus.png")
    img3 = img3.resize((380, 200), Image.ADAPTIVE)
    self.photoimg3 = ImageTk.PhotoImage(img3)
    lblimg3 = Label(self.root, image=self.photoimg3, bd=0, relief=SUNKEN)
    lblimg3.place(x=680, y=55, width=350, height=180)
        
           # tabel Label frame search system
    table_frame = LabelFrame(self.root, bd=4, relief=RIDGE, text="view details and search", font=("serif", 10, "bold"), padx=2)
    table_frame.place(x=360, y=240, width=670, height=220)
        
    search= Label(table_frame, text="search by:", font=("serif", 10, "bold"),bg="red",fg="white")
    search.grid(row=0, column=0, sticky=W,padx=2)
        
    self.search_var=StringVar()
    combo_search = ttk.Combobox(table_frame, width=20,textvariable=self.search_var, font=("serif", 10, "bold"), state="readonly")
    combo_search["values"] = ("Contact", "Room")
    combo_search.current(0)
    combo_search.grid(row=0, column=1)
        
    self.txt_search=StringVar()
    txt_search = ttk.Entry(table_frame, width=20,textvariable=self.txt_search, font=("serif", 10, "bold"))
    txt_search.grid(row=0, column=2,padx=2)
        
    btnsearch=Button(table_frame,text="search",command=self.search,font=("serif", 10, "bold"),bg="black",fg="gold",width=8)
    btnsearch.grid(row=0,column=3,padx=3)
        
    btnshow_all=Button(table_frame,text="Show All",command=self.fetch_data,font=("serif", 10, "bold"),bg="black",fg="gold",width=8)
    btnshow_all.grid(row=0,column=4,padx=3)
        
        # show  data table
    details_table_frame=Frame(table_frame,bd=2,relief=RIDGE)
    details_table_frame.place(x=0,y=50,width=650,height=140)

    scroll_x=ttk.Scrollbar(details_table_frame,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(details_table_frame,orient=VERTICAL)

    self.room_table=ttk.Treeview(details_table_frame,column=("contact","checkin","checkout"
            ,"roomtype","roomavailable","meal","noOfdays"),
                             xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=self.room_table.xview)
      
    self.room_table.heading("contact",text="Contact")
    self.room_table.heading("checkin",text="Check-in")
    self.room_table.heading("checkout",text="Check-out")
    self.room_table.heading("roomtype",text="Roomtype")
    self.room_table.heading("roomavailable",text="Roomavailable")
    self.room_table.heading("meal",text="Meal")
    self.room_table.heading("noOfdays",text="NoOfdays")

    self.room_table["show"]="headings"

    self.room_table.column("contact",width=100)
    self.room_table.column("checkin",width=100)
    self.room_table.column("checkout",width=100)
    self.room_table.column("roomtype",width=100)
    self.room_table.column("roomavailable",width=100)
    self.room_table.column("meal",width=100)
    self.room_table.column("noOfdays",width=100)
    self.room_table.pack(fill=BOTH,expand=1)
    
    self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

    self.fetch_data()
    
    
    # add data 
    
  def add_data(self):
    if self.var_contact.get() == "" or self.var_checkin.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
    else:
      try:
          conn = mysql.connector.connect(host="localhost", username="root", password="arjun123", database="sys")
          my_cursor = conn.cursor()
          my_cursor.execute("INSERT INTO room VALUES (%s, %s, %s, %s, %s, %s, %s)",(
                                    self.var_contact.get(),
                                    self.var_checkin.get(),
                                    self.var_checkout.get(),
                                    self.var_roomtype.get(),
                                    self.var_roomavailable.get(),
                                    self.var_meal.get(),
                                    self.var_noOfdays.get()
                                

                                   ))
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Success", "Room booked", parent=self.root)
      except Exception as es:
          messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
          
          
          # get cursor
  def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
          
        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noOfdays.set(row[6])
          
      #update function    
  def update(self):
      if self.var_contact.get() == "":
          messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
      else:
          conn = mysql.connector.connect(host="localhost", username="root", password="arjun123", database="sys")
          my_cursor = conn.cursor()
          my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s", 
                            (
                                self.var_checkin.get(),
                                self.var_checkout.get(),
                                self.var_roomtype.get(),
                                self.var_roomavailable.get(),
                                self.var_meal.get(),
                                self.var_noOfdays.get(),   
                                self.var_contact.get(),
                                       ))
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Update", "Room details have been updated successfully", parent=self.root)     
          
          # delete function
  def mDelete(self):
      mDelete=messagebox.askyesno("Hotel management Sytem","Do you want delete this customer",parent=self.root)
      if mDelete>0:
          conn = mysql.connector.connect(host="localhost", username="root", password="arjun123", database="sys")
          my_cursor = conn.cursor()
          query="delete from room where Contact=%s"
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
      else:
          if not mDelete:
                 return
      conn.commit()
      self.fetch_data()
      conn.close()     
      
      # reset function
  def reset(self):
      
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noOfdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
         
          
               # fetch data
  def fetch_data(self):
      conn = mysql.connector.connect(host="localhost", username="root", password="arjun123", database="sys")
      my_cursor = conn.cursor()
      my_cursor.execute("select * from room")
      rows=my_cursor.fetchall()
      if len(rows)!=0:
          self.room_table.delete(*self.room_table.get_children())
          for i in rows:
              self.room_table.insert("",END,values=i)
              conn.commit()
      conn.close()
          
        
        
  def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="arjun123", database="sys")
            my_cursor = conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","This number is not found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                
                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=360,y=55,width=300,height=180)
                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)
                
                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=65,y=0)
                
                
                 #====== Gender =============
                
                conn = mysql.connector.connect(host="localhost", username="root", password="arjun123", database="sys")
                my_cursor = conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)
                
                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=70,y=30)
                
                  #====== email =============
                
                conn = mysql.connector.connect(host="localhost", username="root", password="arjun123", database="sys")
                my_cursor = conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblGender=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=60)
                
                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=70,y=60)
                
                  #====== Nationality =============
                
                conn = mysql.connector.connect(host="localhost", username="root", password="arjun123", database="sys")
                my_cursor = conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblGender=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=90)
                
                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=90)
                
                  #====== Address=============
                
                conn = mysql.connector.connect(host="localhost", username="root", password="arjun123", database="sys")
                my_cursor = conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblGender=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=120)
                
                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=120)
                
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
        if search_criteria == "Contact":
            sql_query = "SELECT * FROM room WHERE Contact LIKE '%" + search_text + "%'"
        elif search_criteria == "Room":
            sql_query = "SELECT * FROM room WHERE roomavailable LIKE '%" + search_text + "%'"
        else:
            messagebox.showerror("Error", "Invalid search criteria", parent=self.root)
            return
        
        try:
            my_cursor.execute(sql_query)
            rows = my_cursor.fetchall()
            
            # Clear the table before inserting new search results
            self.room_table.delete(*self.room_table.get_children())
            
            # Insert search results into the table
            for row in rows:
                self.room_table.insert("", END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error in executing SQL query: {str(e)}", parent=self.root)
        
        conn.close()

  def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        
        try:
            inDate = datetime.strptime(inDate, "%d/%m/%Y")
            outDate = datetime.strptime(outDate, "%d/%m/%Y")
            
            # Calculate the total number of days
            total_days = abs((outDate - inDate).days)
            self.var_noOfdays.set(total_days)
            
            # Set the base room cost based on room type
            room_type = self.var_roomtype.get()
            if room_type == "Single":
                base_room_cost = 1000
            elif room_type == "Double":
                base_room_cost = 1200
            elif room_type == "Luxury":
                base_room_cost = 1500
            else:
                messagebox.showerror("Error", "Invalid room type", parent=self.root)
                return
            
            # Set the meal cost based on selected meal
            meal_type = self.var_meal.get()
            if meal_type == "Breakfast":
                meal_cost = base_room_cost
            elif meal_type == "Launch":
                meal_cost = base_room_cost
            elif meal_type == "Dinner":
                meal_cost = base_room_cost
            else:
                messagebox.showerror("Error", "Invalid meal type", parent=self.root)
                return
            
            # Calculate total cost
            total_cost = total_days * meal_cost
            
            # Calculate tax, subtotal, and total cost
            tax = total_cost * 0.09
            subtotal = total_cost
            total_cost += tax
            
            # Update the respective variables
            self.var_paidtax.set("Rs." + str("%.2f" % tax))
            self.var_actualtotal.set("Rs." + str("%.2f" % subtotal))
            self.var_total.set("Rs." + str("%.2f" % total_cost))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid check-in and check-out dates in the format DD/MM/YYYY", parent=self.root)


                
if __name__ == "__main__":
  root = Tk()
  obj = Roombooking(root)
  root.mainloop()
