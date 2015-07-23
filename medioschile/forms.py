from django import forms

class ContactoForm(forms.Form):
	su_nombre = forms.CharField(label='Nombre', max_length=200)
	asunto = forms.CharField(label='Asunto', max_length=100)
	mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)
	email = forms.EmailField()
	cc_myself = forms.BooleanField(label='Nombre', required=False)