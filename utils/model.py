from wtforms import Form, FloatField, validators, IntegerField
from math import pi

class InputForm(Form):
    StartF = IntegerField(
        label='Start Frequency (Hz)', default=9,
        validators=[validators.InputRequired()])
    StopF = IntegerField(
        label='Stop Frequency (Hz)', default=3,
        validators=[validators.InputRequired()])
    Offset = IntegerField(
        label='Offset ', default=2,
        validators=[validators.InputRequired()])
    Gain = IntegerField(
        label='Amplifier Gain ', default=18,
        validators=[validators.InputRequired()])