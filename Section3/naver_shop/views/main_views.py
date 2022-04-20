from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def init_dipl():
    return 'first!'

@bp.route('/hello')
def index():
    return 'Pybo index'

@bp.route('/main')
def main_displ():
    return render_template('main.html')
