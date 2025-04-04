from django import forms


class SendMailForm(forms.Form):
    full_name = forms.CharField(
        max_length=80,
        widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی'})
    )
    email = forms.EmailField(
        max_length=80,
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'})
    )
    subject = forms.CharField(
        max_length=80,
        widget=forms.TextInput(attrs={'placeholder': 'موضوع'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'پیام شما'})
    )