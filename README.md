# Noted — Real-Time Collaborative Notes App

A lightweight web application where multiple users can create, edit, and organize notes that sync live across sessions. Built as part of the GDG Sprint Build Phase 2 challenge.

---

## Features

- User authentication — register, log in, log out securely
- Create, edit, and delete personal notes
- Organize notes with tags
- Real-time sync — changes appear instantly across connected users
- Clean, responsive UI built with Tailwind CSS

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Real-Time | Flask-SocketIO |
| Database | SQLite (development) |
| Auth | Flask-Login, bcrypt |
| Frontend | Jinja2, Tailwind CSS |
| Deployment | Render |

---

## Project Structure

```
collab-notes/
├── app/
│   ├── __init__.py          # App factory
│   ├── models.py            # Database models
│   ├── auth/
│   │   ├── __init__.py
│   │   └── routes.py        # Register, login, logout
│   ├── notes/
│   │   ├── __init__.py
│   │   └── routes.py        # CRUD for notes
│   └── templates/
│       ├── base.html
│       ├── auth/
│       └── notes/
├── config.py                # App configuration
├── run.py                   # Entry point
├── requirements.txt
└── README.md
```

---

## Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/auwalcodes2007/collaborative-notes-app.git
cd collaborative-notes-app

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python run.py
```

Visit `http://localhost:5000` in your browser.

---

## Roadmap

- [x] Project setup and structure
- [ ] User authentication
- [ ] Notes CRUD
- [ ] Real-time sync with Flask-SocketIO
- [ ] Tags and organization
- [ ] Responsive UI with Tailwind CSS
- [ ] Deployment on Render

---

## Author

**Auwal** — 200 Level Software Engineering Student, building in public.

GitHub: [@auwalcodes2007](https://github.com/auwalcodes2007)

---

## License

MIT