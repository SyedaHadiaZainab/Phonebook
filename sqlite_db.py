import sqlite3

def initialize_database():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    
    # Create contacts table
    c.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        blocked INTEGER DEFAULT 0
    )
    ''')

    # Create messages table
    c.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        contact_id INTEGER,
        message TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (contact_id) REFERENCES contacts(id)
    )
    ''')

    # Create calls table
    c.execute('''
    CREATE TABLE IF NOT EXISTS calls (
        id INTEGER PRIMARY KEY,
        contact_id INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (contact_id) REFERENCES contacts(id)
    )
    ''')
    
    conn.commit()
    conn.close()

initialize_database()
