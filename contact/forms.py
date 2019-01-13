from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(label="Your e-mail address", required=True)
    subject = forms.CharField(label="Subject", required=True)
    message = forms.CharField(label="Your message", widget=forms.Textarea, required=True)
