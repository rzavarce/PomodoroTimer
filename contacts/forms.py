from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('cnt_name', 'cnt_email','cnt_message')

