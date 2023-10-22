from django import forms


class ShareForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
