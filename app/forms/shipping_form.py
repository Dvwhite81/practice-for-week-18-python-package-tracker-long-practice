from flask_wtf import FlaskForm
from wtforms import (
    BooleanField, SelectField, StringField, SubmitField
)
from wtforms.validators import DataRequired
from map.map import map


class ShippingForm(FlaskForm):
    sender = StringField("Sender", validators=[DataRequired()])
    recipient = StringField("Recipient", validators=[DataRequired()])
    origin = SelectField("Origin", choices=list(map), validators=[DataRequired()])
    destination = SelectField("Destination", choices=list(map), validators=[DataRequired()])
    express = BooleanField("Express Shipping")
    submit = SubmitField("Submit")
