# Flask Book App

This is a simple web application built using Flask that allows users to manage a list of books. Users can view all books, add new books, edit existing ones, and delete books using RESTful API endpoints.

## Features

- View a list of books.
- Add new books using a POST request.
- Edit existing books using a PUT request.
- Delete books using a DELETE request.
- Basic error handling for invalid requests.

## Technologies Used

- **Flask** – Micro web framework for Python.
- **JSON** – Data format for API communication.
- **Git & GitHub** – Version control and repository hosting.

## How to Run the Project

1. **Clone the repository**:
   git clone https://github.com/snejmail/First-Flask-Book-App.git

2. **Navigate to the project directory**:
   cd First-Flask-Book-App

3. **Create a virtual environment (optional but recommended)**:
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate     # On Windows

4. **Install the required dependencies**:
   pip install flask

5. **Run the application**:
   python app.py

6. **Access the application: Open your browser and go to http://127.0.0.1:5000/**

## Available Endpoints

| Method | Endpoint        | Description                |
|--------|-----------------|----------------------------|
| **GET**    | `/`             | Welcome message            |
| **GET**    | `/books`        | List all books             |
| **POST**   | `/books`        | Add a new book             |
| **PUT**    | `/books/<id>`   | Edit a book by ID          |
| **DELETE** | `/books/<id>`   | Delete a book by ID        |

## License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute it under the terms of this license.


