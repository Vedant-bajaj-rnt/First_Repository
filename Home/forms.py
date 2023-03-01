from django import forms
from .models import user

class UserRegForm(forms.ModelForm):
    class meta:
        model = user
        field = ('Userid','Password')
        widgets = {'Password': forms.PasswordInput(render_value=True),}