Flask Book App
This is a simple web application built using Flask that allows users to manage a list of books. Users can view all books, add new books, edit existing ones, and delete books using RESTful API endpoints.

Features
View a list of books.
Add new books using a POST request.
Edit existing books using a PUT request.
Delete books using a DELETE request.
Basic error handling for invalid requests.
Technologies Used
Flask – Micro web framework for Python.
JSON – Data format for API communication.
Git & GitHub – Version control and repository hosting.
How to Run the Project
Clone the repository:

bash
Copy code
git clone https://github.com/snejmail/First-Flask-Book-App.git
Navigate to the project directory:

bash
Copy code
cd First-Flask-Book-App
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
Install the required dependencies:

bash
Copy code
pip install flask
Run the application:

bash
Copy code
python app.py
Access the application: Open your browser and go to http://127.0.0.1:5000/.

Available Endpoints
Method	Endpoint	Description
GET	/	Welcome message
GET	/books	List all books
POST	/books	Add a new book
PUT	/books/<id>	Edit a book by ID
DELETE	/books/<id>	Delete a book by ID
