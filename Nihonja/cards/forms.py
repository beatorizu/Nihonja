from django import forms

class ContactCard(forms.Form):
    name = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Mensagem|Dúvida', widget=forms.Textarea(attrs={'class': 'form-control'}))
