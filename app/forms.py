from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo

class FormativeSummativeScaleForm(FlaskForm):
    formative_weight = StringField("Formative Weight", validators=[DataRequired()])
    summative_weight = StringField("Summative Weight", validators=[DataRequired()])
    total_number_of_assignments = StringField("Total Number of Assignments", validators=[DataRequired()])

    submit = SubmitField("Save")

class FormativeSummativeAssignmentsForm(FlaskForm):
    assignment_name = StringField("Assignment Name", validators=[DataRequired()])
    assignment_weight = StringField("Assignment Weight", validators=[DataRequired()])
    assignment_user_points = StringField("Assignment Points Received", validators=[DataRequired()])
    assignment_max_points = StringField("Assignment Maximum Points Receviable", validators=[DataRequired()])

    submit = SubmitField("Save")

