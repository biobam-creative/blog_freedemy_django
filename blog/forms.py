from django import forms


def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')


class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(
        attrs={'name': 'message', 'placeholder': 'Your Message', 'cols': 30, 'rows': 9, 'class': 'form-control w-100', }))
    name = forms.CharField(max_length=80, widget=forms.TextInput(
        attrs={'name': 'name', 'placeholder': 'Enter Your Name', 'class': "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'name': 'email', 'placeholder': 'Enter Your Email', 'class': "form-control"}))
    subject = forms.IntegerField(widget=forms.NumberInput(
        attrs={'name': 'subject', 'placeholder': 'Enter Your Phone Number', 'class': "form-control"}))
    forcefield = forms.CharField(
        required=False, widget=forms.HiddenInput, label="Leave empty", validators=[should_be_empty])
