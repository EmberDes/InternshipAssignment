# Django REST Framework Assignment

This project is a backend API built using **Django** and **Django REST Framework (DRF)**.  
It manages relationships between **Vendors, Products, Courses, and Certifications** using mapping tables and provides fully functional REST APIs.

Swagger documentation is included for easy API testing.

---

## Tech Stack

- Python
- Django
- Django REST Framework
- drf-yasg (Swagger API Documentation)
- SQLite (default Django database)

---

## Project Structure


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
├── config/ (project settings)
├── manage.py


---

## Features Implemented

### Master Entities
The following master entities are implemented:

- Vendor
- Product
- Course
- Certification

Each entity contains:

- id
- name
- code
- description
- is_active
- created_at
- updated_at

---

### Mapping Relationships

The system supports the following mappings:

| Mapping | Description |
|------|------|
| Vendor → Product | Vendors can be mapped to multiple products |
| Product → Course | Products can be mapped to courses |
| Course → Certification | Courses can be mapped to certifications |

---

### Validations Implemented

The following validations are enforced:

- Required field validation
- Unique `code` for master records
- Duplicate mapping prevention
- Valid foreign key references
- Only **one `primary_mapping=True` allowed per parent**

Example:

Vendor → only one primary product allowed.

---

## API Endpoints

### Vendor


GET /api/vendors/
POST /api/vendors/
GET /api/vendors/{id}/
PUT /api/vendors/{id}/
DELETE /api/vendors/{id}/


### Product


GET /api/products/
POST /api/products/
GET /api/products/{id}/
PUT /api/products/{id}/
DELETE /api/products/{id}/


### Course


GET /api/courses/
POST /api/courses/
GET /api/courses/{id}/
PUT /api/courses/{id}/
DELETE /api/courses/{id}/


### Certification


GET /api/certifications/
POST /api/certifications/
GET /api/certifications/{id}/
PUT /api/certifications/{id}/
DELETE /api/certifications/{id}/


### Mapping APIs

Vendor → Product


GET /api/vendor-product-mappings/
POST /api/vendor-product-mappings/
PUT /api/vendor-product-mappings/{id}/
DELETE /api/vendor-product-mappings/{id}/


Product → Course


GET /api/product-course-mappings/
POST /api/product-course-mappings/
PUT /api/product-course-mappings/{id}/
DELETE /api/product-course-mappings/{id}/


Course → Certification


GET /api/course-certification-mappings/
POST /api/course-certification-mappings/
PUT /api/course-certification-mappings/{id}/
DELETE /api/course-certification-mappings/{id}/


---

## Swagger Documentation

Swagger UI is available for interactive API testing.

Open in browser:


http://127.0.0.1:8000/swagger/


---

## Setup Instructions

### 1. Clone Repository


git clone <repository-url>
cd project


### 2. Create Virtual Environment


python -m venv venv


Activate environment:

Windows


venv\Scripts\activate


Linux / Mac


source venv/bin/activate


---

### 3. Install Dependencies


pip install -r requirements.txt


---

### 4. Apply Migrations


python manage.py migrate


---

### 5. Run Development Server


python manage.py runserver


Server will start at:


http://127.0.0.1:8000/


---

## Testing APIs

You can test APIs using:

- Swagger UI
- Postman
- curl

Swagger is recommended for quick testing.

---

## Notes

- SQLite is used for development.
- Migrations are included to allow easy database setup.
- Database file (`db.sqlite3`) is excluded from version control.

---

## Author

Assignment submission for Django Backend Internship.
