from django import forms
from .models import *

class form(forms.ModelForm):
        class Meta:
              model=enquiry
              fields='__all__'