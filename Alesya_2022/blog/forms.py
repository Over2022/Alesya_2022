from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(max_length=60,
                             widdget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Ваше имя'
                             })
                             )

    body=forms.CharField(
                             widdget=forms.Textarea(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Ваш комментарий'
                             })
                             )
