from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from tabla1 import excel2mysql
from id_fechas import load_fechas

app = Flask(__name__,  static_folder='static')
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = '/tmp'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        load_fechas(file)
        return excel2mysql(file)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")


