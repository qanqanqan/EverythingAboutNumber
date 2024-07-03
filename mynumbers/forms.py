from django import forms


class NumberInputForm(forms.Form):
    number = forms.IntegerField()
