import json
import plotly
import plotly.graph_objects as go 
from app.utils.json_paser import Parser
from .datachart import create_graph
from flask import Flask, render_template, send_file, request, redirect, url_for
from flask import Blueprint

view_blueprint = Blueprint('view', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)\
        [1].lower() in ALLOWED_EXTENSIONS

# Process json data and drawing the graph of the parse data
@view_blueprint.route('/upload', methods=['POST', 'GET'])
def upload_file():
    result = []
    if  request.methods == 'POST':
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        key_data = request.get['json_key']
        key_data = key_data.split()
        if file.filename == '':
            print('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            try:
                f = open(filename, 'r')
                json_obj = json.load(f)
                res = Parser.parse_data(json_obj, key_data)
                result.append(res)
                print(res)
                f.close()
            except IOError:
                print ('parameters error')
        JsonData = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)
        return JsonData


@view_blueprint.route('/dashboard')
def index():
    pie = create_graph()
    return render_template('dashbord.html', graph_value=pie)
    



