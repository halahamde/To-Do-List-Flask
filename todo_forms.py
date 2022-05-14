from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField , IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegisrationForm(FlaskForm):
    id = IntegerField('ID',
                      validators=[DataRequired(),Length(min=8)])
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('sign up')
    
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    remember_me = BooleanField()
    submit = SubmitField('Login')

class AddTaskForm(FlaskForm):
    
    t_id = IntegerField('Task ID',
                        validators=[DataRequired()])

    t_title = StringField('Title',
                            validators=[DataRequired(), Length(min=5, max=50)])
    t_description = StringField('Description',
                            validators=[DataRequired(), Length(min=5, max=50)])
    t_status = StringField('Status',
                            validators=[DataRequired(), Length(min=5, max=50)])
    submit = SubmitField('Add')

class UpdateTaskForm(FlaskForm):
    t_id = IntegerField('Task ID',
                        validators=[DataRequired()])
    t_title = StringField('Title',
                            validators=[DataRequired(), Length(min=5, max=50)])
    t_description = StringField('Description',
                            validators=[DataRequired(), Length(min=5, max=50)])
    t_status = StringField('Status',
                            validators=[DataRequired(), Length(min=5, max=50)])
    submit = SubmitField('Update')


class DeleteTaskForm(FlaskForm):
    t_id = IntegerField('Task ID',
                        validators=[DataRequired()])
    submit = SubmitField('Delete')
    