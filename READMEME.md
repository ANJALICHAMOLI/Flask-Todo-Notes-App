📌 Flask Todo & Notes App

A simple Flask web application to manage your daily tasks, subtasks, reminders, and personal notes. Organize your to-dos, set reminders, and keep all your notes in one place — from a single intuitive dashboard.

👉 Live demo / screenshots (if available) can be added here!

🛠 Features

✅ Daily Task Management
• Add, edit, and delete tasks
• Mark tasks as completed or pending

✅ Subtasks Support
• Break down tasks into smaller steps
• Track progress more granularly

✅ Reminders
• Set reminders for important tasks
• Never miss deadlines

✅ Personal Notes
• Create, view, edit, and delete notes
• Organized section for all your thoughts & ideas

✔ Built with Python, Flask & Jinja templates
✔ Uses a simple storage and upload system for reminders & notes
✔ Easy to extend or customize

🚀 Quick Start

These steps get your dev environment set up and running locally.

1. Clone the repository
git clone https://github.com/ANJALICHAMOLI/Flask-Todo-Notes-App.git
cd Flask-Todo-Notes-App

2. (Recommended) Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # macOS & Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the app
python todo.py

5. Open in browser

Visit:

http://localhost:5000

📁 Project Structure
Flask-Todo-Notes-App/
├── templates/              # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── notes.html
│   └── (etc…)
├── uploads/                # Uploaded files (if used)
├── todo.py                 # Main Flask application
├── requirements.txt        # Python dependencies
├── .gitignore
└── ...

🧩 Tech Stack
Component	Technology
Backend	Python, Flask
Frontend	HTML, CSS, JavaScript
Templating	Jinja2
Storage (notes/ uploads)	Local storage / filesystem
Dependencies	Listed in requirements.txt
📌 Recommended Enhancements (optional)

Here are a few ideas you could consider adding next:

✨ User authentication (login/signup)
✨ Database support (SQLite / SQLAlchemy)
✨ Email reminders & push notifications
✨ Tags & categories for tasks/notes
✨ Search & filters for notes/tasks

💬 Contributions

Contributions are welcome!
Feel free to raise issues, suggest features, or submit pull requests.

If you find this useful, don’t forget to ⭐ Star this repo!