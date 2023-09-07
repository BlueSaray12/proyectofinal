from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(

        attrs={'class': 'form-control bg-light border-0 px-4',
               'placeholder': 'Your Name', 'style': 'height: 55px;'}
    ), min_length=3, max_length=1000)
    email = forms.EmailField(label="Correo", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control bg-light border-0 px-4',
               'placeholder': 'Your Email', 'style': 'height: 55px;'}
    ))

    subject = forms.CharField(label="Asunto", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control bg-light border-0 px-4',
               'placeholder': 'Subject', 'style': 'height: 55px;'}
    ), min_length=3, max_length=1000)
    message = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(
        attrs={'class': 'form-control bg-light border-0 px-4',
               'placeholder': 'Message'}
    ), min_length=3, max_length=1000)
