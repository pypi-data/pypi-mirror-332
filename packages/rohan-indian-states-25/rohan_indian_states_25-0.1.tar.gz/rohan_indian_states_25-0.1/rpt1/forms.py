from django import forms
from .states import INDIAN_STATES  # Ensure correct import

class StateSelection(forms.Select):
    def __init__(self, attrs=None):
        super().__init__(attrs=attrs, choices=INDIAN_STATES)
