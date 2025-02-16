
import tkinter as tk 
from tkinter import messagebox, simpledialog
import os 
import json 


class contactBook:
    def __init__(self,root ):
        self.root = root 
        self.root.title("contact Book")
        self.root.geometry("500x500")

        self.contacts = {}
        self.file_path = "contacts.json"
        self.load_contacts()

        #setting ui

        self.listbox = tk.Listbox(self.root, font=('Airal',12))
        self.listbox.pack(expand = True, fill = 'both', padx=10,pady=10)
        self.listbox.bind("<<ListboxSelect>>",self.show_contact_details)

        self.detail_label = tk.Label(self.root, text="Select a contact to view details", font = ('Arial', 12),anchor='w')
        self.detail_label.pack(fill='x',padx=10,pady=5)

        self.add_button = tk.Button(self.root, text='Add Contact', command=self.add_contact)
        self.add_button.pack(side='left',padx=10, pady=10)
        
        self.edit_button = tk.Button(self.root, text='Edit Contact', command=self.edit_contact)
        self.edit_button.pack(side='left',padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text='Delete Contact', command=self.delete_contact)
        self.delete_button.pack(side='right',padx=10, pady=10)

        self.refresh_list()
        
    
    def load_contacts(self):
        if os.path.exists(self.file_path):
            with open(self.file_path,"r")as file:
                self.contacts = json.load(file)
        else:
            self.contacts = {}

    def save_contacts(self):
        with open(self.file_path,'w') as file:
            json.dump(self.contacts, file)

    def refresh_list(self):
        self.listbox.delete(0,tk.END)
        for name in sorted(self.contacts.keys()):
            self.listbox.insert(tk.END, name)


    def show_contact_details(self, event):
        selected = self.listbox.curselection()
        if selected:
            name = self.listbox.get(selected)
            details = self.contacts[name]
            self.detail_label.config(text=f'Name: {name}\nPhone:{details['phone']}\n Email:{details['email']}')
            self.edit_button.config(state='normal')
            self.delete_button.config(state='normal')
        else:
            self.detail_label.config(text='Select a contact to view details.')
            self.edit_button.config(state='disabled')
            self.delete_button.config(state='disabled')


    def add_contact(self):
        name = simpledialog.askstring(title='Add Contact',prompt='Enter contact name:')
        if not name:
            return
        if name in self.contacts:
            messagebox.showerror(title='Error',message='Contact already exists.')
        phone = simpledialog.askstring(title='Add Contact', prompt='Enter phone number:')
        email = simpledialog.askstring(title='Add Contact', prompt='Enter email address:')
        self.contacts[name] = {"phone":phone,'email':email}
        self.save_contacts()
        self.refresh_list()

    def edit_contact(self):
        selected = self.listbox.curselection()
        if selected:
            name = self.listbox.get(selected)
            new_phone = simpledialog.askstring(title='Edit Contact', prompt='Enter new phone number:', initialvalue=self.contacts[name]['phone'] )
            new_email = simpledialog.askstring(title='Edit Contact', prompt='Enter new email address:', initialvalue=self.contacts[name]['emal'])
            self.contacts[name] = {"phone":new_phone,'email':new_email}
            self.save_contacts()
            self.refresh_list()

    def delete_contact(self):
        selected = self.listbox.curselection()
        if selected:
            name = self.listbox.get(selected)
            if messagebox.askyesno("Delete Contact",message= f"Are you sure you want to delete '{name}'?"):
                del self.contacts[name]
                self.save_contacts()
                self.refresh_list()
                self.detail_label.config(text="Select a contact to view details.")
                self.edit_button.config(state='disabled')
                self.delete_button.config(state='disabled')

if __name__=='__main__':
    root = tk.Tk()
    app = contactBook(root)
    root.mainloop()