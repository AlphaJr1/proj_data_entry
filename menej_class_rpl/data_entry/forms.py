from django import forms
from .models import Pengguna, Content

STATES = (
    ('', 'Choose...'),
    ('DKI', 'DKI Jakarta'),
    ('DIY', 'DIY Yogyakarta'),
    ('JABAR', 'Jawa Barat')
)

class AddresForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(render_value=True, attrs={'placeholder':'Password'}))
    addres_1 =  forms.CharField(
        label='Addres_1',
        widget=forms.TextInput(attrs={'placeholder':'1234 Main St'})
    )
    addres_2 =  forms.CharField(
        label='Addres_2',
        widget=forms.TextInput(attrs={'placeholder':'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

class PenggunaForm(forms.ModelForm):
    state = forms.ChoiceField(choices=STATES)
    class Meta:
        model = Pengguna
        exclude = ['tanggal_join',]

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        exclude = ['created_at']
