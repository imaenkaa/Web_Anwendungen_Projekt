from flask import Blueprint, render_template,session
from flask_login import login_required
from models import UserBadge

badges_bp = Blueprint('badges', __name__,template_folder='templates')

@badges_bp.route('/badges')
@login_required
def view_badges():
    user_id = session['user_id']
    badges = UserBadge.query.filter_by(user_id=user_id).all()
    print(badges)
    return render_template('badges/badges.html', badges=badges)
