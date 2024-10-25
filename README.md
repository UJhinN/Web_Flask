# Learning Flask with Thai Ghost Story Website 🎓

This project serves as a learning resource for Flask web development through building a Thai ghost story website. Perfect for beginners who want to understand Flask's core concepts through practical implementation.

## 📚 What You'll Learn

1. **Flask Basics**
   - Route handling and URL mapping
   - Template rendering with Jinja2
   - Static file management
   - Request handling (GET/POST methods)

2. **Database Integration**
   - SQLAlchemy ORM setup
   - Database models and relationships
   - CRUD operations

3. **User Authentication**
   - User registration and login system
   - Password hashing
   - Session management with Flask-Login
   - Protected routes with decorators

4. **Web Forms**
   - Form handling
   - Input validation
   - Flash messages
   - File uploads

5. **Project Structure**
   - Organizing Flask applications
   - Blueprint implementation
   - Configuration management

## 🚀 Getting Started

### Prerequisites
- Basic Python knowledge
- Understanding of HTML/CSS
- Python 3.7 or higher installed

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/UJhinN/Web_Flask.git
cd Web_Flask
```

2. Set up a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Code Examples

### 1. Route Creation
```python
@app.route('/blog')
def blog():
    return render_template("blog.html")
```

### 2. User Authentication
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Authentication logic
```

### 3. Database Models
```python
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
```

## 📁 Project Structure Explanation
```
Web_Flask/
├── main.py              # Application entry point
├── models.py            # Database models
├── templates/           # HTML templates
│   ├── Story/          # Story templates
│   ├── login.html      # Authentication templates
│   └── ...
└── assets/             # Static files
```

## 🎯 Learning Exercises

1. **Basic Exercises**
   - Add a new route for a contact page
   - Create a new template
   - Add form validation

2. **Intermediate Challenges**
   - Implement user comments
   - Add image upload functionality
   - Create an admin panel

3. **Advanced Projects**
   - Add user roles and permissions
   - Implement API endpoints
   - Add search functionality

## 🛠 Running the Application

1. Start the development server:
```bash
python main.py
```

2. Access the website at:
```
http://localhost:5000
```

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Flask-Login Documentation](https://flask-login.readthedocs.io/)

## 🤝 Contributing

Feel free to:
1. Fork the repository
2. Create your feature branch
3. Submit a pull request with your improvements

## 📝 License

This project is licensed under the MIT License.
