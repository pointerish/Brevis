from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, URL
from wtforms import StringField, SubmitField

class URLForm(FlaskForm):
    url = StringField("URL:", validators=[DataRequired(), URL()])
    submit = SubmitField("Submit")