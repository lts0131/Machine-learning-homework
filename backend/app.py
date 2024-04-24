from flask import Flask, request, render_template, jsonify, abort
import os
import json
from db.databaseConnection import DatabaseConnection
from flask_cors import CORS
from accuracy.accuracy_cnn import AccuracyCNN
from accuracy.accuracy_fcnn import AccuracyFCNN
from use_model.use_model_cnn import USECNN
from use_model.use_model_full import USEFCNN
from train.model_cnn import Train_CNN
from train.model_touch import Train_Fcnn

# Sets the type of file that is allowed to be uploaded
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__, template_folder="../frontend/dist",static_folder="../frontend/dist/static")
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5000"}})


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:5000'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


# Main interface
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# Login interface
@app.route('/login', methods=["POST"])
def login():
    db = DatabaseConnection()
    username = request.json.get("username")
    password = request.json.get("password")
    c = db.conn.cursor()
    query = "SELECT * FROM user_info WHERE user_name = '%s' AND password = '%s'" % (username, password)
    posts = c.execute(query).fetchall()
    results = []
    for row in posts:
        results.append(dict(zip([column[0] for column in c.description], row)))
    json_str = json.dumps(results)
    c.close()
    return json_str


# Check that the file extension allows uploading
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Uploaded interface
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if any files have been uploaded
        if 'file' not in request.files:
            return 'No file uploaded', 400
        file = request.files['file']
        # Check whether the documents meet the requirements
        if file and allowed_file(file.filename):
            # Save the uploaded file
            filename = file.filename
            path = os.path.join("templates/static/" + filename)
            file.save(path)
            cnn_use = USECNN.use_cnn(path)
            fcnn_use = USEFCNN.use_fcnn(path)
            data = {'fcnn_use': fcnn_use, 'cnn_use': cnn_use}
            response = jsonify(data)
            return response
        else:
            return 'Invalid file', 400


# Train interface
@app.route('/train')
def train():
    response = jsonify("success")
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# Train interface
@app.route('/accuracy')
def get_accuracy():
    fcnn_accuracy = AccuracyFCNN()
    cnn_accuracy = AccuracyCNN()
    data = {'fcnn_accuracy': fcnn_accuracy.fcnn_accuracy(), 'cnn_accuracy': cnn_accuracy.cnn_accuracy()}
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# Train interface
@app.route('/predict')
def get_predict():
    response = jsonify({})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# 404 interface
@app.route('/_404')
def _404():
    abort(404, 'Oops, 404.')


# Main method
if __name__ == '__main__':
    app.run()
