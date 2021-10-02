from flask_wtf import FlaskForm, csrf

from wtforms import BooleanField, StringField, validators

class TaskForm(FlaskForm):
    name = StringField("Task name", validators = [validators.Length(min=2)])
    done = BooleanField("Done")
    #Change later
    class Meta:
        csrf = False