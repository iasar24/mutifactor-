# Login App

This project is a simple login application built using FastAPI for the backend and React for the frontend. It provides a login feature with JWT-based authentication, allowing users to log in and access a welcome page.

## Project Structure

```
login-app
├── backend
│   ├── app.py              # Main entry point for the FastAPI application
│   ├── auth.py             # Functions for creating and verifying JWT tokens
│   ├── models.py           # Pydantic models for request and response validation
│   ├── storage.py          # User data storage and retrieval management
│   ├── requirements.txt     # Backend dependencies
│   └── .env                # Environment variables for the backend
├── frontend
│   ├── package.json        # Configuration file for the React frontend
│   ├── vite.config.js      # Vite configuration for the React application
│   ├── index.html          # Main HTML file for the frontend application
│   └── src
│       ├── main.jsx        # Entry point for the React application
│       ├── App.jsx         # Main application component with routing
│       ├── Login.jsx       # Login component for user authentication
│       └── Welcome.jsx     # Welcome component displaying a welcome message
```

## Setup Instructions

### Backend

1. Navigate to the `backend` directory:
   ```
   cd backend
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the `backend` directory and set the following environment variables:
   ```
   JWT_SECRET=change_this_to_a_long_random_value
   ENV=dev
   ```

5. Run the FastAPI application:
   ```
   uvicorn app:app --reload --port 8000
   ```

### Frontend

1. Navigate to the `frontend` directory:
   ```
   cd frontend
   ```

2. Install the frontend dependencies:
   ```
   npm install
   ```

3. Run the React application:
   ```
   npm run dev
   ```

4. Open your browser and go to `http://localhost:5173`.

## Test Credentials

- **Username:** demo
- **Password:** P@ssw0rd!

## Features

- User authentication with JWT tokens.
- Login form with validation and error handling.
- Welcome page that greets the user upon successful login.
- Logout functionality to clear the session.

## Notes

This project is intended for educational purposes and demonstrates the integration of FastAPI and React for building a simple web application with authentication.