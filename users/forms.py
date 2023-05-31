from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password1','password2']

    def __init__(self,*args,**kwargs):
        super(CustomerUserCreationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder' : 'e.g. Nurillo'
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'e.g. Mahmudjonov'
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'class': 'input input--email',
                'placeholder': 'e.g. user@domain.com'
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'class': 'input input--password',
                'placeholder': '••••••••'
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'class': 'input input--password',
                'placeholder': '••••••••'
            }
        )