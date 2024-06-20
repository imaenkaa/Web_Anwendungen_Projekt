from flask import Blueprint, render_template, session, redirect, url_for, flash
from models import Habit, LogHabit
from datetime import datetime

main_bp = Blueprint('main', __name__,template_folder='templates')

@main_bp.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    user_id = session['user_id']
    habits = Habit.query.filter_by(user_id=user_id).all()

    if not habits:
        flash('You have no habits yet. Let\'s create one!', 'info')
        return redirect(url_for('habits.add_habit'))

    today = datetime.today().date()
    today_logs = {habit.id: LogHabit.query.filter_by(habit_id=habit.id, date=today).first() for habit in habits}
    return render_template('index.html', habits=habits, today=today, today_logs=today_logs)
