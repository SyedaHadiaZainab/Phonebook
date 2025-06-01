# 📞 Phonebook Web App (Python + Flask + SQLite)

A simple yet functional **Phonebook web application** built using **Flask** and **SQLite**. This app allows users to manage contacts, view or store phone numbers, and interact through a responsive web interface.

---

## 📌 Features

- Add, view, update, and delete contacts
- Built with Flask and Python
- Persistent storage using SQLite
- Organized using Flask's standard structure (`static`, `templates`)
- Precompiled with PyInstaller for packaging (`app.spec`, `dist/`)

---

## 🛠️ Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML/CSS (Jinja templates)
- **Database:** SQLite
- **UI Assets:** Stored in `/static`
- **Templates:** Stored in `/templates`

---

## 📁 Project Structure

phonebook-app/
├── build/ # PyInstaller build output
├── dist/ # PyInstaller distribution folder (compiled executable)
├── static/ # CSS, JS, and image assets
├── templates/ # HTML templates (Jinja2)
├── app.py # Main Flask application
├── app.spec # PyInstaller config file
├── contacts.db # SQLite database file for contacts
├── phonebook.db # Backup or alternate database
├── sqlite.py # Additional DB-related logic (if separate)
├── sqlite_db.py # DB schema or access functions
├── test.db # Test database (optional or test cases)
├── icon.ico # App icon
├── README.md # Project readme (you're here)

---

## 🚀 How to Run

### 🔧 Prerequisites
- Python 3.x
- Flask
- SQLite (built-in)

### 💻 Local Setup

```bash
# Clone the repository
git clone https://github.com/SyedaHadiaZainab/phonebook-app.git
cd phonebook-app

# Install dependencies
pip install flask

# Run the app
python app.py
Then open your browser at: http://localhost:5000

👩‍💻 Developer
Syeda Hadia Zainab
BS Software Engineering – Fatima Jinnah Women University
📧 Email: taqviggg@gmail.com
🔗 LinkedIn: www.linkedin.com/in/syeda-hadia-zainab-a3331126b

📜 License
This project is licensed under the MIT License.
---
