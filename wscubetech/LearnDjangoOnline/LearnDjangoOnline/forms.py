from django import forms

class djangoform(forms.Form):
    fn = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    ln = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
