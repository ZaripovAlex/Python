from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired


class SearchF(FlaskForm):
    seach = EmailField("Поиск", validators=[DataRequired()])
    searchButton = SubmitField("Найти")
