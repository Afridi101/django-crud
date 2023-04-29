from django import forms


class userForm(forms.Form):
    pid = forms.IntegerField(
        required=False, widget=forms.TextInput(attrs={'type': 'hidden'}))
    name = forms.CharField(label='Your Name', min_length=2, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'name': 'name'}))
    email = forms.EmailField(label='Email', min_length=2, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'name': 'email'}))
    # file = forms.ImageField(label='Thumbnail', required=False, widget=forms.FileInput(
    #     attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', min_length=2, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'name': 'password'}))
