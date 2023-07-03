from django import forms

class WordInputForm(forms.Form):
    inputWords = forms.CharField(label="userWords", max_length=(1024))