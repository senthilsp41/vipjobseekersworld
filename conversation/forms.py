from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model=ConversationMessage
        fields={'content',}
        widgets={
            'content':forms.Textarea(attrs={
                'class':'form-control w-100 py-3 px-4 rounded border',
                'placeholder':'Enter your Message',
            })
        }