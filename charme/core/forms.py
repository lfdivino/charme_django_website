from django import forms


class ContatoForm(forms.Form):
    name = forms.CharField(label='Nome Completo', widget=forms.TextInput(attrs={'placeholder': 'Nome', 'class': 'form-control'}))
    phone = forms.CharField(label='Telefone', widget=forms.TextInput(attrs={'placeholder': 'Telefone', 'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Digite aqui a sua mensagem', 'class': 'form-control'}),
        label='Mensagem'
    )
