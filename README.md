# HealthConnect

HealthConnect is a telemedicine platform designed to provide seamless virtual healthcare services. The system connects patients with healthcare providers for consultations, scheduling, and medical records management. The platform features user-friendly interfaces for patients and healthcare providers, offering a streamlined solution to access medical services remotely.

## Project Overview
HealthConnect is developed as part of the final assignment for introduction to software engineering course. The system aims to enhance healthcare accessibility by allowing remote consultations, improving patient outcomes, and reducing the need for in-person visits. The system supports three primary user roles: **Patients**, **Healthcare Providers**, and **Administrators**.

## Technologies Used
- **Frontend**: React, Vite, HTML, CSS, JavaScript, Tailwind CSS, Material UI
- **Backend**: Django
- **Database**: SQLite
- **Deployment**: Vercel (Frontend), PythonAnywhere (Backend)
- **CI/CD**: GitHub Actions
- **Authentication**: Django-Auth, JWT

## Features and Functionalities
1. **User Registration and Login**  
   Users can register and log in to the system.  
   Authentication is managed with Django-Auth and JWT.

2. **Appointment Scheduling**  
   Patients can schedule consultations with healthcare providers and receive reminders.

3. **Video Consultations**  
   Patients and healthcare providers can conduct live video consultations using integrated WebRTC technology.

4. **Medical Records Management**  
   Patients can manage their health records and share them with healthcare providers during consultations.

5. **Healthcare Provider Dashboard**  
   Healthcare providers can manage their consultations, patient records, and availability.

6. **Admin Dashboard**  
   Administrators can monitor system performance, manage users, and track consultations.

## Project Setup

### Prerequisites
- Python 3.x
- React Vite
- SQLite
- Git
- PythonAnywhere
- vercel

### Installation

#### Clone the Repository:
```bash
### Backend Setup
1.⁠ ⁠Clone the repository:
   ```bash
   git clone https://github.com/Deolinda/health.git
   cd health
Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
Install required packages:
pip install -r requirements.txt
Configure the SQLite database in settings.py.
Apply database migrations:
python manage.py migrate
Start the backend server:
python manage.py runserver
Frontend Setup
Navigate to the frontend directory:
cd frontend
Install the required packages:
pnpm install
Start the frontend development server:
pnpm run dev
Deployment

Frontend: Deployed on Vercel for scalability and reliability.
Backend: Deployed on PythonAnywhere with automated deployment scripts to handle migrations and restart the server.
License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements

Instructor: Tunde Isiaq Gbadamosi
Course: Introduction to Software Engineering
University: African Leadership University
