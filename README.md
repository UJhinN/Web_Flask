# Learning Flask with Bootstrap - Thai Ghost Story Website 🎓

A learning project demonstrating how to build a responsive web application using Flask and Bootstrap. This project uses Thai ghost stories as engaging content while teaching web development fundamentals.

## 📚 Technology Stack

- **Backend**: Flask (Python Web Framework)
- **Frontend**: Bootstrap 5 (CSS Framework)
- **Database**: SQLAlchemy (ORM)
- **Authentication**: Flask-Login
- **Template Engine**: Jinja2

## 🎯 What You'll Learn

### 1. Flask Framework
- Route handling and URL mapping
- Template rendering with Jinja2
- Form processing
- User authentication
- Database operations

### 2. Bootstrap 5 Integration
- Responsive grid system
- Navigation components
- Forms styling
- Cards and content containers
- Modal dialogs
- Responsive tables
- Utility classes

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Basic understanding of HTML/CSS
- Text editor or IDE

### Installation

1. Clone the repository:
```bash
git clone https://github.com/UJhinN/Web_Flask.git
cd Web_Flask
```

2. Set up virtual environment:
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

### 1. Flask Template with Bootstrap
```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <!-- Navigation content -->
    </nav>

    <div class="container mt-4">
        {% block content %}{% endblock %}
    </div>

    <!-- Bootstrap JS Bundle -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

### 2. Form with Bootstrap Styling
```html
<!-- login.html -->
{% extends "base.html" %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card">
            <div class="card-body">
                <h3 class="card-title text-center">Login</h3>
                <form method="POST">
                    <div class="mb-3">
                        <label class="form-label">Username</label>
                        <input type="text" class="form-control" name="username" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Password</label>
                        <input type="password" class="form-control" name="password" required>
                    </div>
                    <button type="submit" class="btn btn-primary w-100">Login</button>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

## 📁 Project Structure
```
Web_Flask/
├── main.py                 # Flask application
├── models.py              # Database models
├── templates/
│   ├── base.html         # Base template with Bootstrap
│   ├── Story/            # Story templates
│   │   ├── Story_detail_1.html
│   │   └── ...
│   ├── login.html        # Authentication templates
│   └── ...
└── assets/
    └── static/           # Static files (CSS, JS, images)
```

## 🛠 Bootstrap Components Used

1. **Navigation**
   - Responsive navbar
   - Dropdown menus
   - Navigation pills/tabs

2. **Content Layout**
   - Grid system
   - Cards
   - Containers
   - Rows and columns

3. **Forms**
   - Input groups
   - Form validation
   - Custom styling

4. **Components**
   - Modals
   - Alerts
   - Badges
   - Buttons
   - Icons

## 💡 Learning Exercises

### Basic Level
1. Add a responsive navigation bar
2. Create a grid-based layout
3. Style forms using Bootstrap classes

### Intermediate Level
1. Implement modal dialogs
2. Add carousel for story previews
3. Create responsive tables

### Advanced Level
1. Custom Bootstrap theming
2. Advanced component integration
3. Responsive image galleries

## 🚀 Running the Application

1. Start the Flask server:
```bash
python main.py
```

2. Visit the website:
```
http://localhost:5000
```

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Bootstrap Examples](https://getbootstrap.com/docs/5.3/examples/)
- [Flask-Bootstrap](https://bootstrap-flask.readthedocs.io/)

## 🛠 Development Tips

1. **Browser DevTools**
   - Use for responsive design testing
   - Debug Bootstrap classes
   - Inspect element structure

2. **Bootstrap Utilities**
   - Spacing utilities (m-, p-)
   - Flexbox utilities
   - Text utilities
   - Background utilities

3. **Best Practices**
   - Mobile-first approach
   - Semantic HTML
   - Consistent spacing
   - Proper grid usage

