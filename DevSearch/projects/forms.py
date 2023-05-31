from django import  forms
from .models import Project

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
