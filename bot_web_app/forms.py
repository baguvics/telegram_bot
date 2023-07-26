from django import forms

class MessageForm(forms.Form):
    user = forms.CharField(max_length=100)
    chat_id = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    command = forms.CharField(max_length=50)


class CommandForm(forms.Form):
    command = forms.CharField(max_length=100)
    description = forms.CharField(max_length=900)
