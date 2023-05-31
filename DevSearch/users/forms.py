from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from users.models import Profile, Skill


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

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['name','email','username','location','short_intro','bio','profile_image','social_github','social_instagram',
                'social_twitter','social_linkedin','social_telegram','social_whatsapp','social_website','social_youtube',
                'phone']

    def __init__(self,*args,**kwargs):
        super(ProfileUpdateForm,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update(
            {
                'class':'input input--text',
                'placeholder': 'e.g. Nurillo Mahmudjonov'
            }
        )
        self.fields['username'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'e.g. User'
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'e.g. user@domain.com'
            }
        )
        self.fields['location'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'e.g. Namangan, Uzbekiston'
            }
        )
        self.fields['short_intro'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'e.g. I Am A FullStack Developer'
            }
        )
        self.fields['bio'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'Bio'
            }
        )
        self.fields['social_github'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'e.g. https://github.com/username'
            }
        )
        self.fields['social_instagram'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'e.g. https://instagram.com/username'
            }
        )
        self.fields['social_twitter'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'e.g. https://twitter.com/username'
            }
        )
        self.fields['social_linkedin'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'e.g. https://linkedin.com/username'
            }
        )
        self.fields['social_telegram'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'e.g. https://t.me//username'
            }
        )
        self.fields['social_whatsapp'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'e.g. https://whatsapp.com/username'
            }
        )
        self.fields['social_youtube'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'e.g. https://youtube.com/username'
            }
        )
        self.fields['social_website'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'e.g. https://domain.com'
            }
        )
        self.fields['phone'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'e.g. +998949082644'
            }
        )

class SkillCreationForm(forms.ModelForm):
    class Meta:
        model=Skill
        fields=['name','description']


    def __init__(self,*args,**kwargs):
        super(SkillCreationForm,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'e.g. JavaScript'
            }
        )
        self.fields['description'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'description'
            }
        )