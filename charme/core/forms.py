from django import forms


class ContatoForm(forms.Form):
    name = forms.CharField(label='Nome Completo', widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    phone = forms.CharField(label='Telefone', widget=forms.TextInput(attrs={'placeholder': 'Telefone'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Digite aqui a sua mensagem'}),
        label='Mensagem'
    )
