from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField, TextAreaField, SelectField
from wtforms.validators import InputRequired, AnyOf, URL, NumberRange, Optional


def lowercase_filter(value):
    if value:
        return value.lower()
    return value


class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[
        InputRequired(message="Pet name is required")
    ])
    species = StringField("Species",
                          filters=[lowercase_filter],
                          validators=[AnyOf(["cat", "dog", "porcupine"],
                                            message="Species should be either 'cat', 'dog', or 'porcupine'")])
    photo_url = URLField("Image Link", validators=[
        Optional(),
        URL(message="Please provide a valid URL")
    ])
    age = IntegerField("Age", validators=[
        Optional(),
        NumberRange(min=0, max=30, message="Age should be between 0 and 30")
    ])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    photo_url = StringField('Photo URL', validators=[
        Optional(),
        URL(message="Please provide a valid URL")
    ])
    notes = TextAreaField('Notes', validators=[Optional()])
    available = SelectField('Availability', choices=[('--Select Availability--', '--Select Availability--'), (
        'True', 'Available'), ('False', 'Not Available')])
