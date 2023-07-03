from django import forms

class WordInputForm(forms.Form):
    inputWords = forms.CharField(label="Input Here", max_length=(1024))