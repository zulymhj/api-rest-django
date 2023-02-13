# Api Rest Django
Development of a Rest API in Python with the Django framework using the Rest-Framework library.  Deploy with Docker, create file docker-compose.yml with image Python, PostgreSQL and PgAdmin.

### A Simple App
This APP has:
* CRUD of product with logical deletion
* API's cart and order
* Customize admin django
* Insert data in the database with migrations
* Create command for add superuser
* Synchronization of stock of products with signal

### Django REST framework
Web framework for building APIs with Python

### Docker Compose
Remember that for create the file **docker-compose.yml** is necessary has install **version 1.29** or high
* **Python**:
* **PostgreSQL**:
* **PgAdmin**:

### Deploy with docker
1. Check if the **.env** file exists in the root directory.
2. Execute command **docker-compose up --build -d** for create the images of docker.
3. Verify that the images were created correctly, execute command **docker ps -a** 

### URL
* **Swagger**:
 http://127.0.0.1:8001/api/v1/swagger/
* **Admin**:
 http://127.0.0.1:8001/admin/
* **PgAdmin**:
 http://127.0.0.1:8081/
