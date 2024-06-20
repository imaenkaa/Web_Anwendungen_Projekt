from flask_login import UserMixin
from datetime import datetime,timedelta
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    habits = db.relationship('Habit', backref='user', lazy=True)

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    category = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date,nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    logs = db.relationship('LogHabit', backref='habit', lazy=True)
    highest_streak = db.Column(db.Integer, default=0)
  

class LogHabit(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        date = db.Column(db.Date, nullable=False)
        completed = db.Column(db.Boolean, nullable=False, default=False)
        notes = db.Column(db.String(200))
        habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'), nullable=False)


class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    target_date = db.Column(db.Date, nullable=False)
    achieved = db.Column(db.Boolean, nullable=False, default=False)
    start_date = db.Column(db.Date, nullable=False)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'), nullable=False)
    habit = db.relationship('Habit', backref=db.backref('goals', lazy=True)) 
    progress = db.Column(db.Integer, default=0)
    Result=db.Column(db.String(200))


class Badge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    streak_required = db.Column(db.Integer, nullable=False)


class UserBadge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    badge_id = db.Column(db.Integer, db.ForeignKey('badge.id'), nullable=False)
    date_awarded = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('user_badges', lazy=True))
    badge = db.relationship('Badge', backref=db.backref('user_badges', lazy=True))
    habit = db.relationship('Habit', backref=db.backref('user_badges', lazy=True))


class Freeze(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)

# Remember to migrate the changes

