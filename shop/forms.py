from django import forms


class SearchForm(forms.Form):
    question = forms.ChoiceField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type your kayword...'}))
