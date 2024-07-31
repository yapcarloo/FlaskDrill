# Checklist System

This is a Flask application for managing a checklist system. It allows users to perform CRUD operations on customer data stored in a MySQL database.

## Setup

1. Install Python (if not already installed).
2. Install Flask and other dependencies:
   ```bash
   pip install Flask Flask-MySQLdb dicttoxml
3. Make sure you have MySQL installed and running on your local machine.
4. Set up the MySQL database and tables by executing the SQL script provided in database.sql.


## Usage

1. Run the Flask application

python app.py


2. Access the endpoints using a tool like Postman or through a web browser:

Endpoints
-GET /protected: Retrieves a protected resource. Requires authentication.
-GET /customer: Retrieves all customers from the database.
-GET /customer/<id>: Retrieves a customer by ID.
-GET /customer/<id>/orders: Retrieves orders associated with a customer.
-POST /customer: Adds a new customer to the database.
-PUT /customer/<id>: Updates an existing customer.
-DELETE /customer/<id>: Deletes a customer from the database.

## Authentication

The application uses HTTP Basic Authentication. By default, the username is "yappy" and the password is "7891". You can change these credentials in the verify_password function.

## Response Format
The API supports both JSON and XML response formats. You can specify the desired format using the format query parameter.

