from flask import Blueprint, render_template

from app import db

bp = Blueprint('bp', __name__,
               template_folder='templates')

@bp.route('/')
def index():
    return render_template('index.html')
