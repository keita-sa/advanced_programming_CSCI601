import sqlite3

# Connect to the SQLite database
def connect_db():
    conn = sqlite3.connect('address_book.db')
    return conn

# Create the contacts table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            address TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Add a new contact
def add_contact(name, phone, email, address):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO contacts (name, phone, email, address)
        VALUES (?, ?, ?, ?)
    ''', (name, phone, email, address))
    conn.commit()
    conn.close()

# View all contacts
def view_contacts():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    conn.close()
    return contacts

# Update an existing contact
def update_contact(contact_id, name, phone, email, address):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE contacts
        SET name = ?, phone = ?, email = ?, address = ?
        WHERE id = ?
    ''', (name, phone, email, address, contact_id))
    conn.commit()
    conn.close()

# Delete a contact
def delete_contact(contact_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
    conn.commit()
    conn.close()

# Display menu and handle user input
def menu():
    create_table()
    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)
            print("Contact added.")

        elif choice == '2':
            contacts = view_contacts()
            print("\nContacts:")
            for contact in contacts:
                print(
                    f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}, Address: {contact[4]}")

        elif choice == '3':
            contact_id = input("Enter contact ID to update: ")
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            update_contact(contact_id, name, phone, email, address)
            print("Contact updated.")

        elif choice == '4':
            contact_id = input("Enter contact ID to delete: ")
            delete_contact(contact_id)
            print("Contact deleted.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

# Main function
if __name__ == '__main__':
    menu()
