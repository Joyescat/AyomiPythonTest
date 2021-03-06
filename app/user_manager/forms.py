from django import forms

from authentication.models import User

class EditUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['email']
		widgets = {
			'email': forms.EmailInput(
				attrs = {
					'class': 'form-control',
					'id': 'new-email',
					'placeholder': 'E-mail'
				})
		}
