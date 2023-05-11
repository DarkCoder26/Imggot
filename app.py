from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import os
import cv2

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'webp', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'Super secret key'

def processImage(filename, operation):
    img = cv2.imread(f"uploads/{filename}")
    if operation == 'cgray':
            imgProcessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f"static/{filename}", imgProcessed)
            return filename
    else:
        print("Wrong ,error!!!!")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/edit', methods=["GET", "POST"])
def edit():
    operation = request.form.get('Operation')
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return "Error no file found."
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return "Error no file found."
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            processImage(filename, operation)
            flash(f"Your image is process and is available <a href='/static/{filename}'>here</a>")
            return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)