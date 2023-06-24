from django import forms

from FruitipediaApp.profile_app.models import ProfileModel


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class CreateProfileForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        fields = ['first_name', 'last_name', 'email', 'password']
        labels = {
            'first_name': False,
            'last_name': False,
            'email': False,
            'password': False
        }
        widgets = {
        }


