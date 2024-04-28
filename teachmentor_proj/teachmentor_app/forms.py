from django import forms
from django.contrib.auth.models import User
from .models import FeedBackMessage, Course


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedBackMessage
        fields = ['name', 'email', 'message']


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['course_name', 'description', 'book_link', 'video_link']
