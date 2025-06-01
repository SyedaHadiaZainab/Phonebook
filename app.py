import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

class PhoneBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phone Number Manager")

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.number_label = tk.Label(root, text="Number:")
        self.number_label.grid(row=1, column=0)
        self.number_entry = tk.Entry(root)
        self.number_entry.grid(row=1, column=1)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=2, column=0, columnspan=2)

        self.contacts_listbox = tk.Listbox(root)
        self.contacts_listbox.grid(row=3, column=0, columnspan=2)

        self.display_contacts()

        self.call_button = tk.Button(root, text="Call", command=self.call_contact)
        self.call_button.grid(row=4, column=0)

        self.message_button = tk.Button(root, text="Message", command=self.message_contact)
        self.message_button.grid(row=4, column=1)

        self.delete_button = tk.Button(root, text="Delete", command=self.delete_contact)
        self.delete_button.grid(row=5, column=0)

        self.block_button = tk.Button(root, text="Block", command=self.block_contact)
        self.block_button.grid(row=5, column=1)

    def add_contact(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        if name and number:
            conn = sqlite3.connect('phonebook.db')
            c = conn.cursor()
            c.execute("INSERT INTO contacts (name, number, blocked) VALUES (?, ?, ?)", (name, number, False))
            conn.commit()
            conn.close()
            self.display_contacts()
        else:
            messagebox.showwarning("Input Error", "Please enter both name and number")

    def display_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        conn = sqlite3.connect('phonebook.db')
        c = conn.cursor()
        c.execute("SELECT * FROM contacts")
        contacts = c.fetchall()
        for contact in contacts:
            self.contacts_listbox.insert(tk.END, f"{contact[1]} - {contact[2]} {'(Blocked)' if contact[3] else ''}")
        conn.close()

    def call_contact(self):
        selected_contact = self.contacts_listbox.get(tk.ACTIVE)
        if selected_contact:
            contact_name = selected_contact.split(" - ")[0]
            conn = sqlite3.connect('phonebook.db')
            c = conn.cursor()
            c.execute("SELECT * FROM contacts WHERE name=?", (contact_name,))
            contact = c.fetchone()
            conn.close()
            if contact and not contact[3]:
                messagebox.showinfo("Calling", f"Calling {contact[1]} at {contact[2]}...")
            elif contact[3]:
                messagebox.showwarning("Blocked", "Cannot call. Contact is blocked.")
            else:
                messagebox.showerror("Error", "Contact not found.")

    def message_contact(self):
        selected_contact = self.contacts_listbox.get(tk.ACTIVE)
        if selected_contact:
            contact_name = selected_contact.split(" - ")[0]
            message = simpledialog.askstring("Message", f"Enter message for {contact_name}:")
            if message:
                conn = sqlite3.connect('phonebook.db')
                c = conn.cursor()
                c.execute("SELECT * FROM contacts WHERE name=?", (contact_name,))
                contact = c.fetchone()
                conn.close()
                if contact and not contact[3]:
                    messagebox.showinfo("Sending Message", f"Sending message to {contact[1]} at {contact[2]}: {message}")
                elif contact[3]:
                    messagebox.showwarning("Blocked", "Cannot send message. Contact is blocked.")
                else:
                    messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        selected_contact = self.contacts_listbox.get(tk.ACTIVE)
        if selected_contact:
            contact_name = selected_contact.split(" - ")[0]
            conn = sqlite3.connect('phonebook.db')
            c = conn.cursor()
            c.execute("DELETE FROM contacts WHERE name=?", (contact_name,))
            conn.commit()
            conn.close()
            self.display_contacts()
            messagebox.showinfo("Deleted", f"Contact {contact_name} deleted successfully.")

    def block_contact(self):
        selected_contact = self.contacts_listbox.get(tk.ACTIVE)
        if selected_contact:
            contact_name = selected_contact.split(" - ")[0]
            conn = sqlite3.connect('phonebook.db')
            c = conn.cursor()
            c.execute("UPDATE contacts SET blocked=? WHERE name=?", (True, contact_name))
            conn.commit()
            conn.close()
            self.display_contacts()
            messagebox.showinfo("Blocked", f"Contact {contact_name} blocked successfully.")

if __name__ == '__main__':
    root = tk.Tk()
    app = PhoneBookApp(root)
    root.mainloop()
