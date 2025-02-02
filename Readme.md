# **FAQ Management System**

## **Features**
- **FAQ Management**: Create, read, update, and delete FAQs.
- **Multilingual Support**: Automatically translate FAQs into multiple languages (e.g., Hindi, Bengali).
- **WYSIWYG Editor**: Use CKEditor for rich text formatting of answers.
- **Caching**: Improve performance with Redis caching.
- **REST API**: Fully functional API for managing FAQs.
- **Admin Panel**: User-friendly interface for managing FAQs.

---

## **Technologies Used**
- **Backend**: Django, Django REST Framework
- **Database**: SQLite (default), PostgreSQL (optional)
- **Caching**: Redis
- **WYSIWYG Editor**: django-ckeditor
- **Translation**: googletrans
- **Testing**: pytest
- **Containerization**: Docker (optional)

---

## **Installation**

### **Prerequisites**
- Python 3.9 or higher
- Redis (for caching)
- Docker (optional)

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/faq_project.git
   cd faq_project
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser for the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

7. Start the Redis server:
   ```bash
   redis-server
   ```

8. Run the development server:
   ```bash
   python manage.py runserver
   ```

9. Access the application at `http://localhost:8000`.

---

## **API Usage**

### **Base URL**
```
http://localhost:8000/api/faqs/
```

### **Endpoints**
1. **Fetch All FAQs** (GET):
   ```bash
   curl http://localhost:8000/api/faqs/
   ```

2. **Fetch FAQs in a Specific Language** (GET):
   ```bash
   curl http://localhost:8000/api/faqs/?lang=hi  # Hindi
   curl http://localhost:8000/api/faqs/?lang=bn  # Bengali
   ```

3. **Create a New FAQ** (POST):
   ```bash
   curl -X POST http://localhost:8000/api/faqs/ \
   -H "Content-Type: application/json" \
   -d '{
       "question": "What is Python?",
       "answer": "Python is a programming language."
   }'
   ```

4. **Fetch a Single FAQ** (GET):
   ```bash
   curl http://localhost:8000/api/faqs/1/
   ```

5. **Update an FAQ** (PUT):
   ```bash
   curl -X PUT http://localhost:8000/api/faqs/1/ \
   -H "Content-Type: application/json" \
   -d '{
       "question": "What is Django?",
       "answer": "Django is a web framework for Python."
   }'
   ```

6. **Delete an FAQ** (DELETE):
   ```bash
   curl -X DELETE http://localhost:8000/api/faqs/1/
   ```

---

## **Admin Panel**
1. Access the admin panel at `http://localhost:8000/admin`.
2. Log in with your superuser credentials.
3. Manage FAQs from the admin interface.

---

## **Running with Docker**

### **Steps**
1. Build the Docker image:
   ```bash
   docker-compose build
   ```

2. Start the containers:
   ```bash
   docker-compose up
   ```

3. Access the application at `http://localhost:8000`.

---

## **Testing**
Run unit tests using pytest:
```bash
python manage.py test
```

---

## **Caching**
- Redis is used for caching API responses.
- FAQs are cached for 15 minutes to improve performance.
