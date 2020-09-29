from django import forms


class DescriptionForm(forms.Form):
    description = forms.CharField(max_length=1024)
