from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.forms.widgets import RadioSelect
from multiselectfield import MultiSelectField



trade_list = (
('mansory', 'Mansory'),
('furniture', 'Furniture'),
('welding', 'Welding'),
('automobile', 'Automobile'),
('computer', 'Computer'),
)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    #trade = forms.MultipleChoiceField(
    #    required=False,
     #   widget=forms.CheckboxSelectMultiple,
    #    choices=trade_list,
   # )

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']




class UserUpdateForm(forms.ModelForm):

    #email = forms.EmailField()        - I removed this to see the dynamism

    class Meta:
        model = User
        fields = ['first_name', 'last_name']

NGO_CHOICES = (
('one', 'ONE'),
('two', 'TWO'),
('three', 'THREE'),
)
class ProfileUpdateForm(forms.ModelForm):
    #ngo = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=NGO_CHOICES, required=False)

    class Meta:
        model = Profile
        fields = ['image', 'phone', 'bio', 'country', 'gender', 'trade']
        widgets = {
            'gender': forms.RadioSelect()
        }


