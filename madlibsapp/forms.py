from django import forms

class WordInputForm(forms.Form):
    inputWords = forms.CharField(label="Words", max_length=(2048))