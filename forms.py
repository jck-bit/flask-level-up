from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, Email, EqualTo

class registrationform(FlaskForm):
    username = StringField('username',
                          validators=[DataRequired(), length(min=2, max=20)])
    email = StringField('Email',
                          validators=[DataRequired(), Email() ])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password',
                                         validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('sign up')



class LoginForm(FlaskForm):
    email = StringField('Email',
                          validators=[DataRequired(), Email() ])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')
