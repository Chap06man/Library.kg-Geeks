from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

GENDER = (
        ("M", "M"),
        ("Ж", "Ж")
    )
class CustomRegisterForm(UserCreationForm):
    #10 поля 
    photo = forms.ImageField(required=True)
    last_name = forms.CharField(max_length=20, required=True)
    day_birth = forms.DateField(required=True)
    email = forms.EmailField(required=True)
    location = forms.CharField(required=True, max_length=30)
    phone_number = forms.CharField(max_length=15, required=True, initial='+996')
    gender = forms.ChoiceField(choices=GENDER, required=True)
    city = forms.CharField(max_length=15,required=True)
    prof = forms.CharField(max_length=15)
    hobby = forms.CharField(max_length=50)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'photo',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'day_birth',
            'location',
            'gender',
            'city',
            'prof',
            'hobby',
            'captcha',
        )
        def save(self, commit=True):
            user = super(CustomRegisterForm, self).save(commit=False)
            user.email = self.cleaned_data[ 'email']
            user.phone_number = self.cleaned_data['phone_number']
            user.day_birth = self.cleaned_data['day_birth']
            user.city = self.cleaned_data['city']
            user.prof = self.cleaned_data['prof']
            user.hobby = self.cleaned_data['hobby']

            if commit:
                user.save()
            return user
        