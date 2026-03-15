
# Internship Assesment



# Django REST Framework Assignment

This project implements a REST API using **Django** and **Django REST Framework** to manage relationships between:

- Vendors
- Products
- Courses
- Certifications

The system also manages mapping relationships between these entities.

Swagger documentation is included for easy API testing.

---

# Tech Stack

- Python
- Django
- Django REST Framework
- drf-yasg (Swagger documentation)
- SQLite

---

# Project Structure

```
project/
│
├── vendor/
├── product/
├── course/
├── certification/
│
├── vendor_product_mapping/
├── product_course_mapping/
├── course_certification_mapping/
│
├── config/
│
├── manage.py
├── requirements.txt
└── README.md
```
# Installed Apps

The following apps are included in the project:

- vendor
- product
- course
- certification
- vendor_product_mapping
- product_course_mapping
- course_certification_mapping
- rest_framework
- drf_yasg

---

# Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
```
### 2. Create Virtual 
```
python -m venv venv
```
#### Activate it:

Windows
```
venv\Scripts\activate
```
Linux / Mac
```
source venv/bin/activate
```
### 3. Install Dependencies
```
pip install -r requirements.
```
### 4. Migration Steps

Run database migrations:
```
python manage.py makemigrations
python manage.py migrate
```

This will create the database schema.

----
### 5. Run the Development Server

Start the server using:
```
python manage.py runserver
```

The server will run at:
```
http://127.0.0.1:8000/
```
### 6. Swagger API Documentation

Swagger UI is available for testing APIs.

Open:
```
http://127.0.0.1:8000/swagger/
```
You can use Swagger to execute API requests directly.

 ### 7. API Endpoints


All APIs are available under the base path:

```
/api/
```
Interactive testing is available via Swagger:
```
http://127.0.0.1:8000/swagger/
```
#### Vendor APIs

Create Vendor
```
Endpoint

POST /api/vendors/
```

Request Body
```
{
  "name": "Vendor A",
  "code": 101,
  "description": "Example vendor",
  "is_active": true
}
```
Response
```
{
  "id": 1,
  "name": "Vendor A",
  "code": 101,
  "description": "Example vendor",
  "is_active": true,
  "created_at": "2026-03-15T10:00:00Z",
  "updated_at": "2026-03-15T10:00:00Z"
}
```
Get All Vendors
```
GET /api/vendors/
```
Returns a list of all vendors.

Get Vendor by ID
```
GET /api/vendors/{id}/
```
Example:
```
GET /api/vendors/1/
```
Update Vendor
```
PUT /api/vendors/{id}/
```
Delete Vendor
```
DELETE /api/vendors/{id}/
```
#### Product APIs
Create Product
```
POST /api/products/
```
Example request:
```
{
  "name": "Product A",
  "code": 201,
  "description": "Example product",
  "is_active": true
}
```
Product Endpoints
```
GET    /api/products/
GET    /api/products/{id}/
PUT    /api/products/{id}/
DELETE /api/products/{id}/
```
#### Course APIs
Create Course
```
POST /api/courses/
```
Example request:
```
{
  "name": "Course A",
  "code": 301,
  "description": "Example course",
  "is_active": true
}
```
Course Endpoints
```
GET    /api/courses/
GET    /api/courses/{id}/
PUT    /api/courses/{id}/
DELETE /api/courses/{id}/
```
#### Certification APIs

Create Certification
```
POST /api/certifications/
```
Example request:
```
{
  "name": "Certification A",
  "code": 401,
  "description": "Example certification",
  "is_active": true
}
```
Certification Endpoints
```
GET    /api/certifications/
GET    /api/certifications/{id}/
PUT    /api/certifications/{id}/
DELETE /api/certifications/{id}/
```
----
#### Mapping APIs



These APIs manage relationships between master entities.

#### Vendor → Product Mapping

Create mapping:
```
POST /api/vendor-product-mappings/
```
Example request:
```
{
  "vendor": 1,
  "product": 1,
  "primary_mapping": true,
  "is_active": true
}
```
Endpoints:
```
GET    /api/vendor-product-mappings/
PUT    /api/vendor-product-mappings/{id}/
DELETE /api/vendor-product-mappings/{id}/
```
#### Product → Course Mapping
Create mapping:
```
POST /api/product-course-mappings/
```
Example request:
```
{
  "product": 1,
  "course": 1,
  "primary_mapping": true,
  "is_active": true
}
```
Endpoints:
```
GET    /api/vendor-product-mappings/
PUT    /api/vendor-product-mappings/{id}/
DELETE /api/vendor-product-mappings/{id}/
```
#### Course → Certification Mapping
Create mapping:
```
POST /api/course-certification-mappings/
```
Example request:
```
{
  "course": 1,
  "certification": 1,
  "primary_mapping": true,
  "is_active": true
}
```
Endpoints:
```
GET    /api/vendor-product-mappings/
PUT    /api/vendor-product-mappings/{id}/
DELETE /api/vendor-product-mappings/{id}/
```
### 8. Validation Rules

The following rules are enforced by the API:
```
Required field validation

Unique code for master entities

Duplicate mapping prevention

Valid foreign key references

Only one primary_mapping=True allowed per parent entity
```

Example:

A vendor cannot have two primary product mappings.
