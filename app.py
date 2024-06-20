from flask import Flask, render_template, request, redirect, url_for, flash,session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required,current_user
from flask_migrate import Migrate
from models import User, Habit, LogHabit, Goal,Badge,UserBadge,Freeze
from models import db
from datetime import datetime, timedelta
from habits.routes import habits_bp
from auth.routes import auth_bp
from badges.routes import badges_bp
from main.routes import main_bp



app = Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(badges_bp)
app.register_blueprint(habits_bp)

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)
migrate = Migrate(app, db)


login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@app.cli.command("init-badges")
def init_badges():
    badges = [
        {
            "name": "Silver",
            "description": "Awarded for 7 consecutive days streak",
            "streak_required": 7
        },
        {
            "name": "Gold",
            "description": "Awarded for 15 consecutive days streak",
            "streak_required": 15
        },
        {
            "name": "Ace",
            "description": "Awarded for 30 consecutive days streak",
            "streak_required": 30
        }
    ]

    for badge in badges:
        existing_badge = Badge.query.filter_by(name=badge['name']).first()
        if not existing_badge:
            new_badge = Badge(name=badge['name'], description=badge['description'], streak_required=badge['streak_required'])
            db.session.add(new_badge)
    
    db.session.commit()
    print("Badges initialized successfully!")



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    
    with app.app_context():        
        db.create_all()
    app.run(debug=True)
