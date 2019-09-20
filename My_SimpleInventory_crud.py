
try:
    import Tkinter
    import ttk
except ImportError: 
    import tkinter as Tkinter
    import tkinter.ttk as ttk
    from tkinter import messagebox
    
class Items(Tkinter.Frame):
    def __init__(self,parent):
      
        Tkinter.Frame.__init__(self, parent)
        self.parent=parent
       
        self.interface()
   
    def interface(self):

        
        self.parent.title("Main Form")
        self.parent.geometry("1020x490")
        self.parent.resizable(0, 0) 
        self.headercolor=Tkinter.Label(text="My Inventory System",bg="#020202",fg="#ffbf00",font=("Tahoma", 16,'bold'))
        self.headercolor.place(x=0,y=0,width="1020",height="70")
        
        self.linebg=Tkinter.Label(text="",bg="#ffbf00")
        self.linebg.place(x=0,y=70,width="1020",height="2")
        """
        malupet na background
        """
        self.bggcolor=Tkinter.Label(bg="#161616")
        self.bggcolor.place(x=15,y=115,width="328",height="340")
        
        self.rightbgcolor=Tkinter.Label(bg="#161616")
        self.rightbgcolor.place(x=370,y=115,width="634",height="340")




        self.addlbl=Tkinter.Label(text="ITEMS",fg="#ffbf00",bg="#161616",font=("Arial Black", 10,'bold'))
        self.addlbl.place(x=30,y=150)


        self. prdct_Name=Tkinter.Label(text="ProductName ",fg="#ffbf00",bg="#161616",font=("Arial Black", 10,'bold'))
        self. prdct_Name.place(x=30,y=200)
        self.e1 =Tkinter.Entry (self.parent, width=20,font=("Arial Black", 10,'bold'),fg="#020202",bg="#ffbf00")
        self.e1.place(x=140,y=200,height="32")
        self.prdct_Categ=Tkinter.Label(text="Category ",fg="#ffbf00",bg="#161616",font=("Arial Black", 10,'bold'))
        self.prdct_Categ.place(x=30,y=240)
        self.e2 = Tkinter.Entry(self.parent, width=20,font=("Arial Black", 10,'bold'),fg="#020202",bg="#ffbf00")
        self.e2.place(x=140,y=240,height="32")
        self.prdct_Price=Tkinter.Label(text="Price ",fg="#ffbf00",bg="#161616",font=("Arial Black", 10,'bold'))
        self.prdct_Price.place(x=30,y=280)
        self.e3 = Tkinter.Entry(self.parent, width=20,font=("Arial Black", 10,'bold'),fg="#020202",bg="#ffbf00")
        self.e3.place(x=140,y=280,height="32")
        self. prdct_Stock=Tkinter.Label(text="Stock ",fg="#ffbf00",bg="#161616",font=("Arial Black", 10,'bold'))
        self.prdct_Stock.place(x=30,y=320)
        self.e4 = Tkinter.Entry(self.parent, width=20,font=("Arial Black", 10,'bold'),fg="#020202",bg="#ffbf00")
        self.e4.place(x=140,y=320,height="32")
        
        self.btn1 = Tkinter.Button(self.parent, text="ADD ITEM",command=self.additem, width=10,font=("Arial Black", 10))
        self.btn1.place(x=30,y=400,height="32")


        self.button_del = Tkinter.Button(self.parent, text="Delete Item", command=self.deleteitem,width=10,font=("Arial Black", 10))
        self.button_del.place(x=135,y=400,height="32")

        self.button_up = Tkinter.Button(self.parent, text="Update Item",command=self.updateitem,width=10,font=("Arial Black", 10))
        self.button_up.place(x=240,y=400,height="32")
        
        
        self.parent.config(background="#202020")
        self.tree = ttk.Treeview(self.parent, height=14,
                                 columns=('#0', '#1','#2','#3'))
        self.tree.heading('#0', text='Id')
        self.tree.heading('#1', text='Name')
        self.tree.heading('#2', text='Category')
        self.tree.heading('#3', text='Price')
        self.tree.heading('#4', text='Stock')
        self.tree.column('#1', stretch=Tkinter.YES,width=120)
        self.tree.column('#2', stretch=Tkinter.YES,width=120)
        self.tree.column('#3', stretch=Tkinter.YES,width=120)
        self.tree.column('#4', stretch=Tkinter.YES,width=120)
        self.tree.column('#0', stretch=Tkinter.YES,width=120)
        self.tree.grid(columnspan=1, sticky='nsew',padx=387,pady=130)
        self.treeview = self.tree
        self.i = 0
    def additem(self):

        if len(self.e1.get())==0:
            
           messagebox.showerror("ErrorMessage", "please fill in all the field/s")
        elif len(self.e2.get())==0:
           messagebox.showerror("ErrorMessage", "please fill in all the field/s")
        elif len(self.e3.get())==0:
           messagebox.showerror("ErrorMessage", "please fill in all the field/s")
        elif len(self.e4.get())==0:
           messagebox.showerror("ErrorMessage", "please fill in all the field/s")  
        else:
       
           messagebox.showinfo("Message", "Item Added Successfully")
           self.treeview.insert('','end',text=""+str(self.i),values=(self.e1.get(),self.e2.get(),self.e3.get(),self.e4.get()))
           self.i = self.i + 1
           self.e1.delete(0,'end')
           self.e2.delete(0,'end')
           self.e3.delete(0,'end')
           self.e4.delete(0,'end')
       
    def deleteitem(self):
        selecteditem = self.tree.selection()[0]
        self.tree.delete(selecteditem)
        messagebox.showinfo("Message", "Item Deleted Successfully")
       
    def updateitem(self):
        """
        select the item in treeview tapos mag entry sa fields to update the item sa treeview.
        """
        
        selectedi = self.tree.selection()[0]
        self.eMessage = Tkinter.messagebox.askquestion ('Update Message','Are you sure you want to Update Item?',icon = 'warning')
        if self.eMessage == 'yes':
            messagebox.showinfo("Message", "Item Updated Successfully")
            self.tree.item(selectedi, values=(self.e1.get(),self.e2.get(),self.e3.get(),self.e4.get()))
            self.e1.delete(0,'end')
            self.e2.delete(0,'end')
            self.e3.delete(0,'end')
            self.e4.delete(0,'end')
        
    
       
def main():
    root=Tkinter.Tk()
    d=Items(root)
    root.mainloop()
    
if __name__=="__main__":
    main()
