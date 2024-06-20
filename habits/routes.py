from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_required, current_user
from datetime import datetime, timedelta
from models import Habit, LogHabit, Goal, Freeze, UserBadge, Badge, db

habits_bp = Blueprint('habits', __name__,template_folder='templates')


@habits_bp.route('/add_habit', methods=['GET', 'POST'])
def add_habit():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        category = request.form.get('category')
        user_id = session['user_id']

        new_habit = Habit(name=name, description=description, start_date=datetime.today().date(), category=category, user_id=user_id)
        db.session.add(new_habit)
        db.session.commit()

        flash('Habit added successfully!', 'success')
        return redirect(url_for('main.home'))

    return render_template('habit/create_habit.html')

@habits_bp.route('/habit/<int:habit_id>', methods=['GET', 'POST'])
def view_habit(habit_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    habit = Habit.query.get_or_404(habit_id)
    logs = LogHabit.query.filter_by(habit_id=habit_id).order_by(LogHabit.date.asc()).all()
    goals = Goal.query.filter_by(habit_id=habit_id).all()
    freezes = Freeze.query.filter_by(habit_id=habit_id).all()
    freeze_dates = {freeze.date for freeze in freezes}

    streak = 0
    if logs:
        reversed_arr = logs[::-1]
        current_date = reversed_arr[0].date
        i = 0
        while i < len(reversed_arr):
            log = reversed_arr[i]
            if current_date in freeze_dates:
                current_date -= timedelta(days=1)
                i -= 1
            elif log.completed and log.date == current_date:
                streak += 1
                current_date -= timedelta(days=1)
            else:
                break
            i += 1
        if streak > habit.highest_streak:
            habit.highest_streak = streak
            db.session.commit()

    for goal in goals:
        progress = 0
        goal_start_date = goal.start_date
        log_date = goal_start_date
        consecutive_days = 0
        goal_achieved = False
        while log_date <= goal.target_date:
            log = LogHabit.query.filter_by(habit_id=habit_id, date=log_date).first()
            if log and log.completed:
                consecutive_days += 1
                progress += 1
            elif log_date in freeze_dates:
                log_date += timedelta(days=1)
                progress += 1
                continue
            elif log and not log.completed:
                consecutive_days = 0
                goal.achieved = False
                if goal.Result != "Success" and goal.Result != "Failed":
                    flash(f"Failed to achieve goal from {goal.start_date} to {goal.target_date}", "danger")
                goal.Result = "Failed"
                break
            else:
                goal.achieved = False
                break
            log_date += timedelta(days=1)
        else:
            goal.achieved = True
            if goal.Result != "Success" and goal.Result != "Failed":
                flash(f"You successfully achieved your goal from {goal.start_date} to {goal.target_date}", "success")
            goal.Result = "Success"
        goal.progress = int((progress / ((goal.target_date - goal_start_date).days + 1)) * 100)
        db.session.commit()

    user_id = session['user_id']
    badge_name = ""
    if streak >= 30:
        badge = Badge.query.filter_by(name='Ace').first()
        badge_name = "Ace"
    elif streak >= 15:
        badge = Badge.query.filter_by(name='Gold').first()
        badge_name = "Gold"
    elif streak >= 7:
        badge = Badge.query.filter_by(name='Silver').first()
        badge_name = "Silver"
    else:
        badge = None
    if badge:
        user_badge = UserBadge.query.filter_by(user_id=user_id, badge_id=badge.id, habit_id=habit_id).first()
        if not user_badge:
            new_user_badge = UserBadge(user_id=user_id, badge_id=badge.id, habit_id=habit_id)
            db.session.add(new_user_badge)  
            db.session.commit()
            flash(f'Congratulations you have been awarded {badge_name} Badge', 'success')

    return render_template('habit/view_habit.html', habit=habit, logs=logs, goals=goals, streak=streak, freezes=freezes)

@habits_bp.route('/add_log/<int:habit_id>/<string:log_type>', methods=['GET', 'POST'])
def add_log(habit_id,log_type):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    today = datetime.today().date()
    habit = Habit.query.get_or_404(habit_id)    
    if request.method == 'POST':
        today = datetime.today().date()

    if request.method == 'POST':
        if log_type == 'today':
            date = today
        else:
            target_date_str = request.form.get('date')
            date = datetime.strptime(target_date_str, '%Y-%m-%d').date()


        completed = request.form.get('completed')
        notes = request.form.get('notes')

        if(completed!='True' and completed!='False'):
            completed = True if completed == 'on' else False
        if date < datetime.today().date():
            flash('You cannot add a log for a PAST date.', 'danger')
            return redirect(url_for('habits.add_log', habit_id=habit_id, log_type='other'))
        
        last_log = LogHabit.query.filter_by(habit_id=habit_id).order_by(LogHabit.date.desc()).first()
        if last_log:
            missing_dates = []
            current_date = last_log.date + timedelta(days=1)
            while current_date < date:
                missing_dates.append(current_date)
                current_date += timedelta(days=1)

            if missing_dates:
                missing_dates_str = ', '.join([d.strftime('%Y-%m-%d') for d in missing_dates])
            

                # Prompt the user with a confirmation dialog
                # (Assume the confirmation comes as a form submission with `confirm` field)
                if not request.form.get('confirm'):
                    flash(f'You have missing logs for the following dates: {missing_dates_str}. Confirm to add these as incomplete logs.', 'warning')
                    return render_template('/habit/confirm_add_log.html', habit=habit, missing_dates=missing_dates_str, date=target_date_str, completed=completed, notes=notes,last_date=last_log.date,log_type=log_type)

            
                for missing_date in missing_dates:
                    missing_log = LogHabit(date=missing_date, completed=False, notes='', habit_id=habit_id)
                    db.session.add(missing_log)

        existing_log = LogHabit.query.filter_by(habit_id=habit_id, date=date).first()
        if existing_log and not completed:
            flash('A log for this date already exists.', 'danger')
            return redirect(url_for('habits.view_habit', habit_id=habit_id))

        existing_log = LogHabit.query.filter_by(habit_id=habit_id, date=date).first()

        if existing_log:
            if completed and not existing_log.completed:
                # Update the existing log
                existing_log.completed = completed
                existing_log.notes = notes
                db.session.commit()
                flash('Log updated successfully!', 'success')
                return redirect(url_for('habits.view_habit', habit_id=habit_id))
            else:
                flash('A log for this date already exists.', 'danger')
                return redirect(url_for('habits.view_habit', habit_id=habit_id))
        if(completed!=True and completed!=False):
            comp=True if completed=='True' else False
        else:
            comp=completed

        # If no existing log found, add a new log
        new_log = LogHabit(date=date, completed=comp, notes=notes, habit_id=habit_id)
        db.session.add(new_log)
        db.session.commit()

        flash('Log added successfully!', 'success')
        return redirect(url_for('habits.view_habit', habit_id=habit_id))

    return render_template('habit/add_log.html', habit=habit,today_date=today,log_type=log_type)


@habits_bp.route('/add_goal/<int:habit_id>', methods=['GET', 'POST'])
def add_goal(habit_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    habit = Habit.query.get_or_404(habit_id)
    if request.method == 'POST':
        target_date = datetime.strptime(request.form.get('target_date'), '%Y-%m-%d').date()
        
        logs = LogHabit.query.filter_by(habit_id=habit_id).order_by(LogHabit.date.asc()).all()
        current_date=datetime.now()
        if(logs):
            reversed_arr = logs[::-1]
            current_date = reversed_arr[0].date
            if target_date <= current_date:
                flash(f'You have already logged for {current_date}. Please set goal for a future date.', 'danger')
                return redirect(url_for('habits.view_habit', habit_id=habit_id))
        new_goal = Goal(habit_id=habit_id,start_date=current_date + timedelta(days=1) , target_date=target_date)
        db.session.add(new_goal)
        db.session.commit()

        flash('Goal added successfully!','success')
        return redirect(url_for('habits.view_habit', habit_id=habit_id))

    return render_template('/habit/add_goal.html', habit=habit)

@habits_bp.route('/freeze_habit/<int:habit_id>', methods=['GET', 'POST'])
def freeze_habit(habit_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    habit = Habit.query.get_or_404(habit_id)

    if request.method == 'POST':
        date_str = request.form.get('dates')
        if date_str:
            date_list = date_str.split(', ')
            for date_text in date_list:
                try:
                    date = datetime.strptime(date_text, '%m/%d/%Y').date()
                    freeze = Freeze(date=date, habit_id=habit_id)
                    db.session.add(freeze)
                except ValueError:
                    flash('Error in date format. Please try again.', 'danger')
                    return redirect(url_for('freeze_habit', habit_id=habit_id))

            db.session.commit()
            flash('Habit frozen successfully!', 'success')
            return redirect(url_for('habits.view_habit', habit_id=habit_id))

    return render_template('/habit/freeze_habit.html', habit=habit)



@habits_bp.route('/habit/<int:habit_id>/dashboard')
def habit_dashboard(habit_id):
    habit = Habit.query.get_or_404(habit_id)

    logs = LogHabit.query.filter_by(habit_id=habit_id).order_by(LogHabit.date.asc()).all()
    goals = Goal.query.filter_by(habit_id=habit_id).all()
    freezes = Freeze.query.filter_by(habit_id=habit_id).all()
    freeze_dates = set(freeze.date for freeze in freezes)
    # Calculate current streak

    streak = 0
    total_days=0
    completed_days=0
    skipped_days=0
    progress=0
    if(logs):
        reversed_arr = logs[::-1]
        current_date = reversed_arr[0].date
        i = 0
        while i < len(reversed_arr):
            log = reversed_arr[i]
            if current_date in freeze_dates:
                current_date -= timedelta(days=1)
                i-=1
            elif log.completed and log.date == current_date:
                streak += 1
                current_date -= timedelta(days=1)
            else:
                break
            i += 1

        reversed_arr = logs[::-1]
        current_date = reversed_arr[0].date
        total_days = (current_date - habit.start_date).days + 1
        completed_days = LogHabit.query.filter_by(habit_id=habit.id, completed=True).count()
        progress = int((completed_days / total_days) * 100) if total_days > 0 else 0
    # Calculate progress
   

    # Get all goal details
    goals = Goal.query.filter_by(habit_id=habit.id).all()

    return render_template('/habit/habit_dashboard.html', habit=habit, current_streak=streak,highest_streak=habit.highest_streak, progress=progress, goals=goals,total_days=total_days,completed_days=completed_days,skipped_days=total_days-completed_days)