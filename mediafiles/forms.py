from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image 
from django.contrib.auth import authenticate

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control custom-file-input'}),
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EmailOrUsernameLoginForm(forms.Form):
    identifier = forms.CharField(label='Username or Email', widget=forms.TextInput(attrs={'class': 'form-control py-2 px-3'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control py-2 px-3'}))

    def clean(self):
        cleaned_data = super().clean()
        identifier = cleaned_data.get('identifier')
        password = cleaned_data.get('password')

        if identifier and password:
            user = authenticate(username=identifier, password=password)
            if user is None:
                try:
                    # Try to get the username from the email
                    user_obj = User.objects.get(email=identifier)
                    user = authenticate(username=user_obj.username, password=password)
                except User.DoesNotExist:
                    raise forms.ValidationError("Invalid login credentials.")

            if user is None:
                raise forms.ValidationError("Invalid login credentials.")

            cleaned_data['user'] = user

        return cleaned_data