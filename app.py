from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

app = Flask(__name__, static_folder='assets/static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.init_app(app)

db.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template("index.html", user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))

    return render_template('login.html', user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        
        name = request.form.get('name')
        password = request.form.get('password')

        if not name:
            flash('Name is required', 'error')
            return redirect(url_for('editprofile'))

        current_user.name = name

        if password:
            current_user.password = generate_password_hash(password)

        db.session.commit()

        flash('Profile updated successfully', 'success')
        return redirect(url_for('edit_profile'))
    return render_template('edit_profile.html', user=current_user)

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # รับข้อมูลจากฟอร์ม
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')

        if not username:
            flash('Username is required', 'error')
            return redirect(url_for('register'))

        user_exists = User.query.filter_by(username=username).first()
        if user_exists:
            flash('Username already exists', 'error')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, name=name, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.route('/my_course')
def my_course():
    return render_template("my_course.html")

@app.route('/market_detail_1')
def market_1():
    return render_template("market/market_detail_1.html")

@app.route('/market_detail_2')
def market_2():
    return render_template("market/market_detail_2.html")

@app.route('/market_detail_3')
def market_3():
    return render_template("market/market_detail_3.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)