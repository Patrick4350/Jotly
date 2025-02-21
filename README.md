# Jotly 📝  
Jotly is a simple and efficient note-taking application that allows users to create, manage, and organize their notes effortlessly. Built with **Django (backend) and React (frontend)**, Jotly provides a seamless and responsive user experience.  

## 🚀 Features  
- 🔒 **User Authentication** (JWT-based login & signup)  
- 📝 **Create, Edit, and Delete Notes**  
- 📂 **Organize Notes with Categories or Tags**  
- 🔍 **Search and Filter Notes**  
- ☁️ **Persistent Storage** with a database-backed backend  

## 🏗 Tech Stack  
### Backend:  
- **Django & Django REST Framework (DRF)**  
- **PostgreSQL** (Database)  
- **SimpleJWT** (Authentication)  

### Frontend:  
- **React.js (Vite-powered)**  
- **Axios** (for API requests)  
- **React Router** (for navigation)  
- **Tailwind CSS** (for styling)  

## 📂 Project Structure  
```
Jotly/
│── backend/        # Django backend (API)
│   ├── jotly/      # Django project folder
│   ├── api/        # Django app (handles notes & users)
│   ├── settings.py # Django settings
│── frontend/       # React frontend
│   ├── src/        # React components & pages
│   ├── main.jsx    # React entry point
│── .env            # Environment variables
│── requirements.txt # Python dependencies
│── package.json    # Frontend dependencies
│── endpoints.yaml  # API Deployment Configuration
│── README.md       # Project documentation
```

## 🔧 Setup Instructions  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Patrick4350/jotly.git
cd jotly
```

### 2️⃣ Backend Setup (Django)  
```bash
cd backend
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate (Linux/macOS)
venv\Scripts\activate  # Activate (Windows)
pip install -r requirements.txt  # Install dependencies
python manage.py migrate  # Run migrations
python manage.py runserver  # Start the backend
```

### 3️⃣ Frontend Setup (React)  
```bash
cd frontend
npm install  # Install dependencies
npm run dev  # Start the frontend (Vite)
```

## 🔑 Environment Variables (`.env`)  
Create a `.env` file in both **backend** and **frontend** folders with the required variables:  

### Backend `.env`  
```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3  # Change for PostgreSQL
ALLOWED_HOSTS=*
```

### Frontend `.env`  
```env
VITE_API_URL=http://127.0.0.1:8000
```

## 📌 API Endpoints (Sample)  
- **`POST /api/user/register/`** – User Registration  
- **`POST /api/token/`** – Get JWT Token  
- **`GET /api/notes/`** – Retrieve all notes  
- **`POST /api/notes/`** – Create a new note  
- **`PUT /api/notes/{id}/`** – Update a note  
- **`DELETE /api/notes/{id}/`** – Delete a note  

## 🛠️ Deployment  
For production deployment:  
- Use **Gunicorn & Nginx** for Django  
- Use **PM2** to manage the React app  
- Set up **Docker Compose** for containerization (optional)  

## 📌 Contributors  
- **Patrick Owusu Bofah**  

## 📜 License  
This project is licensed under the **MIT License**.  
