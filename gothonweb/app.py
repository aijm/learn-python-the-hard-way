import os
from flask import Flask, request, url_for
from flask import render_template
from flask import send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.getcwd()
print("upload folder:", UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','gif'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# check filename to ensure it's allowed  
def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    

@app.route('/', methods=['POST', 'GET'])
def upload_file():
    if request.method == "POST":
        file = request.files['file']
        print('filename: ', file.filename)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_url = url_for('uploaded_file', filename = filename)
            return render_template("img_form.html",file_url=file_url)
    else:
        return render_template("img_form.html")

@app.route('/hello', methods=['POST', 'GET'])
def index():
    greeting = "Hello World"

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")


if __name__ == "__main__":
    app.run()