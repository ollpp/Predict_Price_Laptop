from flask import Blueprint, render_template, request, url_for
import pandas as pd
import pickle
import os.path
import sklearn

bp = Blueprint('main', __name__, url_prefix='/')

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))


def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return src
    except IOError as exc:
        return str(exc)

@bp.route('/')
def init_dipl():
    return 'first!'

@bp.route('/modeling', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        #temp = request.form['num']
        pass

    elif request.method == 'GET':

        size = request.args.get('display_size')
        os = request.values.get('os')
        cpu = request.args.get('cpu')
        chipset = request.args.get('chipset')
        ram = request.args.get('ram')
        resol = request.args.get('resol')
        video = request.args.get('video')
        ssd = request.args.get('ssd')
        weight = request.args.get('weight')

        select = [float(size), os, cpu, chipset, float(2.25), float(ram), resol, video, float(ssd), weight]

        model = None
        pipe = get_file('model.pkl')
        with open(pipe,'rb') as pickle_file:
            model = pickle.load(pickle_file)
        
        predict_X = pd.DataFrame(select).T
        predict_X.columns = ['screen_size-inch', 'release_OS', 'CPU', 'chipset', 'CPU_speed-GHz', 'RAM-GB', 'resolution', 'video_output', 'SSD-GB', 'weight-kg']

        rslt = int(model.predict(predict_X)[0])

    return render_template('answer.html', rslt = rslt)


@bp.route('/main')
def main_displ():
    return render_template('main.html')
