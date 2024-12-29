# Django REST Framework: CRUD API

This repository contains a Django-based REST API project for managing data with full CRUD (Create, Read, Update, Delete) functionality. The project demonstrates building a scalable and maintainable REST API using Django and Django REST Framework (DRF).

## Image Representation
Here is a image showing the application in action:
<p align="center">
<img width="800" alt="image" src=https://github.com/its-imthiyas/Django-REST-API-Beverages-Management/blob/main/Django%20API%20Screenshot.png>

## Features

- **REST API**: Built with Django REST Framework for efficient and standardized API development.
- **CRUD Operations**:
  - **Create**: Add new records to the database.
  - **Read**: Retrieve details of records, either individually or in bulk.
  - **Update**: Modify existing records.
  - **Delete**: Remove records from the database.
- **Model Integration**: Django ORM is used for seamless interaction with the database.
- **Browsable API**: Leverages Django REST Framework's built-in browsable API for testing and exploration.
- **JSON Responses**: API endpoints return structured JSON data.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: SQLite (default, customizable to other databases like PostgreSQL or MySQL)
- **Frontend**: JSON responses consumable via API clients (Postman, curl, or frontend applications)

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/django-crud-api.git
   cd django-crud-api
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   - Create initial migrations:
     ```bash
     python manage.py makemigrations
     ```
   - Apply migrations:
     ```bash
     python manage.py migrate
     ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
   The application will be accessible at `http://127.0.0.1:8000/`.

## Usage

1. **Admin Interface**:
   - Navigate to `http://127.0.0.1:8000/admin/` to manage database entries via Django's built-in admin panel.

2. **API Endpoints**:
   - `GET /api/`: List all records.
   - `POST /api/`: Create a new record.
   - `GET /api/<id>/`: Retrieve details of a specific record.
   - `PUT /api/<id>/`: Update a specific record.
   - `DELETE /api/<id>/`: Delete a specific record.

3. **Testing the API**:
   - Use tools like Postman, curl, or a custom frontend to interact with the API endpoints.

## Future Enhancements
- Add authentication and permissions to secure the API.
- Implement filtering, searching, and pagination for improved data handling.
- Expand the API to support more complex relationships and operations.

## Contributing

Contributions are welcome! Feel free to fork the repository, create a new branch, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.
