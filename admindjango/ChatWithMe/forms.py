from django import forms
from .models import Chat


class ChatModelForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = [#'user',
                  'content']
    # exclude = ['user']

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if content == 'abs':
            raise forms.ValidationError("Content can't be abs")
        return content
