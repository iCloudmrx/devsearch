from django import  forms
from .models import Project,Review

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image','description','demo_link','source_link','tags']
        widgets={
            'tags': forms.CheckboxSelectMultiple(),
            'featured_image': forms.FileInput()
        }

    def __init__(self,*args,**kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {
                'class': 'input',
                'placeholder': 'Add Title'
            }
        )
        self.fields['description'].widget.attrs.update(
            {
                'class': 'input',
                'placeholder': 'Add Description'
            }
        )
        self.fields['demo_link'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'Add Live Demo'
            }
        )
        self.fields['source_link'].widget.attrs.update(
            {
                'class': 'input',
                'placeholder': 'Add Source Link'
            }
        )

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['value','body']
        labels={
            'value': 'vote',
            'body': 'Add a comment with your vote'
        }
    def __init__(self,*args,**kwargs):
        super(ReviewForm,self).__init__(*args,**kwargs)

        self.fields['value'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'Place your vote'
            }
        )
        self.fields['body'].widget.attrs.update(
            {
                'class': 'input input--text',
                'placeholder': 'Write your comments here...'
            }
        )