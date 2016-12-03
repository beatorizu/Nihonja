from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactCard(forms.Form):
    name = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Mensagem|Dúvida', widget=forms.Textarea(attrs={'class': 'form-control'}))

    def send_mail(self, card):
        subject = '[%s] Contato' % card
        message = 'Nome: %(name)s; Email: %(email)s; %(message)s'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        message = message % context
        send_mail(subject, message, settings.DEFAUL_FROM_EMAIL, [settings.CONTACT_EMAIL])
