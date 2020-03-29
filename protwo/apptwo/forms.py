from django import forms
from apptwo.models import User

class NewUserForm(forms.ModelForm):
	class Meta:
		model = User #model is a key word n hence should always remain same
					 #Also the name ,here 'User' should be the same as the model name in models.py
		fields = '__all__'