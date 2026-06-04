# Python API

## REST (Representational State Transfer): An architectural style for designing networked applications. It relies on a stateless, client-server communication protocol, typically HTTP. RESTful APIs use standard HTTP methods and status codes to perform operations on resources, which are identified by URLs

## HTTP Methods

1. GET → Retrieve Data
2. POST → Create Data
3. PUT → Update Data
4. DELETE → Remove Data

Example:

1. Get list of Users -> GET
2. Create a new User -> POST
3. Update User info -> PUT
4. Delete User -> DELETE

## REST defined conventions

1. Use nouns to represent resources (e.g., /users, /products).
2. Use HTTP methods to perform actions on resources (e.g., GET, POST, PUT, DELETE).
3. Use plural nouns for resource names (e.g., /users instead of /user).
4. Use query parameters for filtering and sorting (e.g., /users?age=30&sort=name).
5. Use status codes to indicate the outcome of a request (e.g., 200 OK, 201 Created, 400 Bad Request, 404 Not Found).
6. Use consistent and meaningful URLs to represent resources and actions (e.g., /users/{id} for specific user operations).
7. Use JSON as the standard format for request and response bodies.
8. Use versioning in the API URL to manage changes and updates (e.g., /v1/users).

## FastAPI: A modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints. It is designed to be easy to use and to provide high performance, making it a popular choice for building RESTful APIs in Python
